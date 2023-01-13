# Написать родительский класс человека и дочерний класс ученика

class Human:
    """
    Этот класс олицетворяет человека
    """

    def __init__(self, name: list, lname, age):
        """
        name:str
        """
        self.name = name
        self.lname = lname
        self.age = age

    def say_name(self):
        print(f'Привет, я - {self.name} {self.lname}')

    def say_age(self):
        print(f'Мой возраст - {self.age}')


class Student(Human):
    def __init__(self, name, lname, age, class_num):
        super().__init__(name, lname, age)
        self.class_num = class_num

    def say_class_num(self):
        print(f'Я обучаюсь в {self.class_num} классе')


student = Student('Vasya', 'Pupkin', 15, 8)
student.say_name()
st2 = Student(123, 2, 3, 5)
print(st2.name)

student.say_class_num()
print(1, )

# Человек => учитель =>