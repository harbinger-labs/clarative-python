from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `clarative.resources` module.

    This is used so that we can lazily import `clarative.resources` only when
    needed *and* so that users can just import `clarative` and reference `clarative.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("clarative.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
