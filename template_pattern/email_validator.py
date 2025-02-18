from typing import override
from input_validator import InputValidator


class EmailValidator(InputValidator):

    @override
    def show_message(self):
        print("Enter a valid email (e.g., name@example.com): ", end='')

    @override
    def convert_input(self, user_input):
        return user_input.strip()

    @override
    def validate_input(self, converted_input):
        return "@" in converted_input and converted_input.index("@") > 0 and "." in converted_input.split("@")[-1]
