for i in range(1, 101):
    if i == 3 or i == 20 or i % 3 == 0:
        continue
    print(i)

for i in range(1, 101):
    if i != 3 and i != 20 and i % 3 != 0:
        print(i)
    if i == 15:
        break
else:
    print("Цикл кончился")

a = 1
while a < 5:
    print('верно')
    a += 1
else:
    print('неверно')
