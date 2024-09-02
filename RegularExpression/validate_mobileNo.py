from re import fullmatch
mobile_no="91 8281650741"
pattern="(91)(\\s)?[6-9][0-9]{9}"

matcher=fullmatch(pattern,mobile_no)

if matcher==None:
    print("invalid")
else:
    print("valid")    