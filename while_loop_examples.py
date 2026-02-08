import time

def basic_while_loop():
    print("\n--- 1. Basic While Loop ---")
    print("Counting from 1 to 5:")
    count = 1
    while count <= 5:
        print(f"Count: {count}")
        count += 1

def while_loop_with_break():
    print("\n--- 2. While Loop with Break ---")
    print("Counting until 3, then breaking:")
    count = 1
    while True:
        print(f"Count: {count}")
        if count == 3:
            print("Breaking the loop!")
            break
        count += 1

def while_loop_with_continue():
    print("\n--- 3. While Loop with Continue ---")
    print("Printing only odd numbers from 1 to 5:")
    count = 0
    while count < 5:
        count += 1
        if count % 2 == 0:
            continue  # Skip even numbers
        print(f"Odd number: {count}")

def while_loop_with_else():
    print("\n--- 4. While Loop with Else ---")
    print("Counting down from 3:")
    count = 3
    while count > 0:
        print(f"Count: {count}")
        count -= 1
    else:
        print("Loop completed successfully without a break.")

def input_validation_loop():
    print("\n--- 5. Input Validation Loop ---")
    while True:
        user_input = input("Type 'exit' to stop: ").lower()
        if user_input == 'exit':
            print("Exiting input loop.")
            break
        print(f"You typed: {user_input}")

def main():
    print("Demonstrating Python While Loops")
    basic_while_loop()
    while_loop_with_break()
    while_loop_with_continue()
    while_loop_with_else()
    input_validation_loop()

if __name__ == "__main__":
    main()
