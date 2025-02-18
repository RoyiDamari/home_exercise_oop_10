from age_validator import AgeValidator
from email_validator import EmailValidator


def main():
    print("\nNumber Validation:")
    number_validator = AgeValidator()
    valid_number = number_validator.get_valid_input()
    print(f"Valid number entered: {valid_number}")

    print("\nEmail Validation:")
    email_validator = EmailValidator()
    valid_email = email_validator.get_valid_input()
    print(f"Valid email entered: {valid_email}")

if __name__ == "__main__":
    main()