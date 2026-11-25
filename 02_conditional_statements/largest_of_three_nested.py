# Problem: Largest of Three Numbers
# Difficulty: Medium
# Approach: Nested conditional statements
# Restrictions: No and, or, or max()

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3= int(input("Enter your third number: "))

if num1>=num2:
    if num1>=num3:
        print("Largest number:", num1)
    else:
        print("Largest number:", num3)

else:
    if num2>=num3:
        print("Largest number:", num2)
    else:
        print("Largest number:", num3)


# Key learnings:
# 1. Breaking a problem into smaller decisions.
# 2. Translating a flowchart into Python code.
# 3. Covering every possible decision path.
# 4. Solving the same problem using different approaches.