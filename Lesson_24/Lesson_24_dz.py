import datetime


def decor(func):
    def wrapper():
        print('Начало функции')
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print('Функция завершилась')
        print(f'Функция отработала за {end_time - start_time}')
    return wrapper

@decor
def func1():
    # Если хотите увидеть числа в выводе, а не нули
    # a = [i for i in range(100000)]
    print('Hello world!')


func1()