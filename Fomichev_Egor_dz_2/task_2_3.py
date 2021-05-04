list_of_something = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(list_of_something))

i = 0
while i < len(list_of_something):
    if not list_of_something[i].isalpha():
        if list_of_something[i][0] == '+' or list_of_something[i][0] == '-':
            list_of_something[i] = f'{list_of_something[i][0]}{int(list_of_something[i][1:]):02}'
            list_of_something.insert(i, '"')
            list_of_something.insert(i + 2, '"')
            i += 3
            continue
        list_of_something[i] = f'{int(list_of_something[i]):02}'
        list_of_something.insert(i, '"')
        list_of_something.insert(i + 2, '"')
        i += 3
    else:
        i += 1
print(id(list_of_something))

message = ''
i = 0
while i < len(list_of_something):
    if list_of_something[i] != '"':
        message += list_of_something[i] + ' '
        i += 1
    else:
        message += ''.join(list_of_something[i:i + 3]) + ' '
        i += 3

print(message)
