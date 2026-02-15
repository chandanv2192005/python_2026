def find_maximum(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def main():
    try:
        # Prompt user for input
        user_input = input("Enter numbers separated by spaces: ")
        # Convert input string into a list of floats
        array = [float(x) for x in user_input.split()]
        
        result = find_maximum(array)
        
        if result is not None:
            print(f"The maximum value in the array is: {result}")
        else:
            print("The array is empty.")
            
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

if __name__ == "__main__":
    main()
