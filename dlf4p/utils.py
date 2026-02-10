import traceback
from .config import (
    red,
    reset,
    log_filename,
    use_file_logging,
    custom_prefix,
    use_color,
    use_time,
)
from datetime import datetime


def log_file(msg: str) -> None:
    file_name: str = log_filename.format(get_data=get_data(), get_time=get_time())
    with open(file_name, "a") as log_handle:
        log_handle.write(msg + "\n")


def get_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


def get_data() -> str:
    return datetime.now().strftime("%d.%m.%Y")


def format_log(
    level: str = "",
    prefix: str = "",
    msg: str = "!!!NOT MSG CONTENT!!!",
    color: str = "",
    exc: Exception | None = None,
) -> None:
    default_prefix: str = "{color}" if use_color else ""
    default_prefix += "[{time}] " if use_time else ""
    default_prefix += "[{prefix}/{level}]: {msg}" if prefix else "[{level}]: {msg}"
    default_prefix += "{reset_color}" if use_color else ""

    exc_text: str | None = None
    if exc is not None:
        if exc.__traceback__ is not None:
            exc_text = "".join(
                traceback.format_exception(type(exc), exc, exc.__traceback__)
            ).rstrip()
        else:
            exc_text = f"{type(exc).__name__}: {exc}"

    if custom_prefix == "":
        print(
            default_prefix.format(
                color=color if color != "" else "",
                time=get_time(),
                prefix=prefix,
                level=level,
                msg=msg,
                reset_color=reset if color != "" else "",
            )
        )
        if exc_text is not None:
            if use_color:
                print(f"{red}{exc_text}{reset}")
            else:
                print(exc_text)
        if use_file_logging:
            log_file(
                default_prefix.format(
                    color="",
                    time=get_time(),
                    prefix=prefix,
                    level=level,
                    msg=msg,
                    reset_color="",
                )
            )
            if exc_text is not None:
                log_file(exc_text)
    else:
        print(
            custom_prefix.format(
                color=color if color != "" else "",
                time=get_time(),
                prefix=prefix,
                level=level,
                msg=msg,
                reset_color=reset if color != "" else "",
            )
        )
        if exc_text is not None:
            if use_color:
                print(f"{red}{exc_text}{reset}")
            else:
                print(exc_text)
        if use_file_logging:
            log_file(
                custom_prefix.format(
                    color="",
                    time=get_time(),
                    prefix=prefix,
                    level=level,
                    msg=msg,
                    reset_color="",
                )
            )
            if exc_text is not None:
                log_file(exc_text)
