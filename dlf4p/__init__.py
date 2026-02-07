"""Dexoron Logging Framework (dlf-py)."""

from .logger import (
    Logger,
    help,
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
    "help",
    "Logger",
    "setup",
    "debug",
    "info",
    "success",
    "warning",
    "error",
    "fatal",
    "exception",
]

from .utils import VERSION
__version__ = VERSION
