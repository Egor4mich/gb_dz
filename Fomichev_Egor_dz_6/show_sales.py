import sys
import itertools
with open('bakery.csv') as sales:
    if len(sys.argv) == 1:
        for line in sales:
            print(line, end='')
    if len(sys.argv) == 2:
        for line in itertools.islice(sales, int(sys.argv[1]) - 1, sys.maxsize):
            print(line, end='')
    if len(sys.argv) == 3:
        for line in itertools.islice(sales, int(sys.argv[1]) - 1, int(sys.argv[2])):
            print(line, end='')
