def func(num):
    while num > 0:
        yield num
        num -= 1


a = func(5)
for num in a:
    if num == 2:
        break
    print(num)
print(next(a))


