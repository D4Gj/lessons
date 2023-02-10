def korona(func):
    def wrapper():
        print('👑')
        func()

    return wrapper
@korona
def snake():
    print('<:=====')

snake()