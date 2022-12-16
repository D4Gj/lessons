# humans = { ключ: значение }
a = {}  # dict()
print(a)
print(type(a))
b = {'a': 1, 'b': 2}
print(b)
print(type(b))

c = dict([(1, 2), [4, 5]])
print(c)

a = {'a': 1}
a['b'] = 4
a['a'] = 10
print(a)

# a.clear()
# print(a)

b = a.copy()
c = a
# a['a'] = 100
print(a, b)
print(c is a)
print(b is a)

# c = {[(1, 2), [4, 5]]}
print(c)

d = {'a': 112312312, 'b': 2}

print(d.get('c', 'Не найдено значение'))
print(d.get('a', 'Не найдено значение'))

print(d.items())
print(d.keys())
print(d.values())

# print(d.pop('b'))
# print(d.popitem())
print(d)
d.setdefault('c')
print(d)

d.update({'d': 123, 'e': 32})
print(d)

