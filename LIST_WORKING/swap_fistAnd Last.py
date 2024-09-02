num=[1,2,3,4,5,6,7]

# num[-1],num[0]=num[0],num[-1]

first=num.pop(0)
second=num.pop(-1)
num.insert(0,second)

num.append(first)

print(num)

# print(num)
