a = tuple()
b = ()
c = (1,)
print(type(a), type(b), type(c))

nums = (1, 2)
a = list(nums)
a.append(100)
a = tuple(a)
print(a, type(a), )