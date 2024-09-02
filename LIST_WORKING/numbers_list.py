number=[10,11,12,34,43,54,19,78,42]


#print no:of object in numbers

count_number=len(number) 

sum_odd=0

sum=0

print(f"count of given string is {count_number}")

for i in range(0,count_number):


    sum=sum+number[i]

    if number[i]%2==0:
        print(number[i])


    if number[i]%2!=0:
        sum_odd=sum_odd+number[i]



print(f"total of the given list: {sum}")

print(f"sum of odd number is: {sum_odd}")
    



# print total  of numbers        

