num=int(input("enter the number:"))

org=num

sum=0

digit_count=len(str(num))

while (num!=0):
    
    digit=num%10

    exponent=digit**digit_count

    sum=sum+exponent

    num=num//10
print(sum)    

if sum==org:
    print("number is armstrong")
else:
    print("number is not armstrong")    
