def func():
    print('я выполнился')


def func2(func1):
    def func3():
        print(125)
    func1()
    return 0


print(func2(func))
