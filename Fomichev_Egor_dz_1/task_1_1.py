duration = int(input())
seconds = duration % 60
minutes = duration % 3600 // 60
hours = duration % 86400 // 3600
days = duration % 2592000 // 86400
months = duration % 31104000 // 2592000
years = duration // 31104000
if duration < 60:
    print(f'{duration} сек')
if 60 <= duration < 3600:
    print(f'{minutes} мин {seconds} сек')
if 3600 <= duration < 86400:
    print(f'{hours} час {minutes} мин {seconds} сек')
if 86400 <= duration < 2592000:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
if 2592000 <= duration < 31104000:
    print(f'{months} мес {days} дн {hours} час {minutes} мин {seconds} сек')
if duration >= 31104000:
    print(f'{years} г {months} мес {days} дн {hours} час {minutes} мин {seconds} сек')
