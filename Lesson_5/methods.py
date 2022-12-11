# имя_объекта.имя_метода(параметры)
s = '\'Hello\' my name is Vasya'
print(s.count('a'))
print(s.count(' '))
print(s.count("'"))
print(s.count('\''))
# Литералы (используйте гугл и гуглите)
# \t - знак таба
# \n - переход на новую строку
print(s.replace(' ', '-'))
print(s.replace('hello', '-'))
print(s.startswith('H'))
print(s.startswith('\'H'))
print(s.endswith('Vasya'))
print(s.endswith('Petya'))
print(s.rfind('\'Hello'))

# names = input().split()
print(s.split('a'))

s2 = '    hello   123 4243 '
print(s2.strip())
s3 = '  \t\f'
s4 = '123H'

if s4.isdigit() or s4.isalnum():
    print(s4)
if s3.isspace():
    print('Состоит')
