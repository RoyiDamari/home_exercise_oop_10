from typing import override
from calculator import Calculator


class FullCalculator(Calculator):

    @override
    def add(self, a, b):
        return a + b

    @override
    def subtract(self, a, b):
        return a - b

    @override
    def multiply(self, a, b):
        return a * b

    @override
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero!")
        return a / b

    @override
    def power(self, a, b):
        return a ** b
