list_of_something = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
another_list = []

for i in list_of_something:
    if not i.isalpha():
        another_list.append('"')
        if i[0] == '+' or i[0] == '-':
            another_list.append(f'{i[0]}{int(i[1:]):02}')
        else:
            another_list.append(f'{int(i):02}')
        another_list.append('"')
    else:
        another_list.append(i)

message = ''
i = 0
while i < len(another_list):
    if another_list[i] != '"':
        message += another_list[i] + ' '
        i += 1
    else:
        message += ''.join(another_list[i:i + 3]) + ' '
        i += 3

print(message)
