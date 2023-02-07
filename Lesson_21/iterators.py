# __next__
# StopIteration
a = '[1]'
iterator = iter(a)
print(next(iterator))
print(next(iterator))
print(next(iterator))

my_tuple = ('milk', 'honey', 'house')
for val in my_tuple:
    print(val)
iterator2 = iter(my_tuple)
for val in iterator2:
    print(val)
# print(next(iterator2))
# print(next(iterator2))
# print(next(iterator2))

