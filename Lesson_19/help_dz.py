adresses = []
domain = 'bestpeople.ru'
logins = ['vasya', 'petya']

for login in logins:
    adresses.append(login + '@' + domain)
print(*sorted(adresses))
