# Read three numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1>num2 and num1>num3:
    if num2>num3:
        print(f"second largest is {num2}")
    else:
        print(f"second largest is {num3}")    

if num2>num1 and num2>num3:
    if num1>num3:
        print(f"sec ond largest is {num1}")
    else:
        print(f"second largest is {num3}")

if num3>num1 and num3>num2:
    if num1>num2:
        print(f"second largest is {num1}")
    else:
        print(f"second largest is {num2}")             

