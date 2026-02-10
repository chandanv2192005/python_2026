import re

def check_password_complexity(password):
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters long.")
        return 0

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = 0
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    print(f"Password Strength: {score}/4")
    if score == 4:
        print("Strong password! Great job.")
    elif score == 3:
        print("Moderate password. Consider adding more complexity.")
    elif score == 2:
        print("Weak password. Add uppercase, lowercase, numbers, and special characters.")
    else:
        print("Very weak password. Please choose a stronger password.")

    return score

def main():
    print("--- Password Complexity Checker ---")
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        check_password_complexity(password)

if __name__ == "__main__":
    main()
