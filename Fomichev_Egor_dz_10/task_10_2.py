from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def calc_required_cloth(self):
        '''расчет требуемой ткани'''
        pass

    @abstractmethod
    def measuring_clothes(self):
        '''задать новый размер'''
        pass


class Clothes(AbstractClothes):

    def __init__(self, name, measuring):
        self.name = name
        self.measuring = measuring

    @property
    def calc_required_cloth(self):
        '''расчет требуемой ткани'''
        pass

    @property
    def measuring_clothes(self):
        '''узнать размер'''
        return self.measuring

    @measuring_clothes.setter
    def measuring_clothes(self, size):
        '''задать новый размер'''
        self.measuring = size

    def __add__(self, other):
        return f'Нужно всего {self.calc_required_cloth + other.calc_required_cloth} кв. метров ткани'


class Coat(Clothes):
    @property
    def calc_required_cloth(self):
        '''расход ткани на пальто'''
        return round(self.measuring / 6.5 + 0.5, 2)

    def __str__(self):
        return f'На пальто размером {self.measuring} см необходимо {self.calc_required_cloth} кв. метров ткани'


class Gard(Clothes):
    @property
    def calc_required_cloth(self):
        '''расход ткани на костюм'''
        return round(2 * self.measuring * 0.01 + 0.3, 2)

    def __str__(self):
        return f'На костюм ростом {self.measuring} см необходимо {self.calc_required_cloth} кв. метров ткани'
