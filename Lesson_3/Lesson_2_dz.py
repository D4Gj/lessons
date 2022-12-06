import datetime

age = int(input())

print(f'Ваш год рождения - {datetime.datetime.today().year - age}')  # можно и просто 2022
