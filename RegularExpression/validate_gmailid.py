from re import fullmatch
email_id=input("enter the email.id: ")

pattern="\\w[\\w\\._]*@gmail.com"

matcher=fullmatch(pattern,email_id)

print("invalid" if matcher==None else "valid")

# if fullmatch==None:
#     print("invalid")
# else:
#     print("valid")    

# + one or more

# ? optional

# * zero or more