"""
Создайте базовый класс Shape, содержащий методы:

calculate_area(): Этот метод должен быть переопределен в каждом дочернем классе для вычисления площади соответствующей фигуры.
calculate_perimeter(): Этот метод должен быть тоже переопределен в каждом дочернем классе для вычисления периметра соответствующей фигуры.

1) Создайте дочерний класс Rectangle, который наследует от базового класса Shape. Добавьте конструктор (метод __init__()),
принимающий длину и ширину прямоугольника в качестве параметров.
Переопределите методы calculate_area() и calculate_perimeter() для вычисления площади и периметра прямоугольника соответственно.

2) Создайте дочерний класс Circle, также наследующий от базового класса Shape. Добавьте конструктор,
принимающий радиус круга в качестве параметра. Переопределите методы calculate_area() и calculate_perimeter()
 ля вычисления площади и периметра круга соответственно.

Для pi используйте библиотеку math
"""

import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


# Тесты
# Тесты
rectangle = Rectangle(5, 7)
assert rectangle.calculate_area() == 35
assert rectangle.calculate_perimeter() == 24

circle = Circle(3)
assert round(circle.calculate_area(), 2) == 28.27
assert round(circle.calculate_perimeter(), 2) == 18.85

assert round(rectangle+circle,2) == 63.27

print("Тесты пройдены успешно!")