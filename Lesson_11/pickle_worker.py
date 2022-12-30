import pickle

filename = 'pickle_text.txt'

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

with open(filename, 'wb') as file:
    pickle.dump(info, file)

with open(filename, 'rb') as file:
    info_2 = pickle.load(file)

print(file)
