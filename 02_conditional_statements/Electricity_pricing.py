# Problem: Electricity Bill Calculator
# Difficulty: Medium
# Lesson: Conditional Statements

num_of_units = int(input("Enter number of units consumed: "))
price = 0

if num_of_units < 0:
    print("Invalid number of units")

else:
    # Calculate electricity bill
    if num_of_units > 200:
        price = 100 * 0.50 + 100 * 0.75 + (num_of_units - 200) * 1.20

    elif num_of_units >= 100:
        price = 100 * 0.50 + (num_of_units - 100) * 0.75

    else:
        price = num_of_units * 0.50

    # Apply 10% surcharge
    if price > 150:
        price = price + price * 0.10

    # Display final bill
    print("Final electricity bill: $", round(price, 2), sep="")