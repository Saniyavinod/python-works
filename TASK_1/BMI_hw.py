height=int(input("Enter the height of user in cm="))

weight=int(input("Enter the weight of user in kg="))

height_in_meter=height/100

BMI=weight/height_in_meter**2

print(f"BMI={BMI}")