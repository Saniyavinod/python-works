source_words="CHICKEN"

target_word="HHEN"

word_count={}

for ch in source_words:

    if ch in word_count:

        word_count[ch]+=1

    else:

        word_count[ch]=1

print(word_count)

is_kangarooword=True

for ch in target_word:
    
    if ch in word_count and word_count.get(ch)>0:            
                                                                                        
         
        word_count[ch]=word_count[ch]-1                            #after finding the word count we have 2 conditions
                                                                                                                                 
    else:                                                            # 1. we need to check the target_word is present in word_count

        is_kangarooword=False                                         #  2. and also check the count value is greater then 0
        
        break                                                        #   if the two condition is true we need to minus 1 from the word_count[ch]
                                                          
print(is_kangarooword)                                               # else if any of the condition uis false the target_wordis not kangaroo word
         
