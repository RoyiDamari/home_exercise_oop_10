from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

    @abstractmethod
    def power(self, a, b):
        pass
