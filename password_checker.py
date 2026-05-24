# Question 4 — Password Strength Checker

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_characters = "!@#$%^&*"

for password in passwords:

    print("\nChecking password:", password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    if len(password) < 8:
        print("Password is weak.")
        print("Missing: Minimum 8 characters")

    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True

    if not has_upper:
        print("Missing uppercase letter")

    if not has_lower:
        print("Missing lowercase letter")

    if not has_digit:
        print("Missing digit")

    if not has_special:
        print("Missing special character")

    if (
        len(password) >= 8
        and has_upper
        and has_lower
        and has_digit
        and has_special
    ):
        print("Strong password")
