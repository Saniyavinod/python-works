

from re import fullmatch

text=input("passport number: ")

pattern="[A-Z]{1}[0-9]{1}[0-9]{1}[0{1}|\\s{1}][0-9]{4}[1-9]{1}"

matcher=fullmatch(pattern,text)

if matcher==None:
    print("invalid")
else:
    print("valid")    