number = input()

if number == number[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')

print('Палиндром' if number == number[::-1] else 'Не палиндром')

##
number_length = len(number)
number = int(number)
while number != 0:
    last_num = number % 10
    first_num = number // 10 % 10
    number //= 10
    if last_num == first_num and number < 10:
        print('Палиндром')
