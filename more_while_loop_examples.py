import random
import time

def fibonacci_sequence(limit):
    print(f"\n--- 1. Fibonacci Sequence (up to {limit}) ---")
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b
    print() # Newline

def factorial_calculation(n):
    print(f"\n--- 2. Factorial Calculation (of {n}) ---")
    result = 1
    count = n
    while count > 0:
        result *= count
        count -= 1
    print(f"Factorial of {n} is: {result}")

def sum_of_digits(number):
    original_number = number
    print(f"\n--- 3. Sum of Digits (of {original_number}) ---")
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    print(f"Sum of digits of {original_number} is: {total_sum}")

def guessing_game():
    print("\n--- 4. Guessing Game ---")
    target_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")
    attempts = 0
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"Good job! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Please enter a valid integer.")

def password_retry(max_attempts=3):
    print(f"\n--- 5. Password Retry (Max {max_attempts} attempts) ---")
    correct_password = "secret"
    attempts = 0
    while attempts < max_attempts:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access Granted!")
            return
        else:
            attempts += 1
            print(f"Wrong password. Attempts remaining: {max_attempts - attempts}")
    
    print("Access Denied. Too many failed attempts.")

def main():
    print("Demonstrating More Python While Loops")
    
    fibonacci_sequence(50)
    factorial_calculation(5)
    sum_of_digits(12345)
    
    # Interactive parts
    guessing_game() 
    password_retry()

if __name__ == "__main__":
    main()
