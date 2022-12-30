import csv

filename = "test_dict.csv"

shop_list = {"картофель": [2, 100], 'яблоки': [3, 250]}

with open(filename, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'weight', 'price'], quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for name, values in sorted(shop_list.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1]))

rows = []
with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for row in rows:
    print(row)
print(rows)
