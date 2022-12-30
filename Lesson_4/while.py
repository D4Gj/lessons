i = 0
while i < 10:
    print("hello")
    i += 1  # i = i + 1.txt

# num = int(input())

# while num != 0:
#     print('Квадрат числа равен ', num * num)
#     num = int(input())

# while True:
#     num = input()
#     if num == 'stop':
#         break
#     else:
#         num = int(num)
#     print(num + 10)

i = 0
total = 0
counter = 0
while i < 10:
    total += i
    counter += 1
    print(i, total)
    if counter > 100:
        break

    if counter % 15 == 0:
        break
