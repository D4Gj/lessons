from functools import lru_cache
import datetime


@lru_cache
def func(n):
    result = 0
    for i in range(n):
        result += i
    return result


for i in range(100000):
    func(i)
start1 = datetime.datetime.now()
print(func(10000000))
end1 = datetime.datetime.now()
print(end1 - start1)
start2 = datetime.datetime.now()
print(func(10000001))
end2 = datetime.datetime.now()
print(end2 - start2)
