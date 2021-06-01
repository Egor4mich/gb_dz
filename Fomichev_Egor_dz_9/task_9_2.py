class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, mass_for_one, number_of_layers):
        return self._length * self._width * mass_for_one * number_of_layers
