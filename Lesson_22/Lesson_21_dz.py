# Выражение генератор в куб числа от 1 до 10 включительно
# Вывести в виде списка
n = (i ** 3 for i in range(1, 11))

print(n)
print(list(n))


def get_n():
    i = 1
    while i <= 10:
        yield i ** 3
        i += 1


print(list(get_n()))
