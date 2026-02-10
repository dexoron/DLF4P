# dlf4p — Dexoron Logging Framework for Python

`dlf4p` is a lightweight and convenient logger for Python inspired by **SLF4J**.
It provides a simple API for logging messages with support for log levels, colored console output, timestamps, and file logging.

The project is being developed as part of the **DLF (Dexoron Logging Framework)** family, with plans for implementations in other programming languages.

GitLab repository: https://gitlab.com/dexoron/dlf4p
PyPi project: https://pypi.org/project/dlf4p

---

## Features

* Log levels: `DEBUG`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `FATAL`, `EXCEPTION`
* Colored console output
* Timestamp support
* Prefix support (e.g., module or component name)
* File logging
* Configuration via `dlf_settings.json`
* Traceback output for exceptions
* Exception logging helper: `exception()`
* Lightweight and with no external dependencies

---

## Installation

Install from PyPI:

```bash
pip install dlf4p
```

---

## Quick Start

```python
import dlf4p as dlf

dlf.info("Application started", "Main")
dlf.success("Server successfully started", "Server")
dlf.warning("Slow response", "API")
dlf.error("Database connection error", "Database")
dlf.fatal("Critical error", "System")

try:
    1 / 0
except Exception as e:
    dlf.error("Division failed", "Math", exc=e)
    dlf.exception("Unhandled error", "Math", exc=e)
```

Console output:

```log
[14:24:56] [Main/INFO]: Application started
[14:24:56] [Server/SUCCESS]: Server successfully started
[14:24:56] [API/WARNING]: Slow response
[14:24:56] [Database/ERROR]: Database connection error
[14:24:56] [System/FATAL]: Critical error
[14:24:56] [Math/ERROR]: Division failed
Traceback (most recent call last):
  File "/home/probrovova/project/dlf-py/test/main.py", line 30, in <module>
    1 / 0
ZeroDivisionError: division by zero
[14:24:56] [Math/EXCEPTION]: Unhandled error
Traceback (most recent call last):
  File "/home/probrovova/project/dlf-py/test/main.py", line 30, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

Logger class example:

```python
import dlf4p as dlf

log = dlf.Logger("Main")
log.info("Application started")

log = dlf.Logger("Core")
log.setLevel(2)  # SUCCESS and higher
log.info("Core module initialized")
log.success("Submodule loaded successfully")
log.warning("Disabled System modules")

try:
    raise ValueError("Bad value")
except Exception as e:
    log.exception("Something went wrong", exc=e)
```

Console output:

```log
[14:26:59] [Main/INFO]: Application started
[14:26:59] [Core/INFO]: Log level set to SUCCESS
[14:26:59] [Core/SUCCESS]: Submodule loaded successfully
[14:26:59] [Core/WARNING]: Disabled System modules
[14:26:59] [Core/EXCEPTION]: Something went wrong
Traceback (most recent call last):
  File "/home/probrovova/project/dlf-py/test/main.py", line 31, in <module>
    raise ValueError("Bad value")
ValueError: Bad value
```

> Logs are saved to a file without ANSI color codes.
> Traceback output uses the provided `exc` object.

---

## Configuration

Configuration is loaded from `dlf_settings.json` in the current working directory.
If the file does not exist, it will be created with defaults on first import.

Example `dlf_settings.json`:

```json
{
  "custom_prefix": "",
  "use_time": true,
  "use_color": true,
  "use_file_logging": true,
  "log_filename": "log-{get_data}-{get_time}.log"
}
```

### Fields:

* `custom_prefix` — custom format string (empty string uses default format)
* `use_time` — enable or disable timestamps
* `use_color` — enable or disable colors
* `use_file_logging` — enable writing logs to a file
* `log_filename` — template for log file name, supports `{get_data}` and `{get_time}`

---

## Run Example

From the project root:

```bash
python3 -m test.main
```

---

## Philosophy

`dlf4p` is inspired by **SLF4J (Simple Logging Facade for Java)** and aims to:

* provide a simple and unified logging interface
* remain minimalistic
* have no external dependencies
* be easily extensible to other programming languages

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

**Dexoron**

GitLab: [https://gitlab.com/dexoron](https://gitlab.com/dexoron)
GitHub: [https://github.com/dexoron](https://github.com/dexoron)
Website: [https://dexoron.su](https://dexoron.su)

---

## Project Links

Changelog: `CHANGELOG`  
Contributing guide: `CONTRIBUTING.md`
GitLab repository: https://gitlab.com/dexoron/dlf4p
PyPi project: https://pypi.org/project/dlf4p

---

> dlf4p — a simple logger today, a full logging framework tomorrow.
