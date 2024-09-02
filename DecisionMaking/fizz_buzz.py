num=int(input("enter the number:"))

# if num%15==0:
#     print(f"enter {num} is fizzbuzz")


# elif num%5==0:
#     print(f"enter {num} is buzz")

# elif num%3==0:
#     print(f"enter {num} is fizz")

# else:
#     print("invalid")        

result=""

if num%3==0:
    result=result+"fizz"

if num%5==0:
    result=result+"buzz"

print(result)    
