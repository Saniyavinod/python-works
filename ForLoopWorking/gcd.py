num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))

gcd=1 

for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(i)        




