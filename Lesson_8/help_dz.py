def plus(a, b):
    print('Сумма:', a + b)


def minus(a, b):
    pass


def raznost(a, b):
    pass


def umnozh(a, b):
    pass


while True:
    print("""=================
0 - выйти из калькулятор
1.txt - Сумма
2 - Разность
3 - Деление
4 - Умножение
=================""")
    number = int(input())
    if number == 0:
        break
    else:
        a, b = map(int, input("Введите два значения\n").split())
        if number == 1:
            plus(a, b)
