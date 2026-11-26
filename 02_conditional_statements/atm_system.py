# Problem: ATM Withdrawal System
# Lesson: 1.6 - Conditional Statements
# Difficulty: Hard

correct_pin = 1234
balance = 1000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    withdrawal_amount = int(input("Enter withdrawal amount: "))

    if withdrawal_amount <= 0:
        print("Invalid amount")
    elif withdrawal_amount > balance:
        print("Insufficient balance")
    elif withdrawal_amount % 20 == 0:
        print("Withdrawal successful")
        balance = balance - withdrawal_amount
        print("Remaining balance: $", balance, sep="")
    else:
        print("Withdrawal must be a multiple of $20")
else:
    print("Incorrect PIN")

# Key learnings:
# 1. Nested conditional statements.
# 2. Validating conditions in the correct order.
# 3. Using modulo to check divisibility.
# 4. Updating variables after a transaction.
# 5. Handling boundary cases.