class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    def __reversed__(self):
        pass


myclass = MyNumbers()
for x in myclass:
    print(x)
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
# raise ZeroDivisionError
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
for x in myiter:
    print(x)
for i in reversed([1, 2, 3]):
    print(i)
