class MyClass:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        x = self.start
        while x < self.stop:
            yield x
            x += self.step

    def __str__(self):
        return f'range({self.start},{self.stop})'
nums = MyClass(0, 10, 1)
print(nums,range(10))
for x in nums:
    print(x)

