class Worker:
    def __init__(self, name, surname, position, wade, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wade': wade, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return f'Доход с учетом премии {(self._income["wade"] + self._income["bonus"])}'
