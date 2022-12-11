"""
Пользователь вводит email в формате example@mail.ru вырезать домен, доменом будем считать все что находится после @, (mail.ru)
Если @ нет то вывести что email введен неверно
"""
email = input()

if '@' in email:
    domen = email[email.index("@") + 1:]
    print(domen)
else:
    print('no domen')
