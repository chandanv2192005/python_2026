def greet(name: str) -> str:
    """
    1. Basic Function with Type Hinting and Docstring.
    Takes a name and returns a greeting string.
    """
    return f"Hello, {name}!"

def power(base, exponent=2):
    """
    2. Function with Default Arguments.
    Calculates base to the power of exponent (default is squared).
    """
    return base ** exponent

def describe_pet(animal_type, pet_name):
    """
    3. Function demonstrating Keyword Arguments.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

def sum_all(*args):
    """
    4. Function with Variable-Length Positional Arguments (*args).
    Accepts any number of arguments and sums them up.
    """
    return sum(args)

def build_profile(first, last, **user_info):
    """
    5. Function with Variable-Length Keyword Arguments (**kwargs).
    Builds a dictionary containing everything we know about a user.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

def apply_operation(x, y, operation):
    """
    6. Higher-Order Function: Passing a function as an argument.
    """
    return operation(x, y)

def main():
    print("--- Python Function Examples ---\n")

    # 1. Basic Function
    print(f"1. {greet('Alice')}")

    # 2. Default Arguments
    print(f"\n2. Power (default): 5^2 = {power(5)}")
    print(f"   Power (custom):  5^3 = {power(5, 3)}")

    # 3. Keyword Arguments
    print("\n3. Keyword Arguments:")
    describe_pet(pet_name="Harry", animal_type="hamster") # Order doesn't matter

    # 4. *args
    total = sum_all(10, 20, 30, 40)
    print(f"\n4. Summing multiple numbers (10, 20, 30, 40): {total}")

    # 5. **kwargs
    user_profile = build_profile('Albert', 'Einstein',
                                 location='Princeton',
                                 field='Physics',
                                 nobel_prize=True)
    print(f"\n5. User Profile (**kwargs): {user_profile}")

    # 6. Lambda Functions (Anonymous Functions)
    print("\n6. Lambda Functions:")
    result_add = apply_operation(10, 5, lambda a, b: a + b)
    result_mul = apply_operation(10, 5, lambda a, b: a * b)
    print(f"   Add (lambda): 10 + 5 = {result_add}")
    print(f"   Multiply (lambda): 10 * 5 = {result_mul}")

if __name__ == "__main__":
    main()
