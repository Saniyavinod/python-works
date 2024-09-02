from re import fullmatch

variable=input("enter variable name:")

pattern="[k-m][0369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,variable)

if matcher==None:
    print("invalid")

else:
    print("valid")    