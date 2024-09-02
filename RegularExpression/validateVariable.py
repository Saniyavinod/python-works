from re import fullmatch

variable=input("enter the variable name ")

pattern="[a-zA-Z][a-zA-Z0-9_]*"


matcher=fullmatch(pattern,variable)


if matcher==None:
    print("invalid")
else:
    print("valid")    