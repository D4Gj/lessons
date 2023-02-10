import sys
import time
import datetime

def get_size(func):
    def wrapper(a, b, delay=0):
        print(f'Функция запущена в {datetime.datetime.now()}')
        result = sys.getsizeof(func(a, b, delay))
        print(f'>> функция {func.__name__} занимает в памяти {result} байт')

    return wrapper


@get_size
def add_with_delay(a, b, delay=0):
    print('Умножь', a, b, delay)
    time.sleep(delay)
    return a * b


print('Старт программы')
add_with_delay(100000000000, 99999999,1)
add_with_delay(10, 20, 3)
print('Конец программы')
