print(sum([x if x % 3 == 0 or x % 5 == 0 else 0 for x in range(1000)]))

summa = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        summa += i
print(summa)