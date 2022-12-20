"""Написать функцию, которая принимает стороны прямоугольника, а затем
выводит периметр и площадь"""


def triangle(i, j, n):
    for i in range(3):
        for j in range(3):
            for n in range(3):
                print('*', end='')
    print(0.5 * i * n)
    print(i * j)


def calculate_perimeter_square(side1, side2):
    square = side1 * side2
    perimetr = 2 * (side1 + side2)
    print(f'Площадь - {square}')
    print(f'Периметр - {perimetr}')


#
# a, b = map(int, input().split())
# print(a * b, 2 * (a + b))

triangle(5, 5, 5)

calculate_perimeter_square(10, 5)
