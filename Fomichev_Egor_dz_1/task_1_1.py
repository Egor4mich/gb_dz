duration = int(input())
if duration < 60:
    print(f'{duration} сек')
if 60 <= duration < 3600:
    minuts = duration // 60
    seconds = duration % 60
    print(f'{minuts} мин {seconds} сек')
if 3600 <= duration < 86400:
    hours = duration // 3600
    minuts = duration % 3600 // 60
    seconds = duration % 60
    print(f'{hours} час {minuts} мин {seconds} сек')
if 86400 <= duration < 2592000:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minuts = duration % 3600 // 60
    seconds = duration % 60
    print(f'{days} дн {hours} час {minuts} мин {seconds} сек')
if 2592000 <= duration < 31104000:
    months = duration // 2592000
    days = duration % 2592000 // 86400
    hours = duration % 86400 // 3600
    minuts = duration % 3600 // 60
    seconds = duration % 60
    print(f'{months} мес {days} дн {hours} час {minuts} мин {seconds} сек')
if duration >= 31104000:
    years = duration // 31104000
    months = duration % 31104000 // 2592000
    days = duration % 2592000 // 86400
    hours = duration % 86400 // 3600
    minuts = duration % 3600 // 60
    seconds = duration % 60
    print(f'{years} год {months} мес {days} дн {hours} час {minuts} мин {seconds} сек')