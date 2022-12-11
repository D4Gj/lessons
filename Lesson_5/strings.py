a = 'hello'
for char in a:
    print(char, end=' ')

print()
i = 0
while i < len(a):
    print(a[i])
    i += 1

# конкатенация
print('a' + 'b')
print('10' + '20' * 10)
print(len(a))

word = 'pencil'
sub_word = 'nc'
if sub_word in word:
    print(sub_word, 'есть в word')

s = 'Python'
print(s[-1])
print(s[-2])
print(s[-6])
# ошибки т.к. нету столько символов
# print(s[-7])
print(s[-0])  # так можно
# print(s[100])
# print(s[6])

stroka = 'abcdefghi'
# print(s[0] * 2 + s[2] * 2 + s[4] * 3 + s[6] * 2)
# aceg
# aa cc eee gg
# "Vasya"
#  01234
name = "Vasya"

for j in range(len(name)):
    print(name[j], end=' ')
print()
for j in range(0, len(name), 3):
    print(name[j], end=' ')
print()




