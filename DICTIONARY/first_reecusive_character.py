text="ABCCDD"


length=len(text)
value=False

for i in range(0,length):
    for j in range(i+1,length):
        if text[i]==text[j]:
            
            print(text[i])
            value=True
            break
    if value==True:
        break       


# seen=set()

# for char in text:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)



word_count={}
for i in text:  #A:1
    if i in word_count:
        print(i) 
        break
    else:
        word_count[i]=1