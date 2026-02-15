def demonstrate_data_types():
    # 1. Numeric Types
    a = 10              # int
    b = 10.5            # float
    c = 1 + 2j          # complex
    print(f"--- Numeric Types ---")
    print(f"{a} is {type(a)}")
    print(f"{b} is {type(b)}")
    print(f"{c} is {type(c)}\n")

    # 2. Sequence Types
    s = "Hello Python"  # str
    l = [1, 2, 3, "Hi"] # list (mutable)
    t = (1, 2, 3, "Hi") # tuple (immutable)
    r = range(5)        # range
    print(f"--- Sequence Types ---")
    print(f"'{s}' is {type(s)}")
    print(f"{l} is {type(l)}")
    print(f"{t} is {type(t)}")
    print(f"{list(r)} is {type(r)}\n")

    # 3. Mapping Type
    d = {"name": "Alice", "age": 25} # dict
    print(f"--- Mapping Type ---")
    print(f"{d} is {type(d)}\n")

    # 4. Set Types
    st = {1, 2, 2, 3}   # set (unordered, unique elements)
    fst = frozenset({1, 2, 3}) # frozenset (immutable set)
    print(f"--- Set Types ---")
    print(f"{st} is {type(st)}")
    print(f"{fst} is {type(fst)}\n")

    # 5. Boolean Type
    is_active = True    # bool
    print(f"--- Boolean Type ---")
    print(f"{is_active} is {type(is_active)}\n")

    # 6. None Type
    empty = None        # NoneType
    print(f"--- None Type ---")
    print(f"{empty} is {type(empty)}")

if __name__ == "__main__":
    demonstrate_data_types()
