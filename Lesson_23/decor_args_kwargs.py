# args - позиционные агрументы: 5,5
# kwargs - именованные аргументы: a=5,b=15

def func(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')


func(5, 5, a=5, b=15)
