person_1_name = "Vasya"
person_1_login = "asd"
# 1-x 2-y 3-r
circle = [-2, 3, 10]


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


circle_oop = Circle(-2, 3, 10)
print(circle_oop.r * 2)
print(circle[2] * 2)
# person = Person('Vasya', 'asd')
# person.
