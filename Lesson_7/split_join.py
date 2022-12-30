languages = 'Python C# Java'.split()
print(languages)
numbers = '1.txt 2 3 4 5'.split()
print(numbers)
# numbers2 = input().split()  # int(input())
# print(numbers2)
# ip = input().split('.')
# print(ip)

languages2 = ' '.join(languages)
print(languages2)
ip = '.'.join(['192', '168', '0', '1.txt'])
print(ip)
# Программа, которая запрашивает на ввод имя и класс(в одну строку через пробел)
# Нужно вывести класс
# Василий 8А
# 8А
pupil = input().split()
print(pupil)
print(pupil[1])
# Есть список слов, необходимо составить из него строку через цикл
# и join
a = ['Hello','world']
b = '_'.join(a)
c = ''
for word in a:
    c += word
    c += '_'
print(c)
print(b)
