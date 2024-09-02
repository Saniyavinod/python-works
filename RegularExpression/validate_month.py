# from re import fullmatch                #month

# num="01"

# pattern="(0?[1-9]|1[0-2])"

# matcher=fullmatch(pattern,num)

# if matcher==None:
#     print("invalid")
# else:
#     print("valid")    


#date 0-31
from re import fullmatch

date=""

pattern="(0?[1-9]|1[0-9|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,date)

if matcher==None:
    print("invalid")
else:
    print("valid")    