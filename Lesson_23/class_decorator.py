class Decorator:
    def __init__(self, func):
        print('> Decorators init ')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('> перед вызовом', self.func.__name__)
        self.func()
        print('> после вызова класса')


@Decorator
def wrapped():
    print('Функция wrapped')


print('>> start')
wrapped()
print('>> end')
