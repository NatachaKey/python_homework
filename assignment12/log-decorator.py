import logging
# One-time logger setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))
# Task 1 — logger_decorator definition
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper
# Task 1 — Function 1: no parameters, no return
@logger_decorator
def say_hello():
    print("Hello, World!")
# Task 1 — Function 2: variable positional arguments
@logger_decorator
def always_true(*args):
    return True
# Task 1 — Function 3: variable keyword arguments
@logger_decorator
def keyword_args_only(**kwargs):
    return logger_decorator
# Task 1 — Mainline calls
if __name__ == "__main__":
    say_hello()
    always_true(1, 2, 3, 4)
    keyword_args_only(name="Alice", age=30)