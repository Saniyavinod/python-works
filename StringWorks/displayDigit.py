word="i have 3 bike and 1 car"

for ch in word:
    if(ch.isalpha()):

        print(ch,end=",")

print("\n printing digits ")        


for ch in word:
    if(ch.isdigit()):

        print(ch,end=",")
