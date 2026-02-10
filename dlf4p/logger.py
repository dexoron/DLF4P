from .utils import (
    format_log,
)
from .config import (
    red,
    green,
    yellow,
    bold_red,
    log_level,
    levels,
)


def help():
    print(
        """Welcome to the Dexoron Logging Framework for Python (DLF4P)!
Usage:
    1. Import the library:
        import dlf4p

    2. Setup the logger (optional):
        dlf4p.setup(time=True, color=True, simple=False, file_logging=True)

    3. Use loger

    3.1. Use Logger class:
        dlf = dlf4p.Logger("MyModule")

        dlf.info("This is an info message")
        dlf.success("This is a success message")
        dlf.warning("This is a warning message")
        dlf.error("This is an error message")
        dlf.debug("This is a debug message")

    3.2 Use global functions:
        dlf4p.info("This is an info message", prefix="MyModule")
        dlf4p.success("This is a success message", prefix="MyModule")
        dlf4p.warning("This is a warning message", prefix="MyModule")
        dlf4p.error("This is an error message", prefix="MyModule")
        dlf4p.debug("This is a debug message", prefix="MyModule")

    4. Set log level (optional):
        dlf.setLevel(2)  # Only log messages with level <= 2 (SUCCESS)
        # Levels: 0=DEBUG, 1=INFO, 2=SUCCESS, 3=WARNING, 4=ERROR, 5=FATAL

    See the documentation for more details and advanced usage!
    Senck you for using DLF4P!
"""
    )


class Logger:
    def __init__(self, prefix: str = ""):
        self.prefix = prefix

    def getLogger(self, prefix: str):
        return Logger(prefix)

    def setLevel(self, level: int):
        global log_level
        log_level = level
        format_log(
            "INFO",
            self.prefix,
            f"Log level set to {levels[level]}",
        )

    def debug(self, msg: str, exc: Exception | None = None):
        if log_level <= 0:
            format_log("DEBUG", self.prefix, msg, exc=exc)

    def info(self, msg: str, exc: Exception | None = None):
        if log_level <= 1:
            format_log("INFO", self.prefix, msg, exc=exc)

    def success(self, msg: str, exc: Exception | None = None):
        if log_level <= 2:
            format_log("SUCCESS", self.prefix, msg, green, exc=exc)

    def warning(self, msg: str, exc: Exception | None = None):
        if log_level <= 3:
            format_log("WARNING", self.prefix, msg, yellow, exc=exc)

    def error(self, msg: str, exc: Exception | None = None):
        if log_level <= 4:
            format_log("ERROR", self.prefix, msg, red, exc=exc)

    def fatal(self, msg: str, exc: Exception | None = None):
        if log_level <= 5:
            format_log("FATAL", self.prefix, msg, bold_red, exc=exc)

    def exception(self, msg: str, exc: Exception | None = None):
        format_log("EXCEPTION", self.prefix, msg, red, exc=exc)


def debug(msg: str, prefix: str = "", exc: Exception | None = None):
    if log_level <= 0:
        format_log("DEBUG", prefix, msg, exc=exc)


def info(msg: str, prefix: str = "", exc: Exception | None = None):
    if log_level <= 1:
        format_log("INFO", prefix, msg, exc=exc)


def success(msg: str, prefix: str = "", exc: Exception | None = None):
    if log_level <= 2:
        format_log("SUCCESS", prefix, msg, green, exc=exc)


def warning(msg: str, prefix: str = "", exc: Exception | None = None):
    if log_level <= 3:
        format_log("WARNING", prefix, msg, yellow, exc=exc)


def error(msg: str, prefix: str = "", exc: Exception | None = None):
    if log_level <= 4:
        format_log("ERROR", prefix, msg, red, exc=exc)


def fatal(msg: str, prefix: str = "", exc: Exception | None = None):
    if log_level <= 5:
        format_log("FATAL", prefix, msg, bold_red, exc=exc)


def exception(msg: str, prefix: str = "", exc: Exception | None = None):
    format_log("EXCEPTION", prefix, msg, red, exc=exc)
