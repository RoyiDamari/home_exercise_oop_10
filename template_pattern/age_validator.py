from typing import override
from input_validator import InputValidator


class AgeValidator(InputValidator):

    @override
    def show_message(self):
        print("Enter your age (1-100): ", end='')

    @override
    def convert_input(self, user_input):
        try:
            return int(user_input)
        except ValueError:
            return None

    @override
    def validate_input(self, converted_input):
        return isinstance(converted_input, int) and 1 <= converted_input <= 100