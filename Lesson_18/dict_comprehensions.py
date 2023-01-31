# {key:value}
from pprint import pprint

dict1 = {x: x ** 2 + 1 for x in range(5)}
print(dict1)
print(type(dict1))

dict_bad = {x: y for x in 'ABC' for y in 'XYZ'}
dict_bad = {x: 'Z' for x in 'ABC'}
dict_bad = {}.fromkeys('ABC', 'Z')
dict2 = {x: y for x, y in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]}
print(dict_bad)
print(dict2.items())
b = ['a', 'b', 'c']
print(list(enumerate(b)))
# dict_empt = {}.fromkeys(*enumerate(b))
# print(dict_empt)
dict_list = {x: [y for y in range(x, x + 3)] for x in range(5)}
print(dict_list)

dict_list_str = {x: [y % 2 for y in range(10)] for x in 'ABC'}
dict_list2 = {'ABCDE'[i]: [i % 2] * 5 for i in range(5)}
print(dict_list_str)
print(dict_list2)
dict_dict = {x: {y: x for y in 'XYZ'} for x in 'ABC'}
pprint(dict_dict)
dict_hard = {x: {y: [z for z in range(z, z + 2)] for y in 'XYZ'} for x, z in zip('ABC', range(3))}
pprint(dict_hard)

dict_if = {x: {y: 3 for y in 'ABCD' if y != x} for x in 'ABCD'}
pprint(dict_if)
dict_if_else = {x: 1 if x in 'ACE' else 0 for x in 'ABCDEF'}
pprint(dict_if_else)

