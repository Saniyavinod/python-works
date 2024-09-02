arr=[
    [10,20],
    [21,30],
    [40,53]
]

even=[num for lst in arr for num in lst if num%2==0]

print(even)


sum_of_number=[num for lst in arr for num in lst]

print(sum(sum_of_number))

number=[num for lst in arr for num in lst if num>15]
print(number)