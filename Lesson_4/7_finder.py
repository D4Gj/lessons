n = int(input())
flag = False
while n != 0:
    last_digit = n % 10
    if last_digit == 7:
        flag = True
        break
    n //= 10

if flag:  # также можно flag == True
    print('Содержит 7')
