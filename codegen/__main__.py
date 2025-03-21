import collections
import json
import keyword
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from subprocess import run
from typing import Any
import tomllib

import inflection

target_version = sys.argv[1]

print(f"Ensure environment is set up for {target_version}")

current_submodule_rev = run(
    ["git", "rev-parse", "HEAD"],
    capture_output=True,
    universal_newlines=True,
    check=True,
    cwd="kubernetes-client",
)
expected_submodule_rev = run(
    ["git", "rev-parse", f"v{target_version}"],
    capture_output=True,
    universal_newlines=True,
    check=True,
    cwd="kubernetes-client",
)
if current_submodule_rev.stdout != expected_submodule_rev.stdout:
    print(
        f"The kubernetes-client submodule must trackt the target revision ({target_version} => {expected_submodule_rev.stdout.strip()}); however, it is at {current_submodule_rev.stdout.strip()}"
    )
    sys.exit(1)

pyproject = tomllib.load(open("pyproject.toml", "rb"))
if (py_version := pyproject["project"]["version"]) != target_version:
    print(f"The pyproject's version is at {py_version} not {target_version}")
    sys.exit(1)

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_FILE = ROOT_DIR / "kubernetes-client" / "scripts" / "swagger.json"
STUBS_DIR = ROOT_DIR / "kubernetes-stubs"
CLIENT_STUBS_DIR = STUBS_DIR / "client"
MODELS_STUBS_DIR = CLIENT_STUBS_DIR / "models"
API_STUBS_DIR = CLIENT_STUBS_DIR / "api"

schema = json.load(open(SCHEMA_FILE))

shutil.rmtree(STUBS_DIR, ignore_errors=True)
shutil.copytree(ROOT_DIR / "codegen" / "base", ROOT_DIR, dirs_exist_ok=True)


class CodegenBuf:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open(mode="a")
        self.indent = 0

    def writeln(self, s: str = ""):
        print(f"{self.indent * '    '}{s}", file=self.file)

    def start_block(self, s: str):
        self.writeln(f"{s}:")
        self.indent += 1

    def end_block(self):
        self.indent -= 1


def make_class_name(s: str):
    return inflection.camelize("".join(s[0].upper() + s[1:] for s in s.split(".")))


def make_file_name(s: str):
    return "_".join(inflection.underscore(s) for s in s.split("."))


def make_type_name(config: dict[str, Any], use_dict: bool = False) -> str:
    def inner():
        ty = config.get("type")
        if not ty and "schema" in config:
            ty = config["schema"].get("type")
        if ty:
            if ty == "boolean":
                return "bool"
            elif ty == "string":
                if config.get("format") == "date-time":
                    return "datetime.datetime"
                else:
                    return "str"
            elif ty == "integer":
                return "int"
            elif ty == "number":
                return "float"
            elif ty == "array":
                item_ty = make_type_name(config["items"], use_dict=use_dict)
                return f"list[{item_ty}]"
            elif ty == "object":
                if "additionalProperties" in config:
                    val_ty = make_type_name(
                        config["additionalProperties"],
                        use_dict=use_dict,
                    )
                    return f"dict[str, {val_ty}]"
                else:
                    return "typing.Any"
            else:
                assert "unknown type"

        ref = config.get("$ref") or config["schema"]["$ref"]
        assert ref.startswith("#/definitions/")
        ref = ref.removeprefix("#/definitions/")
        out = "kubernetes.client." + make_class_name(ref)
        if use_dict:
            out += "Dict"
        return out

    return inner()


def make_property_name(s: str, underscored: bool = True):
    if underscored:
        s = inflection.underscore(s)
    else:
        s = s.replace("-", "_")
    s = s.replace("$", "")
    if keyword.iskeyword(s):
        return "_" + s
    return s


