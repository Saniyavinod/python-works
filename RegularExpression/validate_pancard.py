#first 3 char are alphabets
#4th char with be (PCAFHT)
#5th place one alphabet
#6th 4 digits
#1 alphabet

from re import fullmatch

text=input("enter the PAN NO: ")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-z]{1}"

matcher=fullmatch(pattern,text)

if matcher==None:
    print("invalid")

else:
    print("valid")    