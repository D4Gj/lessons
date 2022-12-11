print('Попробуй угадай слово по буква. Игра - угадай слово')
secret_word = 'машина'
attempts = 5
# len(a) - количество букв в a
user_chars = []  # list()

"""
1. Загадать слово 
2. Указать количество попыток
3. Вывести слово заменив буквы символами
4. Попросить пользователя ввести букву
5. Сравнить букву с буквами в загаданном слове
6. Если буквы нету, то отнять попытку, если пользователь угадал - открыть букву
7. Повторить пункты с 4 по 6 до победы или поражения
8. Реализовать проверку на победу и поражение
"""

for i in range(len(secret_word)):
    print('*', end='')  #
print()
while True:
    is_win = True
    print(f'Попыток {attempts}')
    user_char = input('Введите букву:').lower()
    if user_char not in user_chars:
        user_chars.append(user_char)

    for char in secret_word:
        if char in user_chars:
            print(char, end='')
        else:
            print('*', end='')
            is_win = False
    print()
    if user_char not in secret_word:
        attempts = attempts - 1  # attempts -= 1
    if attempts == 0:
        print('Вы проиграли. Загаданное слово ' + secret_word)
        break
    if is_win == True:
        print('Вы победили')
        break
