"""Создайте класс Matrix, который представляет собой матрицу.
Реализуйте метод __init__ для инициализации матрицы,
а также методы __add__, __sub__ и __mul__ для выполнения операций сложения, вычитания и умножения матриц с использованием операторов +, - и *.
(учтите в своем классе, что складывать и вычитать можно матрицы одинаковой размерности)
"""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        result = []
        for i in range(self.__len__()):
            result.append(''.join([str(element).ljust(2) for element in self.matrix[i]]))
        return '\n'.join(result)

    def __eq__(self, other):
        return self.__len__() == other.__len__() and len(self.matrix[0]) == len(other.matrix[0])

    def __add__(self, other):
        if self.__eq__(other):
            result = []
            for i in range(self.__len__()):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
            return Matrix(result)

        else:
            raise ValueError('Матрицы должны быть одинаковой размерности')

    def __sub__(self, other):
        if self.__eq__(other):
            result = []
            for i in range(self.__len__()):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] - other.matrix[i][j])
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError('Матрицы должны быть одинаковой размерности')

    def __mul__(self, other):
        if self.__eq__(other):
            result = []
            for i in range(self.__len__()):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] * other.matrix[i][j])
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError('Матрицы должны быть одинаковой размерности')


m1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
m2 = Matrix([[0, 0, 2], [0, 0, 0], [0, 0, 0]])
print(m1 == m2)
print(m1 + m2)
print()
print(m1 - m2)
print()
print(m1 * m2)