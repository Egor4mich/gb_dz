import sys
with open('bakery.csv', 'a', encoding='UTF-8') as f:
    f.write(f'{sys.argv[1]}\n')