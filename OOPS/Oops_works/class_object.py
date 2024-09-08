class student:
    name: str
    id: int
    gender: str  # Changed from int to str
    address: str
    age: int

    def __init__(self, name, id, gender, address, age):
        self.name = name
        self.id = id
        self.gender = gender
        self.address = address
        self.age = age

    def display_student(self):  # Corrected indentation
        print(self.name, self.id, self.gender, self.address, self.age)


# Create object
student_instance = student("saniya", 6, "female", "hhh", 89)


student_instance.display_student()  # Call the display_student method to show student details



