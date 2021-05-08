def thesaurus(*args: str) -> dict:
    """Принимает строки, возвращает отсортированный по ключам словарь, в котором ключи - первые буквы строк,
    а значения - списки, содержащие строки, начинающиеся с соответсвующей буквы"""
    data = {}
    for i in sorted(args):
        data.setdefault(i[0], [])
        data[i[0]].append(i)
    return data


def thesaurus_adv(*args: str) -> dict:
    """Принимает в качестве аргументов строки в формате «Имя Фамилия» и возвращает отсортированный по ключам словарь,
    в котором ключи — первые буквы фамилий, а значения — отсортированные по ключам словари, в которых ключи -
    первые буквы имен и значения - списки содержащие записи, в которых фамилия начинается с соответствующей буквы"""
    data = {}
    for name in sorted(list(args), key=lambda i: i.split()[1]):
        data.setdefault(name.split()[1][0], {})
        data[name.split()[1][0]].setdefault(name.split()[0][0], [])
        data[name.split()[1][0]][name.split()[0][0]].append(name)
    return data
