import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        gcd_value = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd_value
        self.denominator = denominator // gcd_value

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

result = frac1 + frac2
print(result == Fraction(5, 4))

result = frac1 - frac2
print(result == Fraction(-1, 4))

result = frac1 * frac2
print(result == Fraction(3, 8))

result = frac1 == frac2
print(result)