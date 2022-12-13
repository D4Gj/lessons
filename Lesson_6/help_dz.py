a = [1, 3, 4, 6]  # 5
last = len(a) - 1
while last > 0:
    if a[last] % 2 == 0:
        del a[last]
    else:
        a[last] = a[last] // 2
    last -= 1
print(a)
a[5]
for val in a:
    print(val)
last = len(a) - 1
i = 0
while last >= i:
    if a[i] % 2 == 0:
        del a[i]
    i += 1
print(a)

# for i in range(last, -1, -1):
#     if a[i] % 3 == 0:
#         print(a[i])
