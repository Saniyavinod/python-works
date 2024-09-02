# Read height and weight from the user
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kilograms: "))
height_in_meter=height/100
# Calculate BMI
bmi = weight / (height_in_meter ** 2)

# Determine the weight category based on BMI
if bmi <= 19:
    category = "Underweight"
elif  bmi <=25:
    category = "Normal weight"
elif bmi <= 30:
    category = "Overweight"
else:
    category = "Obesity"

# Print the BMI and weight category
print(f"Your BMI is: {bmi:.2f}")
print(f"Weight category: {category}")
