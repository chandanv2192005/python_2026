def main():
    while True:
        try:
            # Read two numbers from the user
            print("\n--- Calculator ---")
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

        # Ask user if they want to continue
        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
