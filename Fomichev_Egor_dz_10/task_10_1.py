class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size_matrix = len(self.matrix)
        self.size_row_matrix = set(len(row) for row in self.matrix)
        if len(self.size_row_matrix) != 1:
            raise ValueError('Ряды матрицы разного размера')

    @staticmethod
    def _print_matrix(matrix):
        if len(matrix) != 1:
            for row in matrix:
                print(*row)
                return Matrix._print_matrix(matrix[1:])
        else:
            return ' '.join(map(str, matrix[0]))

    def __str__(self):
        return str(Matrix._print_matrix(self.matrix))

    def __add__(self, other):
        if self.size_matrix == other.size_matrix:
            if self.size_row_matrix == other.size_row_matrix:
                result_matrix = [[el1 + el2 for el1, el2 in zip(row1, row2)] for row1, row2 in
                                 zip(self.matrix, other.matrix)]
                return Matrix(result_matrix)
            else:
                raise ValueError('Складываемые матрицы имеют разный размер рядов')
        else:
            raise ValueError('Складываемые матрицы имеют разный размер')
