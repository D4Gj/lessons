# file = open('dela.txt')
with open('dela.txt',) as file:
    print(file.read())

# with open('dela.txt',) as file:
#     print(file.read(5))
#     print(file.read(2))
#     print(file.read(5))
#     print(file.read(5))
#     print(file.read(5))
#     print(file.read(5))

with open('dela.txt') as fb:
    print(fb.readline())
    print(fb.readline())
    print(fb.tell())
    print(fb.readlines(2))

with open('dela.txt') as fb:
    print(fb.readlines())

