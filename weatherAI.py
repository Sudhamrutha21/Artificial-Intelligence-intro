# Temperature Converter for Weather AI
# Demonstrates variables, data types, operators, and user input
# Used in weather prediction systems

print("=" * 50)
print("WEATHER AI - TEMPERATURE CONVERTER")
print("=" * 50)

# Display conversion options
print("\nSelect conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

# User Input
choice = input("\nEnter your choice (1-4): ")

# Variables
temp_input = float(input("Enter temperature value: "))
converted_temp = 0.0
unit_from = ""
unit_to = ""

# Using operators for conversion
if choice == "1":
    # C to F: (C × 9/5) + 32
    converted_temp = (temp_input * 9/5) + 32
    unit_from = "°C"
    unit_to = "°F"
elif choice == "2":
    # F to C: (F - 32) × 5/9
    converted_temp = (temp_input - 32) * 5/9
    unit_from = "°F"
    unit_to = "°C"
elif choice == "3":
    # C to K: C + 273.15
    converted_temp = temp_input + 273.15
    unit_from = "°C"
    unit_to = "K"
elif choice == "4":
    # K to C: K - 273.15
    converted_temp = temp_input - 273.15
    unit_from = "K"
    unit_to = "°C"
else:
    print("Invalid choice!")
    exit()

# Display Results
print("\n" + "=" * 50)
print("CONVERSION RESULT")
print("=" * 50)
print(f"{temp_input:.2f}{unit_from} = {converted_temp:.2f}{unit_to}")

# AI Prediction based on temperature
print("\n" + "=" * 50)
print("WEATHER PREDICTION")
print("=" * 50)

if unit_to == "°F" or unit_to == "°C":
    temp_check = converted_temp if unit_to == "°C" else (converted_temp - 32) * 5/9
    
    if temp_check > 35:
        prediction = "Extremely Hot - Heatwave warning!"
    elif 25 < temp_check <= 35:
        prediction = "Hot - Perfect for beach activities"
    elif 15 < temp_check <= 25:
        prediction = "Mild and Pleasant"
    elif 5 < temp_check <= 15:
        prediction = "Cool - Carry a light jacket"
    elif -5 < temp_check <= 5:
        prediction = "Cold - Heavy jacket required"
    else:
        prediction = "Freezing! Stay indoors!"

    print(f"Temperature: {converted_temp:.1f}{unit_to}")
    print(f"AI Suggestion: {prediction}")

print("=" * 50)