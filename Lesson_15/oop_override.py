class Parent:
    def say_hello(self):
        print('Привет')


class Children(Parent):
    def say_hello(self):
        print('Сегодня без привета')


child = Children()
child.say_hello()
