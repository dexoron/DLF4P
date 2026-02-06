import dlf4p

dlf4p.setup(time=True, color=True, simple=False, file_logging=True)

dlf = dlf4p.Logger("Main")

dlf.info("Test info message")
dlf.success("Test success message")
dlf.warning("Test warning message")
dlf.error("Test error message")
dlf.debug("Test debug message")

dlf = dlf4p.Logger("Core")
dlf.setLevel(2)
dlf.info("Test info message")
dlf.success("Test success message")
dlf.warning("Test warning message")
dlf.error("Test error message")
dlf.debug("Test debug message")
