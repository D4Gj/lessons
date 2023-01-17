class Person:
    _age = 15

    def __say_hello():
        print('Привет')


pers1 = Person
print(pers1._age)
pers1._age = 16
print(pers1._age)
# pers1.__say_hello()
pers1._Person__say_hello()

