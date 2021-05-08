import random


def get_jokes(n: int, not_repeat: bool = False) -> Union[list[str], str]:
    """Принимает n - целое число, not_repeat - boolean, возвращает список, содержащий n строк, полученных из 3х заданных
    списков (nouns, adverbs, adjectives). При этом каждая строка содержит по одному элементу каждого списка.
    Если not_repeat передается со значением True, то возвращается список строк без повторов, но при этом n не может быть
    больше длины заданных списков, в противном случае возвращается предупреждение"""
    if not_repeat:
        if n <= len(nouns):
            nouns_2 = nouns.copy()
            adverbs_2 = adverbs.copy()
            adjectives_2 = adjectives.copy()
            jokes = []
            for i in range(n):
                jokes.append(nouns_2.pop(random.randrange(len(nouns_2))) + ' ' +
                             adverbs_2.pop(random.randrange(len(adverbs_2))) + ' ' +
                             adjectives_2.pop(random.randrange(len(adjectives_2))))
            return jokes
        else:
            return 'Нельзя пошутить так много и не повториться ни разу!'
    jokes = []
    for i in range(n):
        jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
