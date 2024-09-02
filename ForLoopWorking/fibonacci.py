num=int(input("enter the number:"))


previous=0
current=1

print(f"{previous},{current}",end=",")

for i in range(1,num+1):
    next=previous+current      #p=0+1
    previous=current      #p=1      p=1

    current=next         #c=1       c=2
    print(f"{next}",end=",")     #0,1,1,2,3



