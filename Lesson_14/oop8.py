class Transport:
    def __init__(self, speed, color='white', owner=None) -> None:
        self.speed = speed
        self.color = color
        self.owner = owner

    def say_owner(self):
        if self.owner:
            print(f'Владелец - {self.owner}')
        else:
            print('У авто нет владельца')


car1 = Transport(100, owner='Ivan')
car2 = Transport(90)
car1.say_owner()
print(car1.color)
car2.say_owner()
print(car2.color)
