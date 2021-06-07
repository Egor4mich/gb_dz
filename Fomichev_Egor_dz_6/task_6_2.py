with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    dict_of_data = {}
    for line in f:
        dict_of_data.setdefault(line.split()[0], 0)
        dict_of_data[line.split()[0]] += 1
print(max(dict_of_data, key=dict_of_data.get))
