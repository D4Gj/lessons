# a = int(input())
# b = int(input())
# try:
#     print(a / b)
# except Exception as e:
#     print(e)

# try:
#     print(a / b)
# except ZeroDivisionError as e:
#     print(e)
#

try:
    a = int(input())
    b = int(input())
    print(a / b)
except:
    print('Что-то пошло не так :(')

try:
    a = int(input())
    b = int(input())
    print(a / b)
except (BaseException,Exception) as e:
    print('Что-то пошло не так :(')
else:
    print(1231231)
finally:
    print('Это всегда работает')

