"""Dexoron Logging Framework (dlf-py)."""

from .logger import (
    Logger,
    setup,
    debug,
    info,
    success,
    warning,
    error,
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

__version__ = "1.2.0"
