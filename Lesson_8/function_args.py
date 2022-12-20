def draw_stars_simple(amount=5):
    "Функция просто работает"
    print((('*' * amount) + '\n') * amount)


def draw_stars_custom(width, height=1):
    "Функция просто работает"
    print((('*' * width) + '\n') * height)


def draw_stars_hard():
    """Функция рисует
    звёзды 6х6"""
    for i in range(6):
        for j in range(6):
            print('*', end='')
        print()


draw_stars_simple(10)
draw_stars_simple()
draw_stars_custom(10)
draw_stars_custom(height=10, width=15)  # Именованные аргументы
draw_stars_custom(10, 15, )  # Позиционные аргументы
n = 10
m = 20
print(draw_stars_custom(n, m))

