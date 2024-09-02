arr=[10,11,12,13,14,15,16,17]
# length=len(arr)
# list=[]
# for i in range(0,length):
#     n=arr[i]
#     if n%2!=0:
#         list.append(n)
# reversed_arr=list[::-1]
# print(reversed_arr)



left=1
length=len(arr)-1
if length%2!=0:
    right=length

else:
    right=length-1

while(left<right):
    (arr[left],arr[right])=(arr[right],arr[left])

    left=left+2
    right=right-2
print(arr)       