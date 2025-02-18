from free_calculator_proxy import FreeCalculatorProxy

def main():
    calculator = FreeCalculatorProxy()

    print("10 + 5 =", calculator.add(10, 5))
    print("10 - 5 =", calculator.subtract(10, 5))

    try:
        print("10 * 5 =", calculator.multiply(10, 5))
    except PermissionError as e:
        print(e)

    try:
        print("10 / 5 =", calculator.divide(10, 5))
    except PermissionError as e:
        print(e)

    try:
        print("10 ^ 5 =", calculator.power(10, 5))
    except PermissionError as e:
        print(e)

if __name__ == "__main__":
    main()
