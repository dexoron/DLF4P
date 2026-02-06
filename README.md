# dlf4p — Dexoron Logging Framework for Python

`dlf4p` is a lightweight and convenient logger for Python inspired by **SLF4J**.
It provides a simple API for logging messages with support for log levels, colored console output, timestamps, and file logging.

The project is being developed as part of the **DLF (Dexoron Logging Framework)** family, with plans for implementations in other programming languages.

GitLab repository: https://gitlab.com/dexoron/dlf4p
PyPi project: https://pypi.org/project/dlf4p

---

## Features

* Log levels: `DEBUG`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `FATAL`
* Colored console output
* Timestamp support
* Prefix support (e.g., module or component name)
* File logging
* Simple configuration via `setup()`
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

dlf.setup(time=True, color=True, simple=False, file_logging=True)

dlf.info("Application started", "Main")
dlf.success("Server successfully started", "Server")
dlf.warning("Slow response", "API")
dlf.error("Database connection error", "Database")
dlf.fatal("Critical error", "System")
```

Console output:

```log
[12:30:10] [Main/INFO]: Application started
[12:30:11] [Server/SUCCESS]: Server successfully started
[12:30:12] [API/WARNING]: Slow response
[12:30:13] [Database/ERROR]: Database connection error
[12:30:14] [System/FATAL]: Critical error
```

Logger class example:

```python
import dlf4p as dlf

dlf.setup(time=True, color=True, simple=False, file_logging=True)

log = dlf.Logger("Main")
log.info("Application started")

log = dlf.Logger("Core")
log.setLevel(2)  # SUCCESS and higher
log.info("Core module initialized")
log.success("Submodule loaded successfully")
log.warning("Disabled System modules")
```

Console output:

```log
[12:30:10] [Main/INFO]: Application started
[12:30:11] [Core/SUCCESS]: Submodule loaded successfully
[12:30:12] [Core/WARNING]: Disabled System modules
```

> Logs are saved to a file without ANSI color codes.

---

## Configuration

The `setup()` function is used to configure the logger:

```python
dlf.setup(
    time=True,        # show timestamp
    color=True,       # enable colored output
    simple=False,     # simplified log format (without prefixes)
    file_logging=True # enable file logging
)
```

### Parameters:

* `time` — enable or disable timestamps
* `color` — enable or disable colors
* `simple` — disable prefixes
* `file_logging` — enable writing logs to a file

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
