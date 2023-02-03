numbers = [1, 2, 3, 4]
result = (x * x for x in numbers)
result2 = [x * x for x in numbers]
print(result, result2)
# for number in result:
#     print(number)

print(next(result))
print(next(result))
print(next(result))
print(next(result, 'Мб ошибка'))
#print(next(result, 'Мб ошибка'))
# print(next(result))
# print(next(result, 'Мб ошибка'))
# print(next(result, 'Мб ошибка'))
print(result)
for number in result:
    print(type(number))
    if not number:
        print('Пришло пустое')
    print(number)
# next(iterator, default) - следующий элемент итератора, вызвав метод __next__()
# iterator - объект итератора
# default - значение по умолчанию вместо исключения StopIteration
object