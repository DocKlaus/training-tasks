"""
Создайте класс ComplexNumber, представляющий комплексное число.
Реализуйте методы __add__, __sub__, __mul__ , __str__ и __abs__
для выполнения арифметических операций и представления числа в строковом формате.

Комплексное число — это число вида z=a+bi,
где:
а - действительная часть
b - мнимая часть
i - мнимая единица
"""

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        """ Сложение комплексных чисел"""
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        """ Вычитание комплексных чисел"""
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        """ Умножение комплексных чисел"""
        return ComplexNumber(self.real * other.real, self.imaginary * other.imaginary)

    def __truediv__(self, other):
        """ Деление комплексных чисел"""
        denominator = other.real**2 + other.imaginary**2
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / denominator,
            (self.imaginary * other.imaginary) / denominator
        )

    def __abs__(self):
        """ Модуль комплексного числа"""
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        """Сравнение комплексных чисел"""
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        """Строковое представление"""
        if self.imaginary >= 0:
            return f'{self.real} + {self.imaginary}i'
        else:
            return f'{self.real} - {self.imaginary}i'
