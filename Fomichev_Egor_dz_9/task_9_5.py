class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки объекта "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        return print(f'Объект "{self.title}" нарисован карандашом')


class Pen(Stationery):
    def draw(self):
        return print(f'Объект "{self.title}" нарисован ручкой')


class Hadle(Stationery):
    def draw(self):
        return print(f'Объект "{self.title}" нарисован маркером')
