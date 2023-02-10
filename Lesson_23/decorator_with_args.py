def decorator_with_args(func):
    print('> декоратор с агрументами')

    def decorated(a, b):
        print('> перед вызовом', func.__name__)
        ret = func(a, b)
        print('> после вызова', func.__name__)
        return ret

    return decorated


@decorator_with_args
def add(a, b):
    print('func1')
    return a + b


@decorator_with_args
def sub(a, b):
    print('func2')
    return a - b


print('>> start')
r = add(10, 5)
print('r:', r)
m = sub(10, 5)
print('m:', m)
print('>> end')
