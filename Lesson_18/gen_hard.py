# [выражение for элемент in последовательность if условие]
#      3            1                               2
list1 = [i for i in range(1, 101) if i % 2 == 0 and i ** 2 >= 100]
print(list1)
list_test = []
for j in [1, 2, 3]:
    if j != 2:
        for i in range(1, 10):
            if i % 2 == 0:
                list_test.append(i * j)

list2 = [i * j for i in range(1, 10) if i % 2 == 0
         for j in [1, 2, 3] if j != 2]

print(list2)
print(list_test)
