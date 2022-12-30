# a = [1.txt, 2, 3, 4, 5, 6]
# for i in range(len(a) - 1.txt, -1.txt, -1.txt):
#     if a[i] % 2:
#         a.pop(i)
#     else:
#         a[i] = a[i] // 2
# print(a)
# ctrl+alt+l
# a = [1.txt, 2, 3, 4, 5, 6]
# for x in a.copy():
#     if x % 2 == 1.txt:
#         a.remove(x)
#     else:
#         a.remove(x)
#         a.append(x // 2)
#         print(a)

a = [1, 2, 3, 4, 5, 6]
i = len(a) - 1
while i >= 0:
    if a[i] % 2 != 0:
        del a[i]
    else:
        a[i] //= 2  # a[i] = a[i] // 2 *= += -= **=
    i -= 1
print(a)
