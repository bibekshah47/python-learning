# Problem: Student Exam Result System
# Lesson: 1.6 - Conditional Statements
# Difficulty: Medium

# Requirements:
# 1. Attendance must be at least 75%.
# 2. Determine the grade based on the exam score.
# 3. Always display the completion message.

attendance = float(input("Enter your attendance percentage: "))
exam_score = float(input("Enter your exam score: "))

if attendance < 75:
    print("Not eligible for exam")
else:
    if exam_score >= 90:
        print("Grade A")
    elif exam_score >= 80:
        print("Grade B")
    elif exam_score >= 70:
        print("Grade C")
    elif exam_score >= 60:
        print("Grade D")
    else:
        print("Failed")

print("Result processing complete")

# Key learnings:
# 1. Nested conditional statements.
# 2. Using if, elif, and else.
# 3. Importance of indentation.
# 4. Checking conditions in the correct order.
# 5. Converting user input using float().