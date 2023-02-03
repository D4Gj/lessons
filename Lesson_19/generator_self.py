# yield

def func(num):
    while num > 0:
        yield num
        num -= 1


def bad_func():
    yield 22
    return 33312312


b = bad_func()
print(next(b))
print(next(b))
for i in bad_func():
    print(i)
a = func(5)
print(a)
print(a)
print(a)
print(a)
# print(next(a))
# print(a.__next__())
# print(a.__next__())
print(sum(func(3)))
print(min(func(3)))
# for number in a:
#     print(number)
