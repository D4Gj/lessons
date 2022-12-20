def excercise_1(b, a=0, ):
    summa = 0
    for i in range(a, b):
        if i % 3 == 0 or i % 5 == 0:
            summa += i
    print(summa)


excercise_1(5000, -100)
excercise_1(a=-100, b=5000)
"""
Написать функцию, которая принимает стороны прямоугольника, а затем 
выводит периметр и площадь
"""