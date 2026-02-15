def multiplication_table(a, b):
    c = a * b
    return c

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {multiplication_table(num, i)}")
    except ValueError:
        print("Please enter a valid integer.")
