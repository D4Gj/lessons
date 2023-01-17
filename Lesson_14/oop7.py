class Transport:
    def __init__(self, speed, color='white'):
        self.speed = speed
        self.color = color

    def beep(self):
        print('beep')


mazda1 = Transport(100)
# print(mazda1.color)
mazda2 = Transport(100, 'Red')
print(f' Это цвета моих машин {mazda1.color=} {mazda2.color=}')
print('{mazda1.color=} {mazda2.color=}')
