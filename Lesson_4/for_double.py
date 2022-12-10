# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

for i in range(5):
    for j in range(5):
        if i == j or i + j == 4 or i == 2 or j == 2:
            print('X', end='')
        else:
            print('.', end='')
    print()

