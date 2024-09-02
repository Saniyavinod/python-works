from re import finditer

text="abc27383bdh998hs8882dbj"

# pattern="[a-z]{3}"  #{} will check the limit 


# pattern="[c-ht-z]"

#c-h or t-z

# pattern="([c-h]|[t-z])"

pattern="([a-z]{3}|[0-9]{3})"



matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())