num=int(input("enter the number:"))

result=0

orginal=num

while(num!=0):

    digit=num%10

    result=result*10+digit

    num=num//10

if orginal==result:
    print(f"{orginal} is palindrom") 

else:

    print(f"{orginal} is not palindrom")    