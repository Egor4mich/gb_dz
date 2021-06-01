class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'машина марки {self.name} поехала')

    def stop(self):
        return print(f'машина марки {self.name} остановилась')

    def turn(self, direction):
        return print(f'машина марки {self.name} повернула {direction}')

    def show_speed(self):
        return print(f'скорость автомобиля {self.name} равна {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print('Превышение скорости!')
        return print(f'скорость автомобиля {self.name} равна {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print('Превышение скорости!')
        return print(f'скорость автомобиля {self.name} равна {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        if self.is_police == False:
            self.show_message()

    def show_message(self):
        return print('Это не полицеская машина!')
