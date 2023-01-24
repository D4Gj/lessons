class IntPrinter(int):
    def __init__(self, num) -> None:
        super().__init__()
        self.num = num

    def __add__(self, other):
        print('Произошло сложение')
        return self.num + other

    def __sub__(self, other):
        print('Произошло вычитание')
        return self.num - other

    def __mul__(self, other):
        print('Произошло умножение')
        return self.num * other

    def __truediv__(self, other):
        print('Произошло деление целочисленное')
        return self.num / other


a = Int_printer(10)
print(a / (a * 15 + 20))
