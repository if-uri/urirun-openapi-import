# Author: Tom Sapletta · Part of the ifURI solution.
"""Pure unit tests of the OpenAPI→bindings mapping — no urirun runtime needed, so they run in
the isolated package-test env (where the integration tests skip)."""
from __future__ import annotations

from urirun_openapi_import.openapi_import import _route_uri, import_openapi

SPEC = {
    "openapi": "3.0.0",
    "servers": [{"url": "https://api.example.test"}],
    "paths": {
        "/things": {
            "get": {"operationId": "listThings", "summary": "List things"},
            "post": {"operationId": "makeThing", "summary": "Make a thing"},
        },
    },
}


def test_route_uri_maps_get_to_query_and_post_to_command():
    assert "/query/" in _route_uri("demo", "api", "get", "/things")
    assert "/command/" in _route_uri("demo", "api", "post", "/things")


def test_import_openapi_builds_bindings():
    out = import_openapi(SPEC, scheme="demo")
    b = out.get("bindings", out)
    uris = list(b)
    assert len(uris) == 2
    assert any("/query/" in u for u in uris)
    assert any("/command/" in u for u in uris)
