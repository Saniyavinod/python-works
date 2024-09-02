def nth_digit_max(n1,n2):

    f=n1%10
    s=n2%10

    if f>s:
        return n1 
    else:
        return n2
    
print(nth_digit_max(123,127))   



# def nth_digit_max(n1,n2):


#     return n1 if n1%10 > n2%10 else n2

# print(nth_digit_max(127,134))