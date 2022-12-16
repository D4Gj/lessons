a = [1, 2, 3, 'a', True, 123]
b = '1231asdf24'
# Индексируемость
# Изменяемый
# Итерируемый
for i in a:
    print(i, end=' ')

for i in range(len(a)):
    print(a[i])


print(*a)
print(*b)
