text="hello hai hello hai hello"

split=text.split(" ")

word_count={}

for w in split:
    if w in word_count:
        word_count[w]+=1

    else:
        word_count[w]=1    

print(word_count)        