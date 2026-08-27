# Parent class
class person:
    def details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name :" , self.name)
        print("age :" , self.age)

# Child class
class student(person):
    def stud_details(self,div):
        self.div=div

    def stud_display(self):
        print("div" , self.div)

# Create an instance of the child class
s1 = student()
s1.details("vidit" , 19)
s1.display()
s1.stud_details("SY1")
s1.stud_display()









#--------------------------- (1 parent and 2 child class inheritance) -----------------------------------------
# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child Class 1
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print("\n----- Employee Details -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Child Class 2
class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


# -------- Employee Input --------
print("Enter Employee Details")
name = input("Enter Name: ")
age = input("Enter Age: ")
employee_id = input("Enter Employee ID: ")
salary = input("Enter Salary: ")

emp = Employee(name, age, employee_id, salary)
emp.display_employee()


# -------- Student Input --------
print("\nEnter Student Details")
name = input("Enter Name: ")
age = input("Enter Age: ")
roll_no = input("Enter Roll No: ")
course = input("Enter Course: ")

stu = Student(name, age, roll_no, course)
stu.display_student()