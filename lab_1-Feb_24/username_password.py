# Problem 16
# Validate username and password

# Taking username input
username = input("Enter username: ")
# Stored as string

# Taking password input
password = input("Enter password: ")
# Stored as string

# ---------------- USERNAME VALIDATION ----------------

# Check minimum length and alphanumeric condition
if len(username) < 5:
    # Username must be at least 5 characters
    print("Invalid Username: Must be at least 5 characters long.")

elif not username.isalnum():
    # isalnum() checks if string contains only letters and numbers
    print("Invalid Username: Only letters and numbers allowed.")

# ---------------- PASSWORD VALIDATION ----------------

elif len(password) < 8:
    # Password must be at least 8 characters
    print("Invalid Password: Must be at least 8 characters long.")

else:
    # Initialize flags for password conditions
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Loop through each character in password
    for ch in password:

        if ch.isupper():
            # Check for uppercase letter
            has_upper = True

        elif ch.islower():
            # Check for lowercase letter
            has_lower = True

        elif ch.isdigit():
            # Check for digit
            has_digit = True

        else:
            # If not letter or digit → special character
            has_special = True

    # Final validation check
    if has_upper and has_lower and has_digit and has_special:
        print("Username and Password are Valid.")
    else:
        print("Invalid Password: Must contain uppercase, lowercase, digit, and special character.")