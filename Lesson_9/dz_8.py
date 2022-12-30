def plus(a, b):
    print('Сумма:', a + b)


def minus(a, b):
    print(a - b)


def division(a, b):
    print(a / b)


def umnozh(a, b):
    print(a * b)


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
        if number == 2:
            minus(a, b)
        if number == 3:
            division(a, b)
        if number == 4:
            umnozh(a, b)

