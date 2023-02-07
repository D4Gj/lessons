def gen1(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1


def gen2(start):
    n = start
    while n > 0:
        yield n
        n -= 1


# def func(n):
#     yield from gen1(n)
#     yield from gen2(n)
def func(n):
    for x in gen1(n):
        yield x
    for x in gen2(n):
        yield x


for i in func(5):
    print(i)
