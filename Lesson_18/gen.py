# generator

# print(range(1, 10))
# Если это запустить, то компьютер зависнет :)
# numbers = list(range(1000000000))
# for i in numbers:
#     print(i)

# for i in range(1000000000):
#     print(i)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(1, 11):
    b.append(i)
print(b)

list1 = [i for i in range(1, 11)]
# [выражение for элемент in последовательность]
print([i ** 2 for i in list1])
list_strs = [str(i) for i in b]
print(list_strs)
# list2 = map(int, input().split())
list2 = [int(number) for number in input().split('-')]
print(list2,sep=' ')