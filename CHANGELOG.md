# Changelog

All notable changes to `urirun-openapi-import` are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2026-06-26

### Added
- Initial release. Import an OpenAPI/Swagger spec as urirun URI bindings (each operation → a typed
  `http-service` route) — extracted from `urirun.connectors.openapi_import` as a standalone,
  dependency-free package.
- Back-compat: the old import path `urirun.connectors.openapi_import` keeps working via a
  `sys.modules` re-export shim; `node/mesh.py` loads it lazily (the `add_openapi` CLI command).
