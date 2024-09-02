
from re import fullmatch

f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\RegularExpressionPeriod\\domain.txt","r")
pattern="[\w\W]+\\.com"
for mail in f:
    domain=mail.rstrip("\n")
    
    matcher=fullmatch(pattern,domain)

    if matcher!=None:
        print(domain)