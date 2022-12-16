a = {1, 'a', 3, 3, 2, 2, 3, 3}
print(a)

a.add(123)
print(a)

a.update((5, 6, 7))
print(a)

a.remove(7)
a.discard(7)
print(a)

b = ['abc', 'and', 'for', 'abc', 'fsdf', 'for', 'abc']
print(set(b))
print(a.pop())


