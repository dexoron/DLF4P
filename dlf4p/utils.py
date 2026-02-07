from datetime import datetime

VERSION = "1.2.1"

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
reset = "\033[0m"
bold_red = "\033[1;31m"

useTime = True
useColor = True
simpleLog = False
def logFile(msg):
    return None

def get_time():
    return datetime.now().strftime("%H:%M:%S")
def get_data():
    return datetime.now().strftime("%d.%m.%Y")

levels = ["DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "FATAL", "EXCEPTION"]
logLevel = 0