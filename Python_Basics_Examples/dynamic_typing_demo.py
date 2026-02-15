def demonstrate_dynamic_typing():
    print("--- Python Dynamic Typing Demo ---")

    # 1. No explicit type declaration needed
    # The interpreter infers the type at runtime.
    x = 10
    print(f"Initial: x = {x}, Type: {type(x)}")

    # 2. Variable can change types (reassignment)
    # This is not possible in statically typed languages like C++ or Java.
    x = "Hello, Python!"
    print(f"After reassignment: x = '{x}', Type: {type(x)}")

    # 3. List can hold multiple types
    mixed_list = [1, "Python", 3.14, True]
    print(f"\nMixed List: {mixed_list}")
    for item in mixed_list:
        print(f"  Item: {item}, Type: {type(item)}")

    # 4. Impact: No need to declare types for functions
    def add_anything(a, b):
        return a + b

    print(f"\nFunction 'add_anything':")
    print(f"  Integers: 5 + 5 = {add_anything(5, 5)}")
    print(f"  Strings: 'Hello' + ' World' = {add_anything('Hello', ' World')}")
    print(f"  Lists: [1] + [2] = {add_anything([1], [2])}")

if __name__ == "__main__":
    demonstrate_dynamic_typing()
