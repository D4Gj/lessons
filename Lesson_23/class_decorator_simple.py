class Decorator:
    def __init__(self, func):
        print('> Decorators init ')
        self.func = func

    def __call__(self, a, b):
        print('> перед вызовом', self.func.__name__)
        c = self.func(a,b)
        print('> после вызова класса')
        print(f'Полученные данные имеют тип {type(c)}')

        return c


# @Decorator
# def wrapped():
#     print('Функция wrapped')
@Decorator
def sub(a, b):
    print('func2')
    return a - b

print('>> start')
res = sub(10,5)
print(f'{res=}')
print('>> end')
