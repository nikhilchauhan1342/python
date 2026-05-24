# Question 1 — ATM Withdrawal Validator

balance = float(input("Enter your current balance: "))
daily_withdrawn = float(input("Enter amount already withdrawn today: "))
amount = float(input("Enter withdrawal amount: "))

if daily_withdrawn >= 50000:
    print("Daily withdrawal limit reached.")

elif amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

elif amount > balance:
    print("Insufficient balance.")

elif daily_withdrawn + amount > 50000:
    print("Daily withdrawal limit reached.")

else:
    balance = balance - amount
    print("Withdrawal successful.")
    print("Your current balance after withdrawal: NPR", balance)

