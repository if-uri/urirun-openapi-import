# Changelog

## [Unreleased]

## [0.1.1] - 2026-07-05

### Docs
- Update README.md

### Test
- Update tests/__pycache__/test_import_pure.cpython-313-pytest-9.1.1.pyc
- Update tests/__pycache__/test_openapi_import.cpython-313-pytest-9.1.1.pyc
- Update tests/test_import_pure.py
- Update tests/test_openapi_import.py

### Other
- Update .gitignore
- Update dist/urirun_openapi_import-0.1.0-py3-none-any.whl
- Update dist/urirun_openapi_import-0.1.0.tar.gz
- Update src/urirun_openapi_import.egg-info/PKG-INFO
- Update src/urirun_openapi_import.egg-info/SOURCES.txt
- Update uv.lock


All notable changes to `urirun-openapi-import` are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2026-06-26

### Added
- Initial release. Import an OpenAPI/Swagger spec as urirun URI bindings (each operation → a typed
  `http-service` route) — extracted from `urirun.connectors.openapi_import` as a standalone,
  dependency-free package.
- Back-compat: the old import path `urirun.connectors.openapi_import` keeps working via a
  `sys.modules` re-export shim; `node/mesh.py` loads it lazily (the `add_openapi` CLI command).
