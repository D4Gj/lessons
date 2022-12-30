import time


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

# f(5) = 5*f(4) = 5*4*f(3) = 5*4*3*2*f(1.txt)
ft = time.time()
# print(factorial(500))
print(ft - time.time())
st = time.time()
i = 1
for j in range(1, 501):
    i *= j
print(i)
print(st - time.time())
