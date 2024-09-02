year=1800
print("leap year from 1800 to 2024 is:")
i=year
while(i<=2024):
    if (i%100==0 and i%400==0) or (i%100!=0 and i%4==0):
        print(i)
    i=i+1    
