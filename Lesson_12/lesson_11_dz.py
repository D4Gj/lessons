n = int(input())
todo_list = []
for i in range(n):
    todo_list.append(input())
with open('todo_list.txt', 'a') as file:
    for todo in range(0, len(todo_list), 2):
        file.write(todo_list[todo] + "---")
