# num=int(input("enter the number:"))

# pre=0
# current=1
# isFibo=False


# if num in (0,1):

#     isFibo=True
# else:
#     next=pre+current


#     while(next<=num):

#         next=pre+current

    
    
#         previous=current      #p=1      p=1

#         current=next        #c=1       c=2

#         if next==num:

#             isFibo=True

#             break

# print(isFibo)    


num = int(input("Enter the number: "))

pre = 0
current = 1
isFibo = False

if num == 0 or num == 1:
    isFibo = True
else:
    next = pre + current

    while next <= num:
        if next == num:
            isFibo = True
            break

        # Update variables to the next Fibonacci numbers
        pre = current
        current = next
        next = pre + current

print(isFibo)





    

