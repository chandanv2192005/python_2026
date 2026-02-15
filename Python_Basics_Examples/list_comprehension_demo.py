# List Comprehension Demo
# A "Pythonic" way to create and transform lists in one line.

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original numbers: {numbers}")

    # 1. Square all numbers
    # Standard way:
    # squares = []
    # for x in numbers:
    #     squares.append(x**2)
    
    # Pythonic way (List Comprehension):
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")

    # 2. Filter: Only even numbers
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {evens}")

    # 3. Transform and Filter: Squares of odd numbers
    odd_squares = [x**2 for x in numbers if x % 2 != 0]
    print(f"Squares of odd numbers: {odd_squares}")

    # 4. Working with strings
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    long_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
    print(f"Loud long fruits: {long_fruits}")

if __name__ == "__main__":
    main()
