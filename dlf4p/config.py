import json

VERSION: str = "1.3.0"

try:
    with open("dlf_settings.json", "r", encoding="utf-8") as f:
        file = json.load(f)

except FileNotFoundError:
    settings = """{
    "custom_prefix": "{color}[{time}] [{prefix}/{level}]: {msg}{reset_color}",
    "custom_prefix_disc": "Хотите ли задать свой лог? Пример: '{color}!!![{time}] [{prefix}/{level}]: {msg}{reset_color}'",
    "use_time": true,
    "use_time_disc": "Писать время в лог?",
    "use_color": true,
    "use_color_disc": "Использовать цвета в консоли?",
    "use_file_logging": true,
    "use_file_logging_disc": "Логировать консоль в файл?",
    "log_filename": "logger-{get_data}-{get_time}.log",
    "log_filename_disc": "Имя файла лога"
}"""

    with open("dlf_settings.json", "w", encoding="utf-8") as f:
        f.write(settings)

    # ВАЖНО: перечитать файл
    file = json.loads(settings)


# Color
red: str = "\033[31m"
green: str = "\033[32m"
yellow: str = "\033[33m"
reset: str = "\033[0m"
bold_red: str = "\033[1;31m"

# Settings
custom_prefix: str = file.get("custom_prefix", "")
use_time: bool = file.get("use_time", True)
use_color: bool = file.get("use_color", True)
use_file_logging: bool = file.get("use_file_logging", True)

# Logs
levels: list[str] = [
    "DEBUG",
    "INFO",
    "SUCCESS",
    "WARNING",
    "ERROR",
    "FATAL",
    "EXCEPTION",
]
log_level: int = 0
log_filename: str = file.get("log_filename", "logger-{get_data}-{get_time}.log")
