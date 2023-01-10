# Машина => Грузовая => Карьер
#                    => Продуктов
#        => Легковая

# Инкапсуляция
# Наследование
# Полиморфизм
class Car:
    manufacturer = 'Tesla'
    model = 'model X'
    mileage = 100

    def beep(self):
        print(self.model + ' Бибикает')


my_car = Car()
print(my_car.manufacturer)
my_car.manufacturer = 'Lada'
print(my_car.manufacturer)
my_car.beep()
