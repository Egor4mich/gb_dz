# Задание 1
def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


# Задание 2
def odd_nums_adv(n):
    num = (i for i in range(1, n + 1, 2))
    return num
