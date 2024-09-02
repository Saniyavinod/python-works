from json import load

f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\jsonWorking\\filims.json")

movies=load(f)

for m in movies:
    print(m.get("title"))