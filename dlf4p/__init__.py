"""Dexoron Logging Framework (dlf-py)."""

from .logger import (
    Logger,
    help,
    debug,
    info,
    success,
    warning,
    error,
    exception,
    fatal,
)

__all__ = [
    "help",
    "Logger",
    "debug",
    "info",
    "success",
    "warning",
    "error",
    "fatal",
    "exception",
]

from .config import VERSION

__version__ = VERSION
