# Написать родительский класс человека и дочерний класс ученика

class Human:
    """
    Этот класс олицетворяет человека
    """

    def __init__(self, name, lname, age):
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


class Teacher(Human):
    def __init__(self, name, lname, age, lesson):
        super().__init__(name, lname, age)
        self.lesson = lesson

    def teaching(self):
        print(f'Я веду - {self.lesson}')


class Director(Teacher, Human):
    def say(self):
        print('Я - директор')


stud = Student('Vasya', 'Pupkin', 16, 9)
stud.say_name()

eng_teacher = Teacher('Vasya', 'Pupkin', 40, 'английский язык')
eng_teacher.teaching()

school_director = Director('Vasya', 'Pupkin', 45, 'немецкий язык')
school_director.teaching()
school_director.say()
