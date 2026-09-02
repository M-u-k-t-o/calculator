def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operation():
    operations = {"+", "-", "*", "/"}
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in operations:
            return op
        print("Invalid operation. Please choose +, -, *, or /.")


def main():
    print("Simple Python Calculator")
    first = get_number("Enter the first number: ")
    operation = get_operation()
    second = get_number("Enter the second number: ")

    try:
        if operation == "+":
            result = add(first, second)
        elif operation == "-":
            result = subtract(first, second)
        elif operation == "*":
            result = multiply(first, second)
        else:
            result = divide(first, second)
        print(f"Result: {result}")
    except ZeroDivisionError as exc:
        print(exc)


if __name__ == "__main__":
    main()