@dataclass
class Property:
    name: str
    ty: str
    is_optional_argument: bool
    is_optional_attribute: bool

    def __str__(self):
        return f"{self.name}: {self.ty}"

    def typing(self, attribute: bool) -> str:
        if (attribute and self.is_optional_attribute) or (
            self.is_optional_argument and not attribute
        ):
            return f"{self.name}: typing.Optional[{self.ty}]"
        return f"{self.name}: {self.ty}"

    def arg_str(self) -> str:
        s = self.typing(attribute=False)
        if self.is_optional_argument:
            s += " = None"
        return s

    def param_str(self) -> str:
        s = self.typing(attribute=False)
        if self.is_optional_argument:
            s += " = ..."
        return s


@dataclass(eq=True, frozen=True)
class Manager:
    name: str
    api_name: str


@dataclass
class ManagerOp:
    name: str
    api_name: str
    required_params: list[Property]
    optional_params: list[Property]
    return_ty: str


# `kubernetes.client.models` modules.
for name, config in schema["definitions"].items():
    class_name = make_class_name(name)
    file_name = make_file_name(name)
    # Required arguments are those documented as required in the swagger spec
    required_arguments = config.get("required", [])
    # Required attributes are those that are always included in an API response
    required_attributes = list(required_arguments)
    props: list[Property] = []
    dict_props: list[Property] = []
    if "apiVersion" in config["properties"]:
        # Top-level attributes can't be None
        required_attributes += ["apiVersion", "kind", "metadata", "spec", "status"]
    elif class_name.startswith("V1ObjectMeta"):
        required_arguments.append(["name"])
        required_attributes += ["name", "namespace", "uid", "labels"]
    for name, config in config["properties"].items():
        is_optional_argument = name not in required_arguments
        is_optional_attribute = name not in required_attributes
        props.append(
            Property(
                name=make_property_name(name),
                ty=make_type_name(config),
                is_optional_argument=is_optional_argument,
                is_optional_attribute=is_optional_attribute,
            )
        )
        dict_props.append(
            Property(
                name=make_property_name(name, underscored=False),
                ty=make_type_name(config, use_dict=True),
                is_optional_argument=is_optional_argument,
                is_optional_attribute=is_optional_attribute,
            )
        )
    buf = CodegenBuf(MODELS_STUBS_DIR / (file_name + ".pyi"))
    buf.writeln("import datetime")
    buf.writeln("import kubernetes.client")
    buf.writeln("import typing")
    buf.writeln()
    buf.start_block(f"class {class_name}")
    for prop in props:
        buf.writeln(prop.typing(attribute=True))
    buf.writeln()
    params_str = ", ".join(prop.param_str() for prop in props)
    buf.start_block(f"def __init__(self, *, {params_str}) -> None")
    buf.writeln("...")
    buf.end_block()
    buf.start_block(f"def to_dict(self) -> {class_name}Dict")
    buf.writeln("...")
    buf.end_block()
    buf.end_block()
    buf.start_block(f"class {class_name}Dict(typing.TypedDict, total=False)")
    for dict_prop in dict_props:
        buf.writeln(str(dict_prop))
    buf.end_block()

# `kubernetes.client.models` root.
buf = CodegenBuf(MODELS_STUBS_DIR / "__init__.pyi")
for name in schema["definitions"]:
    buf.writeln(
        f"from kubernetes.client.models.{make_file_name(name)} import {make_class_name(name)} as {make_class_name(name)}"
    )
    buf.writeln(
        f"from kubernetes.client.models.{make_file_name(name)} import {make_class_name(name)}Dict as {make_class_name(name)}Dict"
    )

# `kubernetes.client.api` modules.
apis: collections.defaultdict[str, Any] = collections.defaultdict(list)
for name, config in schema["paths"].items():
    for method in ["get", "put", "post", "delete", "options", "head", "patch"]:
        if method not in config:
            continue
        op = config[method]
        if "parameters" in config:
            op["parameters"] = config["parameters"] + op.get("parameters", [])
        op["path"] = name
        for tag in op.get("tags", []):
            apis[tag].append(op)
