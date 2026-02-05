from datetime import datetime

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
reset = "\033[0m"
bold_red = "\033[1;31m"

useTime = True
useColor = True
simpleLog = False
LOG_FILENAME = None
def logFile(msg):
    return None

def get_time():
    return datetime.now().strftime("%H:%M:%S")
def get_data():
    return datetime.now().strftime("%d.%m.%Y")

def setup(time=True, color=True, simple=False, file_logging=False):
    global useTime, useColor, simpleLog, logFile
    useTime = time
    useColor = color
    simpleLog = simple
    if file_logging:
        LOG_FILENAME = f"logger-{get_data()}-{get_time()}.log"
        def logFile(msg):
            return open(LOG_FILENAME, "a").write(msg + "\n")
    else:
        def logFile(msg):
            return None

def _print(level, prefix, content, color=None):
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


def debug(content, prefix=None):
    _print("DEBUG", prefix, content)

def info(content, prefix=None):
    _print("INFO", prefix, content)

def success(content, prefix=None):
    _print("SUCCESS", prefix, content, green)

def warning(content, prefix=None):
    _print("WARNING", prefix, content, yellow)

def error(content, prefix=None):
    _print("ERROR", prefix, content, red)

def fatal(content, prefix=None):
    _print("FATAL", prefix, content, bold_red)