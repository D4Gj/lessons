f = open('C:\\Users\\inzad\\AppData\\Local\\JetBrains\\PyCharm2020.1\\python_stubs\\1699852814\\builtins.py')
lines = (t for t in f)
comments = (t for t in lines if t[0] == '#')

print(list(comments))
for c in comments:
    print(c)
