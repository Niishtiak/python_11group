def type_check(*tipy):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(args)):
                if not isinstance(args[i], tipy[i]):
                    raise TypeError("Неверный тип аргумента")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(f"Результат: {add(5, 10)}")