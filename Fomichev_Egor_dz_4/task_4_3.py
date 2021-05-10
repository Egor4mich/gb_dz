import requests
from datetime import datetime
from decimal import Decimal


def currency_rates(val):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    date = datetime.strptime(response.headers['Date'], '%a, %d %B %Y %H:%M:%S %Z').date()
    response = response.json()
    if not response['Valute'].get(val.upper()):
        return
    return f'{Decimal(str(response["Valute"][val.upper()]["Value"]))}, {date}'
