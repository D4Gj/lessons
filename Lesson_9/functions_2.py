x = 15


def func():
    global x
    x += 1


print(x)


def f():
    b = 15

    def e():
        global b
        b += 1
        ff = 11


func()
print(x)
# print(c)
