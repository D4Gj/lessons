helo = "hello"

for char in helo:
    print(char, 'буква из слова')

print(*range(10))
print(*range(5, 10))
print(*range(5, 10, 2))
print(*range(10, 2))
print(*range(10, 2, -1))
print(*range(-10, 10, 2))
print(*range(0, 10, 2))

for i in range(10):
    print('Привет')

# for i in range(5):
#     num = int(input())
#     print(num * num)

for i in range(10):
    print(i)

for _ in range(5):
    print('Python')

for i in range(7):
    print('Дед мороз выходи')

print('Дед мороз выходи\n' * 7)

# b = input()
#
# for char in b:
#     print(char, 'буква слова', b)

for i in range(11):
    print(f'{i}*7={i * 7}')

# number = int(input())
# for i in range(10):
#     print(f'{i}*{number}={i * number}')

bought = [1, 2, 3, 4, 5]

for tovar in bought:
    print(tovar, 'куплен')

for i in range(5):
    for j in range(5):
        print((i, j), end='')
    print()
