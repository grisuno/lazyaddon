"""lazyaddon: declarative tool and extension manager.

Turns any GitHub/GitLab project into an installable, runnable addon from a
single YAML file. Usable programmatically through :class:`LazyAddonEngine`,
via the ``lazyaddon`` console script, or through a declarative project YAML
for non-programmers.
"""

from __future__ import annotations

from .config import AddonConfig
from .engine import LazyAddonEngine
from .installer import AddonInstaller
from .models import AddonError, AddonParam, AddonSpec, SchemaError, ToolSpec
from .placeholders import PlaceholderEngine
from .runner import AddonHook, AddonRunner, CommandResult, CommandRunner
from .security import SecurityPolicy

__version__ = "1.0.0"

__all__ = [
    "AddonConfig",
    "AddonError",
    "AddonHook",
    "AddonInstaller",
    "AddonParam",
    "AddonRunner",
    "AddonSpec",
    "CommandResult",
    "CommandRunner",
    "LazyAddonEngine",
    "PlaceholderEngine",
    "SchemaError",
    "SecurityPolicy",
    "ToolSpec",
    "__version__",
]
