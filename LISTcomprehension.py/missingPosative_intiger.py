# 1st method

arr=[0,1,2,3]

n=len(arr)

sum_of_n=n*(n+1)/2

current_sum=sum(arr)

missing_number=sum_of_n-current_sum

print(missing_number)

#2nd method
# previous,current

arr = [0, 1, 2, 3]

# Step 1: Sort the array
arr.sort()

# Step 2: Initialize the previous and current variables
previous = 0
current = 1

# Step 3: Iterate through the sorted array
for num in arr:
    if num == current:
        # If num matches current, move to the next integer
        previous = current
        current += 1
    elif num > current:
        # If num is greater than current, we've found a missing integer
        break

print("The smallest missing positive integer is:", current)


