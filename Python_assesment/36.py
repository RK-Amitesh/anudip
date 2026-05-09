# Q36. Create an ATM simulation program
# that repeatedly asks for PIN validation
# and locks the account after three invalid attempts.

correct_pin = "1234"

attempts = 0

while attempts < 3:

    pin = input("Enter ATM PIN : ")

    # checking pin
    if pin == correct_pin:

        print("Login Successful")
        break

    else:

        attempts = attempts + 1

        print("Invalid PIN")

        remaining = 3 - attempts

        if remaining > 0:

            print("Attempts Left =", remaining)

# account lock
if attempts == 3:

    print("Account Locked Due to 3 Invalid Attempts")