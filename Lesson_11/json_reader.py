import json

# json.dumps()
# json.loads()

filename = 'file.json'

info = {
    "ФИО": "Пупкин Василий Васильевич",
    "Оценки": {
        "Математика": 4,
        "Информатика": 5,
    },
    "Хобби": ["Программирование", "Учёба"],
    "Возраст": 15,
    "Дом_Животные": None
}

with open(filename, 'w', encoding='utf-8') as file:
    file.write(json.dumps(info, ensure_ascii=False, indent=4))

info_2 = {}
with open(filename, encoding="utf-8") as file:
    info_2 = json.loads(file.read())

print(info_2)
