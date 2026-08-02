"""
PROJECT BRAHMA
Universal Runtime Registry

Author:
    Ramendra Singh Rajput

Description
-----------
The Runtime Registry is the central discovery mechanism of
Project BRAHMA.

All runtime components are registered here.

Responsibilities
----------------

• Service Registry

• Laboratory Registry

• Provider Registry

Future

• Agent Registry

• Tool Registry

• Workflow Registry

• Plugin Registry

Philosophy
----------

Register once.

Access everywhere.

No direct dependencies.
"""

from __future__ import annotations

from typing import Any


class RuntimeRegistry:
    """
    Universal Runtime Registry.
    """

    def __init__(self):

        self._services: dict[str, Any] = {}

        self._labs: dict[str, Any] = {}

        self._providers: dict[str, Any] = {}

    # ==========================================================
    # Services
    # ==========================================================

    def register_service(self, name: str, service: Any) -> None:

        self._services[name] = service

    def get_service(self, name: str) -> Any:

        return self._services.get(name)

    def has_service(self, name: str) -> bool:

        return name in self._services

    def list_services(self) -> list[str]:

        return sorted(self._services.keys())

    # ==========================================================
    # Laboratories
    # ==========================================================

    def register_lab(self, name: str, lab: Any) -> None:

        self._labs[name] = lab

    def get_lab(self, name: str) -> Any:

        return self._labs.get(name)

    def has_lab(self, name: str) -> bool:

        return name in self._labs

    def list_labs(self) -> list[str]:

        return sorted(self._labs.keys())

    # ==========================================================
    # Providers
    # ==========================================================

    def register_provider(self, name: str, provider: Any) -> None:

        self._providers[name] = provider

    def get_provider(self, name: str) -> Any:

        return self._providers.get(name)

    def has_provider(self, name: str) -> bool:

        return name in self._providers

    def list_providers(self) -> list[str]:

        return sorted(self._providers.keys())

    # ==========================================================
    # Utilities
    # ==========================================================

    def clear(self) -> None:

        self._services.clear()

        self._labs.clear()

        self._providers.clear()

    def summary(self) -> dict[str, int]:

        return {
            "services": len(self._services),
            "labs": len(self._labs),
            "providers": len(self._providers),
        }


#
# Global Registry
#

runtime_registry = RuntimeRegistry()