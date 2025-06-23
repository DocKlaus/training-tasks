"""
Декоратор для замера времени выполнения:

Создайте декоратор, который измеряет время выполнения функции и выводит его при вызове функции.
Воспользуйтесь магическими методами __enter__ и __exit__ или только с одним магическим методом __call__
для реализации контекстного менеджера для измерения времени выполнения.
"""

import time

""" Через __call__"""
class TimeDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        """ Экземпляр этого класса можно вызывать с использованием круглых скобок, как если бы это была функция"""
        start = time.perf_counter() # возвращает значение в долях секунды счетчика производительности
        result = self.func(*args, **kwargs) # вызываем исходную функцию с переданными аргументами
        end = time.perf_counter()
        print(f"Функция '{self.func.__name__}' выполнилась за {end - start:.4f} секунд")
        return result

# Пример
@TimeDecorator
def example_function(n):
    return sum(i * i for i in range(n))

print(example_function(1000000), '\n')




""" Через __enter__ и __exit__"""
class TimerContextManager:
    def __enter__(self):
        self.start = time.perf_counter()
        return self # Можно вернуть сам объект для доступа к времени

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f"Выполнение заняло {self.end - self.start:.4f} секунд")

# Пример
with TimerContextManager():  # Вход в контекстный менеджер
    result = sum(i * i for i in range(10**6))  # Код, время которого замеряем
    print("Результат:", result)