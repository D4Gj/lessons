def func():
    while True:
        n = yield
        print(n)


# GeneratorExit
r = func()
r.send(None)
r.send(1)

r.throw(RuntimeError, 'Ошибка')
r.send(1.0)
print(r.close())
r.send(10)
r.send(10)
