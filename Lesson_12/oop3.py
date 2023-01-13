class Car:
    def __init__(self, manufacturer, model, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage

    def __str__(self):
        return f'This is {self.manufacturer} {self.model}'


tesla = Car('lada', 'granta', 20000)
tesla2 = Car('tesla', 'model x', 50000)
tesla3 = Car('tesla', 'model x', 50000)

print(tesla2.model)
print(tesla.model)
print(tesla3.model)
print(tesla3.__dir__())