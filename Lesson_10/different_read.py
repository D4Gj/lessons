filename = 'dela.txt'

# 1.txt Чтение в одну строку
with open(filename, encoding='utf-8') as file:
    data = file.read()
    print(data)

# 2 Чтение в список
with open(filename, encoding='utf-8') as file:
    data = file.readlines()
    print(data)

# 3 Построчное чтение
with open(filename, encoding='utf-8') as file:
    for line in file:
        print(line.strip())