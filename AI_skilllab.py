from decimal import Decimal, InvalidOperation

def get_number(prompt):
    while True:
        try:
            value = input(prompt).strip()

            if not value:
                print("Error: Input cannot be empty. Please try again.")
                continue

            number = Decimal(value)

            if not number.is_finite():
                print("Error: Please enter a finite number.")
                continue

            return number

        except InvalidOperation:
            print("Error: Invalid input. Enter a valid number, such as 10, -5, 3.14, or 0.")

def add_three_numbers():
    print("=== Three Number Addition Calculator ===")

    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    c = get_number("Enter the third number: ")

    result = a + b + c

    print("\n--- Result ---")
    print(f"First number  : {a}")
    print(f"Second number : {b}")
    print(f"Third number  : {c}")
    print(f"Sum           : {result}")

try:
    add_three_numbers()
except (KeyboardInterrupt, EOFError):
    print("\nError: Input cancelled by the user.")
