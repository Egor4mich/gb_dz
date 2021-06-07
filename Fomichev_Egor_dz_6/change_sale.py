import fileinput
import sys

if len(sys.argv) != 3:
    print('Введите номер номер записи и значение!')
    sys.exit()

else:
    with fileinput.input('bakery.csv') as f:
        if int(sys.argv[1]) not in [int(f.filelineno()) for i in f]:
            print('Такой записи нет')
            sys.exit()
    with fileinput.input('bakery.csv', inplace=True) as f:
        for line in f:
            if f.filelineno() == int(sys.argv[1]):
                print(sys.argv[2])
            else:
                print(line, end='')
