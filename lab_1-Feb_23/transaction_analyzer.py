"""
Program: Bank Transaction Analyzer
---------------------------------
- Calculate total balance
- Find largest withdrawal
- Count deposits > 10000
"""

def analyze_transactions(transactions):
    total_balance = sum(transactions)

    withdrawals = [t for t in transactions if t < 0]
    largest_withdrawal = min(withdrawals) if withdrawals else 0

    large_deposits = len([t for t in transactions if t > 10000])

    return total_balance, largest_withdrawal, large_deposits


transactions = [20000, -5000, 15000, -2000, 8000]

balance, largest_wd, big_deposits = analyze_transactions(transactions)

print("Net Balance:", balance)
print("Largest Withdrawal:", largest_wd)
print("Deposits > 10000:", big_deposits)