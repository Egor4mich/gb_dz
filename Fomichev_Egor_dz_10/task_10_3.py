class Cell:
    def __init__(self, quantity: int):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            return f'Разность клеток не может быть меньше 0!'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self) -> str:
        return f"Клетка состоит из {self.quantity} ячеек"

    def make_order(self, cell_in_row):
        row = self.quantity // cell_in_row
        remainder_cell_in_row = self.quantity % cell_in_row
        return '\n'.join(['*' * cell_in_row] * row + (['*' * remainder_cell_in_row]))
