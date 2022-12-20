def draw_stars_simple():
    "Функция просто работает"
    print((('*' * 5) + '\n') * 5)


def draw_stars_hard():
    """Функция рисует
    звёзды 6х6"""
    for i in range(6):
        for j in range(6):
            print('*', end='')
        print()


draw_stars_hard()
draw_stars_hard()
draw_stars_hard()
draw_stars_hard()
print()
draw_stars_simple()
print()
draw_stars_simple()
print()
draw_stars_simple()
print()
