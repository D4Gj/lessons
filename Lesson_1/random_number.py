import random

secret_number = random.randint(1, 10)
attempts = 3
print('Это программа угадай число. У вас 3 попытки')

while attempts > 0:
    print('Попыток ' + str(attempts))
    attempts = attempts - 1
    user_number = input('Число: ')
    user_number = int(user_number)
    if user_number > secret_number:
        print('Загаданное число меньше')
    if user_number < secret_number:
        print('Загаданное число больше')
    if user_number == secret_number:
        print('Победа')
        break
    if attempts == 0:
        print('Вы проиграли')
