def plus(num1: float, num2: float) -> float:
    return num1 + num2


def minus(num1: float, num2: float) -> float:
    return num1 - num2


def division(num1: float, num2: float) -> float:
    if num2 != 0:
        return num1 / num2
    else:
        print("Деление на ноль!")


def mul(num1: float, num2: float) -> float:
    return num1 * num2


# kite ai
if __name__ == '__main__':
    print(__name__)
    print('Ура я самостоятельная програма')
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        print('error')
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % plus(x, y))
        elif s == '-':
            print("%.2f" % minus(x, y))
        elif s == '*':
            print("%.2f" % mul(x, y))
        elif s == '/':
            print("%.2f" % division(x, y))
    else:
        print("Неверный знак")
