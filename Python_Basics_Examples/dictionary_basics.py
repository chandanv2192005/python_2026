# Dictionary Basics Demo
# Dictionaries store data in Key-Value pairs. Think of it like a real dictionary or a phonebook.

def main():
    # 1. Creating a dictionary
    student = {
        "name": "Chandan",
        "age": 20,
        "courses": ["Math", "Cybersecurity"],
        "is_intern": True
    }

    print(f"Student Data: {student}")

    # 2. Accessing values
    print(f"Name: {student['name']}")
    # Use .get() to avoid errors if key doesn't exist
    print(f"Grade: {student.get('grade', 'Not Assigned Yet')}")

    # 3. Adding/Updating items
    student["grade"] = "A"
    student["age"] = 21
    print(f"Updated Student: {student}")

    # 4. Looping through a dictionary
    print("\nIterating through keys and values:")
    for key, value in student.items():
        print(f"- {key}: {value}")

    # 5. Nesting dictionaries (Data within data)
    students = {
        "001": {"name": "Alice", "score": 95},
        "002": {"name": "Bob", "score": 88}
    }
    print(f"\nStudent 001 name: {students['001']['name']}")

if __name__ == "__main__":
    main()
