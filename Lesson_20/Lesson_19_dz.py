emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep='\n')
created_emails = []
for email in emails:
    for username in emails[email]:
        created_emails.append(username + '@' + email)

# created_emails.sort()
# print(*created_emails)
print(*sorted(created_emails))
