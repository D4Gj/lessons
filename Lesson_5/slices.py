# python slices (срезы)
s = 'abcdefghi'
for i in range(len(s)):
    print(i, end='\t')
print()
for char in s:
    print(char, end='\t')
print()
for i in range(len(s), 0, -1):
    print(-i, end='\t')
print()
# переменная[старт = 0:стоп = длине объекта:шаг = 1]
# print(s[:])
# print(s[:3])
# print(s[3:])
# print(s[3:5])
# print()
# print(s[-9:-5])
# print(s[:-3])
# print(s[-3:])
# print(s[-3:-5])
# print() # шаг
# print(s[3::2])
# print(s[::2])
# print(s[1::2])
# print(s[2:7:2])
# print(s[::-1]) # переворот
# print(s[::-2])
# print(s[::-1][::2])
# print(s[2:5][::-1])
# print(s[-3:-5:-1])
print(s[3::2][::-1])  # hfd
