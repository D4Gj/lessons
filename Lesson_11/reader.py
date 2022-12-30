with open('1.txt') as file:
    str1 = file.read()

word_list = str1.split()
print(str1, word_list)
result = ''

for word in word_list:
    result += word + ','

print(result)

better_result = '---@#$123'.join(word_list)
print(better_result)
