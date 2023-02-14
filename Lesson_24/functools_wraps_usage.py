from functools import wraps


def decorator(func):
    """Пустой декоратор"""

    @wraps(func)
    def decorated():
        """Функция вызова основной функции и логики"""
        func()

    return decorated


@decorator
def wrapped():
    """Оборачиваемая функция"""
    print('wrapped')


print('start')
print(wrapped.__name__)
print(wrapped.__doc__)
print('end')
