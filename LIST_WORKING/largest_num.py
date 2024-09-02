num=[1,2,3,9,6,4]

# largest_num=num[0]

# for i in num:

#     if i>largest_num:

#         largest_num=i

# print(f"largest number from the list is..{largest_num}")        

# num=[1,2,3,9,6,4]

largest_num=num[0]
second_largest=num[0]

for i in num:

    if i>largest_num and i > second_largest :

        second_largest=largest_num
        largest_num=i

        
print(f"second largest number from the list is..{second_largest}")