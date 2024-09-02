numbers=[10,11,12,13,14,20,21]

def is_prime(n):
    if n <2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True
        
for num in numbers:
    if is_prime(num):
        print(num)        