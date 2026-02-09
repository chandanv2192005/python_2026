import time
import functools

# --- 1. Decorators (Modifying behavior) ---
def timer_decorator(func):
    """
    A decorator that measures the execution time of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def slow_function(seconds):
    """
    A function that sleeps to demonstrate the timer decorator.
    """
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return "Wake up!"

# --- 2. Closures (Function factories) ---
def multiplier_factory(factor):
    """
    Returns a function that multiplies its input by 'factor'.
    This demonstrates closures: the inner function remembers 'factor'.
    """
    def multiplier(number):
        return number * factor
    return multiplier

# --- 3. Generators (Yielding values lazily) ---
def fibonacci_generator(limit):
    """
    A generator that yields Fibonacci numbers up to a limit.
    Memory efficient compared to creating a full list.
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# --- 4. Recursion (Function calling itself) ---
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi puzzle recursively.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# --- 5. Initial Examples (kept for reference) ---
def greet(name: str) -> str:
    return f"Hello, {name}!"

def power(base, exponent=2):
    return base ** exponent

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

def sum_all(*args):
    return sum(args)

def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)
    return profile

def apply_operation(x, y, operation):
    return operation(x, y)

def main():
    print("--- Advanced Python Function Examples ---\n")

    # 1. Decorators
    print("1. Decorators:")
    slow_function(0.5)

    # 2. Closures
    print("\n2. Closures:")
    double = multiplier_factory(2)
    triple = multiplier_factory(3)
    print(f"   Double of 10: {double(10)}")
    print(f"   Triple of 10: {triple(10)}")

    # 3. Generators
    print("\n3. Generators (Fibonacci up to 20):")
    for num in fibonacci_generator(20):
        print(num, end=" ")
    print()

    # 4. Recursion
    print("\n4. Recursion (Tower of Hanoi - 3 Disks):")
    tower_of_hanoi(3, 'A', 'C', 'B')

    # Quick run of basic examples
    print("\n--- Basic Examples (Recap) ---")
    print(greet("Alice"))
    print(f"Power: {power(5)}")
    print(f"Sum *args: {sum_all(1, 2, 3)}")

if __name__ == "__main__":
    main()
