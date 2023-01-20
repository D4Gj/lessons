class Test(list):
    def append(self, object) -> None:
        for i in range(len(self)):
            self[i] **= object
    
    def pop(self, __index: int = None):
        if __index:
            return f'Вы вытащили из списка значение - {self[__index]}' \
                   f' по индексу {__index}'
        else:
            return 'Вы ничего не указали'


a = Test([1, 2, 3])
print(a)
a.append(10)
print(a)
print(a.pop(1))
