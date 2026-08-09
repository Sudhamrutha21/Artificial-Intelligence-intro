# Age Eligibility Checker
# Demonstrates variables, data types, and operators
# Used in AI systems for age-based services

print("=" * 50)
print("AI AGE ELIGIBILITY CHECKER")
print("=" * 50)

# Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

# Data Types
age_int = age
age_str = str(age)  # Type conversion
name_upper = name.upper()  # String operation

# Eligibility Checks using Operators
can_vote = age >= 18
can_drive = age >= 16
can_rent_car = age >= 21
can_retire = age >= 62
is_senior = age >= 60
is_youth = 18 <= age <= 30
is_child = age < 13
is_teen = 13 <= age <= 19

# Display Results
print("\n" + "=" * 50)
print("ELIGIBILITY REPORT")
print("=" * 50)
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Country: {country}")

print("\n" + "-" * 50)
print("ELIGIBILITY CHECK")
print("-" * 50)

# Using logical and comparison operators
if can_vote:
    print("✅ Can Vote: Yes")
else:
    print(f"❌ Can Vote: No (Need {18 - age} more years)")

if can_drive:
    print("✅ Can Drive: Yes")
else:
    print(f"❌ Can Drive: No (Need {16 - age} more years)")

if can_rent_car:
    print("✅ Can Rent Car: Yes")
else:
    print(f"❌ Can Rent Car: No (Need {21 - age} more years)")

if can_retire:
    print("✅ Can Retire: Yes")
else:
    print(f"❌ Can Retire: No (Need {62 - age} more years)")

# AI Recommendation
print("\n" + "-" * 50)
print("AI RECOMMENDATIONS")
print("-" * 50)

if is_child:
    print("🔹 Category: Child")
    print("🔹 Recommendation: Focus on education and play")
elif is_teen:
    print("🔹 Category: Teenager")
    print("🔹 Recommendation: Explore career options and build skills")
elif is_youth:
    print("🔹 Category: Young Adult")
    print("🔹 Recommendation: Start career, save money, plan future")
elif is_senior:
    print("🔹 Category: Senior Citizen")
    print("🔹 Recommendation: Health checkups, enjoy retirement")
else:
    print("🔹 Category: Adult")
    print("🔹 Recommendation: Balance work, family, and personal growth")

print("=" * 50)