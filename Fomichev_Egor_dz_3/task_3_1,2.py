def num_translate_adv(number: str) -> str:
    """Возвращает перевод цифр от 1 до 10 с английского языка на русский на основе заданного словаря.
    Если переводимое слово начинается с заглавной буквы - возвращаемое значение также будет начинаться с заглавной.
    При отсутствии перевода возвращает None"""
    table = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number[0].isupper():
        if number.lower() in table:
            return table[number.lower()].capitalize()
    elif number in table:
        return table[number]
