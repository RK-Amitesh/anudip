#program to detect suspicious banking transactions

# input of transaction amount
amount = float(input("Enter transaction amount:"))
account_age = int(input("Enter account age in months: "))
transaction_type = input("Is the transaction international? (yes/no):")

# validating whether transaction amount is valid or not
if(amount > 200000 and account_age < 6 and transaction_type == "yes"):
    print("Transaction Flagged for Manual Verification")
else:
    print("Transaction is normal")