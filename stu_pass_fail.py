# Student Pass/Fail Predictor
# This program demonstrates variables, data types, and operators
# Used in AI systems for educational performance prediction

# Variables and Data Types
student_name = "Aisha Khan"           # String
student_id = 2024001                  # Integer
marks_obtained = 72.5                 # Float
is_passing = True                     # Boolean

# User Input
print("=" * 50)
print("STUDENT PERFORMANCE PREDICTOR")
print("=" * 50)

name = input("Enter student name: ")
marks = float(input("Enter marks obtained (0-100): "))
total_marks = float(input("Enter total marks: "))

# Operators: Arithmetic, Comparison, Logical
percentage = (marks / total_marks) * 100    # Arithmetic Operator

# Comparison and Logical Operators
if percentage >= 40 and marks >= 0:          # Logical AND, Comparison
    status = "PASS"
    is_passing = True
elif percentage >= 35 and percentage < 40:
    status = "SUPPLEMENTARY"
    is_passing = False
elif percentage >= 0 and percentage < 35:
    status = "FAIL"
    is_passing = False
else:
    status = "INVALID MARKS"
    is_passing = False

# Display Results
print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)
print(f"Student Name: {name}")
print(f"Marks Obtained: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Status: {status}")
print(f"Passing Status: {is_passing}")
print("=" * 50)