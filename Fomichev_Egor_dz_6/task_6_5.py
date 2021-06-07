import sys
import re
from itertools import zip_longest

with open(sys.argv[1], encoding='UTF-8') as users, \
        open(sys.argv[2], encoding='UTF-8') as hobbies, \
        open(sys.argv[3], 'w', encoding='UTF-8') as users_hobby:
    for i, j in zip_longest(users, hobbies):
        if i:
            if j is not None:
                hobby = re.sub(r'[\f\n\r\t\v]', '', j)
                users_hobby.write(f"{i.strip()}: {hobby}\n")
            else:
                users_hobby.write(f"{i.strip()}: {j}\n")
        else:
            sys.exit(1)
