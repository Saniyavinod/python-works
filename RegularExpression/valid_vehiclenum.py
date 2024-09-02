#kerala vehicle registration number validation

#starting with KL
#two digit
#aplhabets(1 or 2)
#4 digits

from re import fullmatch

vehicle_number="KL-08-BN-4970"

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vehicle_number)

if matcher==None:
    print("invalid")

else:
    print("valid")    