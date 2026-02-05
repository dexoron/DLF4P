# dlf-py — Dexoron Logging Framework for Python

`dlf-py` is a lightweight and convenient logger for Python inspired by **SLF4J**.
It provides a simple API for logging messages with support for log levels, colored console output, timestamps, and file logging.

The project is being developed as part of the **DLF (Dexoron Logging Framework)** family, with plans for implementations in other programming languages.

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
pip install dlf-py
```

---

## Quick Start

```python
import dlf

dlf.setup(time=True, color=True, simple=False, file_logging=True)

dlf.info("Application started", "Main")
dlf.success("Server successfully started", "Server")
dlf.warning("Slow response", "API")
dlf.error("Database connection error", "Database")
dlf.fatal("Critical error", "System")
```

Example console output:

```
[12:30:10] [Main/INFO]: Application started
[12:30:11] [Server/SUCCESS]: Server successfully started
[12:30:12] [API/WARNING]: Slow response
[12:30:13] [Database/ERROR]: Database connection error
[12:30:14] [System/FATAL]: Critical error
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

## Philosophy

`dlf-py` is inspired by **SLF4J (Simple Logging Facade for Java)** and aims to:

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

> dlf-py — a simple logger today, a full logging framework tomorrow.