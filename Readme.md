# kubernetes-stubs

Python type stubs for the [Kubernetes API client](https://github.com/kubernetes-client/python).

At Kialo, we only have a single Kubernetes version in use at each time.
For a simplified release process, we release new stubs versions only for that version.
See tags for available list.

## Usage

```bash
pip install git+https://github.com/kialo/kubernetes-stubs.git@v1.29
```

Change the version number accordingly.

## Update def dependencies

Dev dependencies are currently only pinned via uv's lock file. You can upgrade them via:

```bash
uv sync --upgrade
```

## Generate stubs for a new version

- Update `kubernetes-client` submodule to target release
- Update `pyproject.toml` version
- Generate API models: `uv run codegen ${target-version}`
- Commit changes
- Release new tag: `git tag v${version}; git push v${version}`
