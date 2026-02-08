def main():
    # Read two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # 1. Addition
        addition = num1 + num2
        print(f"Addition: {num1} + {num2} = {addition}") 

        # 2. Subtraction
        subtraction = num1 - num2
        print(f"Subtraction: {num1} - {num2} = {subtraction}")

        # 3. Multiplication
        multiplication = num1 * num2
        print(f"Multiplication: {num1} * {num2} = {multiplication}")

        # 4. Division
        if num2 != 0:
            division = num1 / num2
            print(f"Division: {num1} / {num2} = {division}")
        else:
            print("Division: Cannot divide by zero")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
