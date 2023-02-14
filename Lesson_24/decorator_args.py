def decorator_with_args(name):
    print('> decorator with args', name)

    def real_decorator(func):
        print('>> Сам декоратор')

        def decorated(*args, **kwargs):
            print('>>>перед функцией', func.__name__)
            ret = func(*args, **kwargs)
            print('>>>после функцией', func.__name__)
            return ret

        return decorated

    return real_decorator


@decorator_with_args('test')
def add(a, b):
    print('>>>> функция add')
    return a + b


print('старт программы')
r = add(10, 20)
print(r)
print('конец программы')
