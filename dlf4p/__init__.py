"""Dexoron Logging Framework (dlf-py)."""

from .logger import (
    Logger,
    setup,
    debug,
    info,
    success,
    warning,
    error,
    exception,
    fatal,
)

__all__ = [
    "Logger",
    "setup",
    "debug",
    "info",
    "success",
    "warning",
    "error",
    "fatal",
]

from .utils import VERSION
__version__ = VERSION
