important_info = ['123',
                  '123',
                  '123',
                  'number // 10 % 10',
                  'asdfmsd']

print(important_info[0] == '123')
print(important_info[0])
print(important_info[1])
print(important_info[2])
print(important_info[3])
print(important_info[4])

different_values = [1, 1.0, range(10), [], True, '123']
print(different_values)
print(*different_values)  # распаковка
print(len(different_values))  # длина списка

mylist = []
mylist = list()

print(list('1232'))
print(list(range(5)))
print(list(range(0, 10, 2)))
print(list(range(1, 10, 2)))

for info in important_info:
    print(info)

for i in range(1, len(important_info), 2):
    print(i, important_info[i])

for i in range(0, len(important_info), 2):
    print(i, important_info[i])

print(important_info * 5)
print(min([1, 2, 3, 4, 5]))
numb = [1, 2, 3]

for i in range(len(numb)):
    numb[i] = numb[i] * 100
print(numb)
