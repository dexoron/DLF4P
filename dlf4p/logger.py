import traceback
from .utils import (
    red,
    green,
    yellow,
    reset,
    bold_red,
    useTime,
    useColor,
    simpleLog,
    logFile,
    get_time,
    get_data,
    levels,
    logLevel,
)

LOG_FILENAME = None

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
""")

def setup(time: bool=True, color: bool=True, simple: bool=False, file_logging: bool=True):
    global useTime, useColor, simpleLog, logFile, LOG_FILENAME
    useTime = time
    useColor = color
    simpleLog = simple
    if file_logging:
        LOG_FILENAME = f"logger-{get_data()}-{get_time()}.log"
        def logFile(msg):
            with open(LOG_FILENAME, "a") as log_handle:
                log_handle.write(msg + "\n")
    else:
        def logFile(msg):
            return None

def _print(level: int, prefix: str, content: str, color: str=None, exc: Exception=None):
    base_msg = ""

    if useTime:
        base_msg += f"[{get_time()}] "

    if simpleLog or not prefix:
        base_msg += f"[{level}]"
    else:
        base_msg += f"[{prefix}/{level}]"

    base_msg += f": {str(content)}"

    if useColor and color:
        console_msg = f"{color}{base_msg}{reset}"
    else:
        console_msg = base_msg

    print(console_msg)
    logFile(base_msg)

    if exc is not None:
        base_tb = traceback.format_exc()[:-1]
        console_tb = red
        console_tb += base_tb
        console_tb += reset
        print(console_tb)
        logFile(base_tb)

class Logger:
    def __init__(self, prefix: str=None):
        self.prefix = prefix

    def getLogger(self, prefix: str):
        return Logger(prefix)
    
    def setLevel(self, level: int):
        global logLevel
        logLevel = level
        _print("INFO", self.prefix, f"Log level set to {levels[level]}")

    def debug(self, content: str):
        if logLevel <= 0:
            _print("DEBUG", self.prefix, content)
        
    def info(self, content: str):
        if logLevel <= 1:
            _print("INFO", self.prefix, content)

    def success(self, content: str):
        if logLevel <= 2:
            _print("SUCCESS", self.prefix, content, green)

    def warning(self, content: str):
        if logLevel <= 3:
            _print("WARNING", self.prefix, content, yellow)

    def error(self, content: str, exc: Exception=None):
        if logLevel <= 4:
            _print("ERROR", self.prefix, content, red, exc=exc)

    def fatal(self, content: str, exc: Exception=None):
        if logLevel <= 5:
            _print("FATAL", self.prefix, content, bold_red, exc=exc)
    
    def exception(self, content: str, exc: Exception=None):
        _print("EXCEPTION", self.prefix, content, red, exc=exc)



def debug(content: str, prefix: str=None):
    _print("DEBUG", prefix, content)

def info(content: str, prefix: str=None):
    _print("INFO", prefix, content)

def success(content: str, prefix: str=None):
    _print("SUCCESS", prefix, content, green)

def warning(content: str, prefix: str=None):
    _print("WARNING", prefix, content, yellow)

def error(content: str, prefix: str=None, exc: Exception=None):
    _print("ERROR", prefix, content, red, exc=exc)

def fatal(content: str, prefix: str=None, exc: Exception=None):
    _print("FATAL", prefix, content, bold_red, exc=exc)

def exception(content: str, prefix: str=None, exc: Exception=None):
    _print("EXCEPTION", prefix, content, red, exc=exc)