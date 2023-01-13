class Transport:
    def __init__(self, speed, color='white'):
        self.speed = speed
        self.color = color
        print('Вызвался родительский метод')

    def beep(self):
        print('beep')


class Car(Transport):

    def __init__(self, speed, owner, color):
        super().__init__(speed, color)
        self.owner = owner

    def say_owner(self):
        print(f'Владелец - {self.owner}')

    def beep(self):
        print(f'Машина очень громко бибкает')

    def max_speed(self, new_speed):
        """Присвоение максимальной скорости"""
        if new_speed > self.speed:
            self.speed = new_speed
            print('Скорость успешно присвоена')
        else:
            print('Скорость уже больше')


class SportCar(Car, Transport):
    pass

    def wroom(self):
        print('wroom wroom')


car1 = SportCar(100, 'yellow', 'Ivan')
print(car1.speed)
car1.speed = 200
print(car1.speed)
car1.beep()
car1.say_owner()
car1.max_speed(300)
print(car1.speed)
car1.wroom()
