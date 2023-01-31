set1 = {i ** 2 % 4 for i in range(10)}
list1 = [i ** 2 % 4 for i in range(10)]
print(set1, list1)

set2 = {i for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if 'a' not in i}
print(set2)

set_if_else = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:]
               for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2']}
print(set_if_else)
set_if_if_else = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:]
                  for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if i[1] == 'c'}
print(set_if_if_else)
