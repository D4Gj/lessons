# Декоратор позволяет изменить поведение функции, не изменяя её код

def decorator(func):
    def wrapper():
        print('функция оболочка')
        func()

    return wrapper


def basic():
    print('Это основная функция')


wrapped = decorator(basic)
print('Start')
basic()
wrapped()
print('End')
