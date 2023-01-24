from calc import *

class Calculator:
    def __init__(self):
        self.main()

    def main(self):
        print('Это калькулятор')
        while True:
            num1 = int(input())
            num2 = int(input())
            choice = int(input())
            match choice:
                case 0:
                    print('Press enter for exit')
                    input()
                    break
                case 1:
                    print(plus(num1,num2))
                case 2:
                    print(minus(num1,num2))
                case 3:
                    print(division(num1,num2))
                case 4:
                    print(umnozh(num1,num2))
                case _:
                    print('Неверный выбор')

obj = Calculator()