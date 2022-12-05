log, password = input().split()
print(f'Ваш {log} {password}')

month = int(input())

if month == 12 or month == 1 or month == 2:
    print('Зима')
elif 3 <= month <= 5:
    print('Весна')
elif 6 <= month <= 8:
    print('Лето')
elif 9 <= month <= 11:
    print('Осень')

a, b = map(int, input().split())
print(a * b, 2 * (a + b))

comp = 'компьютер'

print(comp + 'а')
print(comp + 'ов')
print(comp)
