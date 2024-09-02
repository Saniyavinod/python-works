words=["hello","hai","hello","hello"]


# count=words.count("hello")
# print(f"hello:{count}")

# count_hi=words.count("hai")
# print(f"hii:{count_hi}")
word_count={}
for w in words:
    if w in word_count:
        word_count[w]=word_count[w]+1
    else:
        word_count[w]=1
print(word_count)        