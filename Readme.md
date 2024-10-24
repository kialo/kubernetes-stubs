# kubernetes-stubs

Python type stubs for the [Kubernetes API client](https://github.com/kubernetes-client/python).
The code is contained in branches, which are named after the respective Kubernetes version.

## Usage

```bash
pip install git+https://github.com/kialo/kubernetes-stubs.git@v1.29
```

Change the version number accordingly.

## Updating stubs

- Commit your changes to non-autogenerated code on `master`.
  I.e. missing type annotations, dependency upgrades, etc.
- Branch off or merge `master` into the corresponding version branch.
- Checkout the corresponding version of the kubernetes-client submodule.
- Generate API model stubs for each version branch independently: `uv run codegen`.
