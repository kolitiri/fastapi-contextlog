from my_app import clogger


def another_func():
    clogger.info(f"Hello from {another_func.__name__}")
