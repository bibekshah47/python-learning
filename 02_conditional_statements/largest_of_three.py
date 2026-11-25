# Problem
# Write a Python program that asks the user to enter three integers and displays the largest number.
# Requirements
# - Use input() and type conversion.
# - Use conditional statements and logical operators.
# - Do not use the built-in max() function.
# - Handle negative numbers and equal numbers correctly.

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3= int(input("Enter your third number: "))

if num1>=num2 and num1>=num3:
    print("Largest number:", num1)

elif num2>=num1 and num2>=num3:
    print("Largest number:", num2)

else:
    print("Largest number:", num3)

# Key learnings:
# 1. Use >= instead of > when equal values are possible.
# 2. Use int() when the problem requires integers.
# 3. Valid syntax does not guarantee correct logic.
# 4. Always test negative numbers and equal values.