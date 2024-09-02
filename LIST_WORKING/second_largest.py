num=[14,4,8,5,9,10,11,12,1,13]
largest_num=0
second_largest=0

for i in num:

    if i>largest_num and i > second_largest :

        second_largest=largest_num
        largest_num=i

    elif i>second_largest and i!=largest_num:

        second_largest=i    
print(f"second largest number from the list is..{second_largest}")