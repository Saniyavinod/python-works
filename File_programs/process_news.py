f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\File_programs\\new.txt","r")
word_list=[]
for line in f:
    words=line.strip("\n").split(" ")
    
    

    for w in words:
        if w!="":
            word_list.append(w)
        
print(word_list)       

word_count={}

for w in word_list:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)        

def get_value(key):
    return word_count.get(key)
sort=sorted(word_count,key=get_value,reverse=True)
print(sort) 