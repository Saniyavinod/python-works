f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\File_programs\\students.txt","r")

students=[]

for stud in f:
    students.append(stud.rstrip("\n"))
print(students)    