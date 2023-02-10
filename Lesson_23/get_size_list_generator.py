import sys
import time
import datetime


def get_size(func):
    def wrapper(*args, **kwargs):
        print(f'Функция запущена в {datetime.datetime.now()}')
        result = sys.getsizeof(func(*args, **kwargs))
        print(f'>> функция {func.__name__} занимает в памяти {result} байт')

    return wrapper


@get_size
def add_with_delay(n):
    return [1 for i in range(n)]


add_with_delay(1000000000)
