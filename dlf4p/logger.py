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

def _print(level: int, prefix: str, content: str, color: str=None):
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

    def error(self, content: str):
        if logLevel <= 4:
            _print("ERROR", self.prefix, content, red)

    def fatal(self, content: str):
        if logLevel <= 5:
            _print("FATAL", self.prefix, content, bold_red)

def debug(content: str, prefix: str=None):
    _print("DEBUG", prefix, content)

def info(content: str, prefix: str=None):
    _print("INFO", prefix, content)

def success(content: str, prefix: str=None):
    _print("SUCCESS", prefix, content, green)

def warning(content: str, prefix: str=None):
    _print("WARNING", prefix, content, yellow)

def error(content: str, prefix: str=None):
    _print("ERROR", prefix, content, red)

def fatal(content: str, prefix: str=None):
    _print("FATAL", prefix, content, bold_red)
