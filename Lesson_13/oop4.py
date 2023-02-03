class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        print('Вызвался родительский метод')

    def beep(self):
        print('beep')


class Car(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner

    def say_owner(self):
        print(f'Владелец - {self.owner}')


class Bus(Transport):
    def __init__(self, speed, color, seeds):
        super().__init__(speed, color)
        self.seeds = seeds

    def say_seeds(self):
        print(f'Мест: {self.seeds}')


avto = Car(100, 'blue', 'Vasya')

print(avto.owner, avto.speed)
print(avto.color)
avto.beep()
avto.say_owner()
bus1 = Bus(150, 'red', 15)
print(bus1.seeds)
bus1.say_seeds()
# print(bus1.owner)
