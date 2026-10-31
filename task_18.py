import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            vremya = datetime.datetime.now()
            f = open(filename, "a")
            f.write(f"{vremya} - {func.__name__} - args: {args}, kwargs: {kwargs}\n")
            f.close()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("log.txt")
def test(a, b):
    return a + b

print(f"Результат функции: {test(2, 3)}")