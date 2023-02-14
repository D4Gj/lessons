from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper


@decor
def func(a, b):
    """Сумма двух чисел"""
    return a + b


print(func(1, 5))
print(func.__name__)
print(func.__doc__)
