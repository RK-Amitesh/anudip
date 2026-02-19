# Hospital Emergency Triage System

# taking inputs
age = int(input("Enter patient's age: "))
heart_rate = int(input("Enter heart rate: "))
severe_injury = input("Is there a severe injury? (yes/no): ")

# checking condition

# Critical condition
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    print("Category: CRITICAL")

# Moderate condition
elif heart_rate >= 60 and heart_rate <= 100:
    category = "Moderate"
    
    # upgrade rule for senior citizens
    if age > 65:
        print("Category: CRITICAL (Upgraded due to senior age)")
    else:
        print("Category: MODERATE")

# Normal condition
else:
    print("Category: NORMAL")
