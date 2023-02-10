def decorator(func):
    '''Основная функция'''
    print('Декоратор 1')

    def wrapper():
        func()
        print('Перед функцией 1')

    return wrapper


def decorator2(func):
    print('декоратор 2')

    def wrapper():
        print('Перед функцией 2')
        func()

    return wrapper


@decorator
@decorator2
def wrapped():
    print('---Функция с декоратором')


@decorator2
def a():
    pass


@decorator2
def b():
    pass


print('-Start')
wrapped()
print('-End')
# print(a())
