text="pneumonoultramicroscopicsilicovolcanoconiosis"

vowels="aeiou"

vowel_count=0

c_count=0

for ch in text:

    if vowels.count(ch)!=0:

        vowel_count+=1

    else:

        c_count+=1

print(vowel_count)    

print(c_count)

