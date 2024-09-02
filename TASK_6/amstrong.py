numbers = [151,153,154,370,371,372,373,16341,1635]

for num in numbers:
    org = num  # original number
    sum = 0
    digit_count = len(str(num))  # count of digits in the number
    
    current_num = num
    while current_num > 0:
        digit = current_num % 10
        sum += digit ** digit_count
        current_num =current_num//10
    
    if sum == org:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
