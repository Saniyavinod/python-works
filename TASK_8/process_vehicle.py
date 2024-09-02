
from re import fullmatch

# Open the input file for reading
f = open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\TASK_8\\vehicle.txt", "r")

# Define the pattern for valid vehicle numbers (using raw string for clarity)
pattern = r"(KL)\s[0-9]{2}\s[A-Z]{1,2}\s[0-9]{4}"

# Open the output file for appending
out_file = open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\TASK_8\\write.txt", "a")

# Iterate through each line in the input file
for line in f:
    register = line.rstrip("\n")
    matcher = fullmatch(pattern, register)

    if matcher !=None:
        print(register)
        out_file.write(register + "\n")