managers: collections.defaultdict[Manager, list[ManagerOp]] = collections.defaultdict(
    list
)
for name, api in apis.items():
    class_name = make_class_name(name)
    buf = CodegenBuf(API_STUBS_DIR / f"{name}_api.pyi")
    buf.writeln("import kubernetes.client")
    buf.writeln("import typing")
    buf.writeln()
    buf.start_block(f"class {class_name}Api")
    buf.start_block(
        "def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None"
    )
    buf.writeln("...")
    buf.end_block()
    for op in api:
        name = inflection.underscore(op["operationId"])
        responses = op["responses"]
        if "200" in responses:
            return_ty = make_type_name(responses["200"]["schema"])
        else:
            return_ty = "None"
        params: list[Property] = []
        for param in op.get("parameters", []):
            is_optional_argument = not param.get("required", False)
            param_name = param["name"]
            i = 2
            while any(param.name == param_name for param in params):
                param_name = param["name"] + str(i)
                i += 1
            params.append(
                Property(
                    name=make_property_name(param_name),
                    ty=make_type_name(param),
                    is_optional_argument=is_optional_argument,
                    is_optional_attribute=False,
                )
            )
        required_params, optional_params = [], []
        for param in params:
            if param.is_optional_argument:
                optional_params.append(param)
            else:
                required_params.append(param)
        required_params_str = ", ".join(param.param_str() for param in required_params)
        if required_params_str:
            required_params_str = ", " + required_params_str
        optional_params_str = ", ".join(param.param_str() for param in optional_params)
        if optional_params_str:
            optional_params_str = ", *, " + optional_params_str
        params_str = required_params_str + optional_params_str
        if "x-kubernetes-group-version-kind" in op:
            is_namespaced = any(param.name == "namespace" for param in params)
            gvk = op["x-kubernetes-group-version-kind"]
            [op_name, resource_name] = name.split("_", 1)
            manager = Manager(
                name=make_class_name(
                    ".".join(
                        [
                            class_name,
                            resource_name,
                        ]
                    )
                ),
                api_name=class_name,
            )
            manager_op = ManagerOp(
                name=op_name,
                api_name=name,
                required_params=required_params,
                optional_params=optional_params,
                return_ty=return_ty,
            )
            managers[manager].append(manager_op)
        buf.start_block(f"def {name}(self{params_str}) -> {return_ty}")
        buf.writeln("...")
        buf.end_block()
    buf.end_block()

# `kubernetes.client.api` root.
buf = CodegenBuf(API_STUBS_DIR / "__init__.pyi")
for name in apis:
    buf.writeln(
        f"from kubernetes.client.api.{name}_api import {make_class_name(name)}Api as {make_class_name(name)}Api"
    )

# `kubernetes.client` root.
buf = CodegenBuf(CLIENT_STUBS_DIR / "__init__.pyi")
for name in schema["definitions"]:
    buf.writeln(
        f"from kubernetes.client.models.{make_file_name(name)} import {make_class_name(name)} as {make_class_name(name)}"
    )
    buf.writeln(
        f"from kubernetes.client.models.{make_file_name(name)} import {make_class_name(name)}Dict as {make_class_name(name)}Dict"
    )
for name in apis:
    buf.writeln(
        f"from kubernetes.client.api.{name}_api import {make_class_name(name)}Api as {make_class_name(name)}Api"
    )

# `kubernetes` root.
buf = CodegenBuf(STUBS_DIR / "__init__.pyi")
for submodule in sorted(STUBS_DIR.iterdir()):
    if submodule.is_dir() or (
        submodule.suffix == ".pyi" and not submodule.name.startswith("_")
    ):
        buf.writeln(f"from . import {submodule.stem} as {submodule.stem}")

process = run(["ruff", "check", "--fix", "--quiet", STUBS_DIR])
process = run(["ruff", "format", "--quiet", STUBS_DIR])

print(f"Stubs gernated for {target_version}")
