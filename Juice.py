"""
Задача: Соковыжималка
Необходимо создать класс Juice (Сок), который будет иметь два атрибуты:
name (название)
volume (емкость)
Задачей этого класса будет возможность сложения двух объектов Juice
для получения нового объекта Juice с объединенной емкостью и названиями двух соков, которые складываются.
Например, если добавить апельсиновый "Orange' сок с емкостью 1,0 и яблочный 'Apple' сок с емкостью 2,5,
то результатом должен быть новый объект Juice с атрибутами name = 'Orange&Apple', volume = 3.5

Этот класс должен быть создан таким образом, чтобы позволить легко выполнять операцию сложения для объектов Juice и получать правильный результат.
"""
class Juice:
    def __init__(self, name, volume):
        # Защита от отрицательного объёма
        if volume <= 0:
            raise ValueError('Volume cannot be negative')
        self.name = name
        self.volume = volume

    def __iadd__(self, other):
        # Эта версия изменяет текущий класс. И используется +=, __iadd__
        if not isinstance(other, Juice):
            return NotImplemented
        self.name += f"&{other.name}"
        self.volume += other.volume
        return self

    def __add__(self, other):
        # Эта версия создаёт новый объект
        # + проверка, что объект того же класса
        if not isinstance(other, Juice):
            return NotImplemented
        else:
            new_name = self.name + '&' + other.name
            new_volume = self.volume + other.volume
            return Juice(new_name, new_volume)

    def __str__(self):
        return f'{self.name} ({self.volume}L)'

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)