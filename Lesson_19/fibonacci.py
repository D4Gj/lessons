# # Числа фибоначчи представляют последовательность, получаемую в результате сложения двух предыдущих элементов.
# Начинается коллекция с чисел 1 и 1.
# Она достаточно быстро растёт, поэтому вычисление больших значений занимает немало времени.
# Создайте функцию fib(n), генерирующую n чисел фибоначчи с минимальными затратами ресурсов. Используйте yield

def fibonacci_of(n):
    # Handle the base cases

    previous, fib_number = 1, 1

    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


def fibonacci_of1(n):
    # Handle the base cases

    previous, fib_number = 1, 1
    yield previous
    yield fib_number
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number
        yield fib_number
    return fib_number


for num in fibonacci_of1(500000):
    pass
print(num)
# print(fibonacci_of(500000))
