list_of_people = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]
for i in list_of_people:
    print(f'Привет, {str(i.split()[-1]).capitalize()}!')
