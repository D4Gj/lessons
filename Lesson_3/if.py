# if <условие>:
#    if <условие>:
#       блок кода
# ctrl+alt+l
# if <условие>:
#   блок кода
# #
# user_number = int(input('Число'))
#
# print('Моё число ' + str(user_number))
#
# if user_number % 2 == 0:
#     print('Число чётное')
# if user_number % 2 == 1:
#     print('Число нечётное')
#
# if user_number % 2 != 1:
#     print('Число чётное')
x = 0
if x > 2:
    if x < 10:
        print('х больше 2,но меньше 10')

if x > 2 and x < 10:
    print('х больше 2,но меньше 10')

if x == 5 and not (x > 2 + 10 or x < 10):
    print('х либо больше 2,либо меньше 10')

print(not True)
print(not False)
print(not not not not 100)
if 5 == 5 and 1000000000000000000000000000000000 == x ** 10000 \
        and 5 == 5:
    print('\'Vasya\'')
"""
Написать программу которая запрашивает 
на ввод температуру тела человека и 
выводит здоров или болен человек
Человека будем считать здоровым если 
его t лежит в диапазоне от 36 до 37, 
в остальных случаях программа должна вывести сообщение вы больны
"""

if x % 2 == 0:
    print('Начинается проверка числа')
    if x > 0:
        print(x, 'х больше 0 и является чётным')
        # print('123') - так нельзя...
        if x == 100:
            print('Вы попали в сотку')
        else:
            print()
    elif x < 0:
        print()

if x > 0:
    print('х больше 0')
elif x == 0:
    print('x = 0')
elif x < 0:
    print('x < 0')
else:
    print('Как вы сюда попали?')
print()
if x >= 0:
    print('х больше 0')
if x == 0:
    print('x = 0')
if x <= 0:
    print('x < 0')

age = 20
if age >= 14 < 18:
    print('shkola')
elif age >= 18:
    print('univer')

# Тернарный оператор
num = 15
print('Чётное' if num % 2 == 0 else 'Нечётное')
# Если условие верно Условие Иначе Если не верно
# 6 <= a <= 8
# a == 6 or a == 7 or a == 8
# 5 < a < 9
# a <= 8 and a >= 6
