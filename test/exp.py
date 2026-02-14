# type: ignore
import dlf4p

dlf = dlf4p.Logger("Core")
try:
    value = int(input("Enter number: "))
    result = 100 / value
    dlf.info(f"Solver: {result}")
    dlf.info("Touch to file nonexistent.txt")
    file = open("nonexistent.txt")
except Exception as e:
    dlf.exception("Crash", exc=e)


try:
    a = 2
    b = "two"
    dlf.info(f"Add {a} and {b}")
    print(a + b)
except Exception as e:
    dlf.exception("Crash", exc=e)
