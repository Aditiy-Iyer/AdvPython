class Organization:
    def set_data(self, org):
        self.org = org

class Department:
    def set_name(self, dep, code):
        self.dep = dep
        self.code = code

class student(Department, Organization):
    def get_data(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f'Student ID:{self.code}{self.id} \nStudent name: {self.name}\nDepartment: {self.dep}\n{self.org}')

stu1 = student()
stu1.get_data(1101," Aditiy Nagarajan Iyer ")
stu1.set_name("Bioengineering", "MITU19IMBI")
stu1.set_data("MIT ADT University")
stu1.display()


