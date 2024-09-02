

words = ["fly", "float", "flower", "flat"]


smallest_word = words[0]

for ch in words:
    if len(ch) < len(smallest_word):
        smallest_word = ch
        
common_prefix=smallest_word
for ch in words:
    while not ch.startswith(common_prefix):
        common_prefix=common_prefix[:-1]    #slice the word [start:end:]    [0:5]it print upto index position 0 to 5  #[:-1] cut the last letter
        
                        
        
    if not common_prefix:
        print("no common prefix")
        break
print(common_prefix)                      
                                        
        





