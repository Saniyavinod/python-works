
from re import finditer

text="a 293 @455#b839,H003+j"

# pattern="[ahj8]"   check either a,h,j or 8

# pattern="[a-z]"

# pattern="[A-Z]"

# pattern="[a-zA-Z]"

# pattern="[0-9]"      \d  ,exclude\D

#pattern="[a-zA-Z0-9]"

# pattern="[^a-zA-Z]"

# pattern="[^0-9]"

# pattern="[\s]"  #chech for space

pattern="[^a-zA-Z0-9\s]"

matcher=finditer(pattern,text)

for m in matcher:
    
    print(m.start(),"===",m.group())
