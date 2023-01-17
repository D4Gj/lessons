class Myclass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # геттер
        return self._name + ' Крутой чел'

    @name.setter
    def name(self, name):  # сеттер
        self._name = name


a = Myclass('Ivan')
print(a.name)
a.name = 'Sergey'
print(a.name)

# 2 + 2 = 22
# 2 + 20 = 22