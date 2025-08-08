# More Math

Adds math nodes for numbers and types which do not need it. I got inspired by was_extras node.

#WARNING This node is not compatible to ComfyUI-Impact-Pack which forces older antlr version.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Clone this repository into `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

# Features

- expression parsing with support for functions (sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, abs, sqrt, ln, log, exp, pow, smin, tmin, smax, tmax, tnorm,snorm (norm not applicable on number math node), floor, ceil, round, gamma,clamp,sigmoid), math operators (binary and unary +,- and ^,*,/,%) and constants (e,pi)
- run expressions on both components of CONDITIONING (not that I know what they do), LATENT, IMAGE and FLOAT

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd more_math
pip install -e .[dev]
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will automatically be picked up the next time you run ComfyUI.

## Publish to Github

## Tests

This repo contains unit tests written in Pytest in the `tests/` directory. It is recommended to unit test your custom node.

- [build-pipeline.yml](.github/workflows/build-pipeline.yml) will run pytest and linter on any open PRs
- [validate.yml](.github/workflows/validate.yml) will run [node-diff](https://github.com/Comfy-Org/node-diff) to check for breaking changes

## Publishing to Registry

If you wish to share this custom node with others in the community, you can publish it to the registry. We've already auto-populated some fields in `pyproject.toml` under `tool.comfy`, but please double-check that they are correct.

You need to make an account on https://registry.comfy.org and create an API key token.

- [ ] Go to the [registry](https://registry.comfy.org). Login and create a publisher id (everything after the `@` sign on your registry profile). 
- [ ] Add the publisher id into the pyproject.toml file.
- [ ] Create an api key on the Registry for publishing from Github. [Instructions](https://docs.comfy.org/registry/publishing#create-an-api-key-for-publishing).
- [ ] Add it to your Github Repository Secrets as `REGISTRY_ACCESS_TOKEN`.

A Github action will run on every git push. You can also run the Github action manually. Full instructions [here](https://docs.comfy.org/registry/publishing). Join our [discord](https://discord.com/invite/comfyorg) if you have any questions!

