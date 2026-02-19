# Smart Login System

# correct credentials (stored values)
correct_username = "admin"
correct_password = "12345"

attempts = 0

while attempts < 3:
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # checking credentials
    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Invalid credentials. Please try again.")
        print("Attempts remaining:", 3 - attempts)

# if 3 attempts failed
if attempts == 3:
    print("Account Locked. Too many failed attempts.")