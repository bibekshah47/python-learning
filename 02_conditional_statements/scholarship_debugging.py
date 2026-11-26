# Problem: University Scholarship System
# A university awards scholarships based on the following requirements:
# - The student must have a GPA of at least 3.5.
# - The student must have completed at least 30 credits.
# - The student must not be on academic probation.
# - Eligible students with a GPA of 3.8 or higher receive a $5,000 scholarship.
# - Other eligible students receive a $2,000 scholarship.
# - Ineligible students receive no scholarship

gpa = float(input("Enter your GPA: "))
credits = int(input("Enter completed credits: "))
on_probation = False

if gpa >= 3.5 and credits >= 30 and not on_probation:
    if gpa >= 3.8:
        print("Scholarship: $5000")
    else:
        print("Scholarship: $2000")
else:
    print("Not eligible for scholarship")