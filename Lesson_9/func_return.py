def func():
    x = 5
    return x


number = func()
print(number)

print(func())


def func2():
    x = 5
    y = 15
    z = 0
    return x, y, z


print(list(func2()))
print(*func2())
a, b, c = func2()
print(a, c)


def func3():
    print("hello")
    return 'end'
    print('world')


print(func3())


def func4(x, c=10):
    return x + c, x, c


print(func4(50))
