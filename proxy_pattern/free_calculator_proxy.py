from typing import override
from calculator import Calculator
from full_calculator import FullCalculator


class FreeCalculatorProxy(Calculator):

    def __init__(self):
        self.full_calculator = FullCalculator()

    @override
    def add(self, a, b):
        return self.full_calculator.add(a, b)

    @override
    def subtract(self, a, b):
        return self.full_calculator.subtract(a, b)

    @override
    def multiply(self, a, b):
        raise PermissionError("Access Denied: Multiplication is a premium feature!")

    @override
    def divide(self, a, b):
        raise PermissionError("Access Denied: Division is a premium feature!")

    @override
    def power(self, a, b):
        raise PermissionError("Access Denied: Power is a premium feature!")
