a = {2: 1, 'a': 2}

for key in a:
    print(key)
for key in a:
    print(a[key])

for key, value in a.items():
    print(f'{key} - {value}')

for item in a.items():
    print(item)

for value in a.values():
    print(value)

a = {'level1': [1, 2, 1, 2], 'a': 2}

for monster in a['level1']:
    print(monster)
