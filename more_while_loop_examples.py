import random
import time

def collatz_conjecture(n):
    print(f"\n--- 1. Collatz Conjecture (Starting at {n}) ---")
    steps = 0
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    print(1)
    print(f"Reached 1 in {steps} steps.")

def newton_sqrt(number, tolerance=1e-7):
    print(f"\n--- 2. Newton's Method for Square Root of {number} ---")
    guess = number / 2.0
    iteration = 0
    while True:
        iteration += 1
        new_guess = (guess + number / guess) / 2.0
        diff = abs(guess - new_guess)
        print(f"Iteration {iteration}: {new_guess:.9f} (diff: {diff:.9f})")
        if diff < tolerance:
            break
        guess = new_guess
    print(f"Approximate square root: {new_guess}")

def prime_factory(count_needed):
    print(f"\n--- 3. Generating first {count_needed} Prime Numbers ---")
    primes = []
    num = 2
    while len(primes) < count_needed:
        # Check if num is prime
        is_prime = True
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        
        if is_prime:
            primes.append(num)
        num += 1
    print(f"Primes: {primes}")

def binary_search_game():
    print("\n--- 4. Computer Guesses Your Number (Binary Search) ---")
    print("Think of a number between 1 and 100.")
    input("Press Enter when you are ready...")
    
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        print(f"My guess is {guess}.")
        feedback = input("Is it too (h)igh, too (l)ow, or (c)orrect? ").lower()
        
        if feedback == 'c':
            print(f"I got it in {attempts} attempts!")
            return
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please enter 'h', 'l', or 'c'.")
    
    print("I think you might be cheating... I can't guess it!")

def bank_system_simulation():
    print("\n--- 5. Simple Bank System Simulation ---")
    balance = 1000
    while True:
        print("\n--- Bank Menu ---")
        print(f"Current Balance: ${balance}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposited ${amount}. New balance: ${balance}")
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: "))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"Withdrew ${amount}. New balance: ${balance}")
                elif amount > balance:
                    print("Insufficient funds.")
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '3':
            print("Exiting Bank System.")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    print("Demonstrating Complex Python While Loops")
    
    collatz_conjecture(27)
    newton_sqrt(25)
    prime_factory(10)
    
    # Interactive parts
    # binary_search_game()
    # bank_system_simulation()

if __name__ == "__main__":
    main()
