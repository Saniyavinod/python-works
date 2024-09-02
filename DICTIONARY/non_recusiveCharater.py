text="ABABCDE"

word_count={}
for i in text:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
        
print(word_count)

for k,v in word_count.items():
    if v==1:
        print(k)

   

