def demonstrate_with_statement():
    print("--- Python 'with' Statement Demo ---")

    # 1. The Old Way (Manual)
    # You have to remember to close the file, even if an error occurs.
    f = open("example.txt", "w")
    try:
        f.write("Hello from the old way!")
    finally:
        f.close()
        print("Manual: File closed successfully.")

    # 2. The 'with' Way (Recommended)
    # The 'with' statement is a "Context Manager".
    # It automatically closes the file for you as soon as the block ends.
    with open("example_with.txt", "w") as f:
        f.write("Hello from the 'with' statement!")
        print("Inside 'with': File is open.")
    
    # At this point, the file is ALREADY closed.
    print("Outside 'with': File is automatically closed.")

    # 3. Benefits: Even if an ERROR occurs inside 'with', 
    # Python guarantees the file will be closed properly.
    try:
        with open("error_test.txt", "w") as f:
            print("Trying to do something risky...")
            raise Exception("Something went wrong!")
    except Exception as e:
        print(f"Caught Error: {e}")
    
    # Even though we crashed, the file handle is released by the OS.
    print("Post-Error: Resource cleanup handled by Context Manager.")

if __name__ == "__main__":
    demonstrate_with_statement()
