import csv

filename = "test.csv"

shop_list = {"картофель": [2, 100], 'яблоки': [3, 250]}

with open(filename, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Наименование", "Вес", "Цена за кг"])  # Заголовки столбца
    for name, values in sorted(shop_list.items()):
        writer.writerow([name, *values])
    writer.writerow(["майонез", '4', '100'])

rows =[]
with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

print(rows)
