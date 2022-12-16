counter = 0
proizv = 1
for i in range(-100, 100):
    if i % 2 == 0 and i ** 2 <= 100:
        print(i)
        counter += 1
        proizv *= i
print(counter, proizv)

