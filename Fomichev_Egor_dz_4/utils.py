import requests
from decimal import Decimal
from datetime import datetime


def currency_rates(val):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    date = datetime.strptime(response.headers['Date'], '%a, %d %B %Y %H:%M:%S %Z').date()
    response = response.json()
    if not response['Valute'].get(val.upper()):
        return
    return f'{Decimal(str(response["Valute"][val.upper()]["Value"]))}, {date}'


if __name__ == '__main__':
    print(currency_rates('USD'))
