vehicle_numbers=[
    "KL58B2367"
    "KL58023"
    "K58B236"
    "58B2367"
    "KL5"
    ]

f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\File_programs\\vehicle_numbers.txt","w")

for veh in vehicle_numbers:
    f.write(veh+"\n")