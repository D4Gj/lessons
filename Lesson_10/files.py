# login = input()
# password = input()

file = open('1.txt')
# r - read
# w - write
# r+ - read and write
# w+ - read and write. создаст новый если не найдёт
# a - append - добавить в конец
# a+ - read and append
print(file)
print(file.read())
file.close()

file = open('1.txt', 'r')  # open('1.txt')
print(file)
print(file.read())
file.close()

file = open('dela1111.txt', 'w')
file.write('123')
file.close()
file = open('dela.txt')
print(file.read())
file.close()