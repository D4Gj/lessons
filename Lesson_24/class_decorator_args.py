class Decorator:
    def __init__(self, name):
        print('> Decorators init with name', name)
        self.name = name

    def __call__(self, func):
        def wrapper(a, b):
            print('>>> перед вызовом', func.__name__)
            func(a,b)
            print('>>> после вызова класса')

        return wrapper


@Decorator('test')
def add(first_number, second_number):
    print('функция даёт результат', first_number + second_number)


print('>> start')
add(5, 5)
print('>> end')

# print('>> start')
# wrapped()
# print('>> end')
