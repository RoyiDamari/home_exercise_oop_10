from abc import ABC, abstractmethod



class InputValidator(ABC):

    def get_valid_input(self):

        while True:
            self.show_message()
            user_input = InputValidator.ask_for_input()
            if InputValidator.is_empty(user_input):
                print("Input cannot be empty. Try again.")
                continue

            converted_input = self.convert_input(user_input)

            if converted_input is None:
                print("Invalid input format. Try again.")
                continue

            if not self.validate_input(converted_input):
                print("Input does not meet requirements. Try again.")
                continue

            return converted_input


    @abstractmethod
    def show_message(self):
        pass

    @staticmethod
    def ask_for_input():
        return input().strip()

    @staticmethod
    def is_empty(user_input):
        return user_input.strip() == ""

    @abstractmethod
    def convert_input(self, user_input):
        pass

    @abstractmethod
    def validate_input(self, converted_input):
        pass






