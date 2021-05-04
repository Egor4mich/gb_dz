list_of_prices = [55.04, 37.54, 10001.2, 450, 234.34, 765.99, 200.50, 123.32, 500.99, 10, 5.02, 3.07, 9.99, 277.6,
                  863.01, 45.97]

# Подзадача A
for i in list_of_prices:
    if list_of_prices[::-1].index(i) == 0:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп')
    else:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп', end=', ')

# Подзадача В
print(id(list_of_prices))  # ID списка до сортировки
list_of_prices.sort()  # сортировка
print(id(list_of_prices))  # ID после сортировки

for i in list_of_prices:
    if list_of_prices[::-1].index(i) == 0:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп')
    else:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп', end=', ')

# Подзадача C
list_of_prices_after_sort = sorted(list_of_prices, reverse=True)  # сортировка функцией sorted и создание нового списка
print(id(list_of_prices_after_sort))  # ID нового списка

# Подзадача D
for i in list_of_prices[-5:]:
    if list_of_prices[::-1].index(i) == 0:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп')
    else:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп', end=', ')
