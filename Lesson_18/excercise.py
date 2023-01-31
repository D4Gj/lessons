# С помощью включения добавить в список все чётные числа, разделённые нацело на два
# в диапазоне от 1 до 100

even_numbers = [i // 2 for i in range(1, 101) if i % 2 == 0]
print(even_numbers)


# Написать функцию, которая принимает словарь с параметрами и возвращает строку запроса
# Пример:
# код print(query({'course':'python','lesson':2,'challenge':17})
def query(params: dict):
    return '&'.join(sorted(f'{k}={v}' for k, v in params.items()))


print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))
