#-------------------------- HYBRID INHERITANCE---------------------------

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child class 1 (inherits Person)
class Employee(Person):
    def __init__(self, name, age, salary, employee_id):
        Person.__init__(self, name, age)
        self.salary = salary
        self.employee_id = employee_id


# Child class 2 (inherits Person)
class Department(Person):
    def __init__(self, name, age, department):
        Person.__init__(self, name, age)
        self.department = department


# Manager inherits from Employee and Department
class Manager(Employee, Department):
    def __init__(self, name, age, salary, employee_id, department):
        Employee.__init__(self, name, age, salary, employee_id)
        Department.__init__(self, name, age, department)

    def display_details(self):
        print("\n----- Manager Details -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)


# User Input
name = input("Enter Name: ")
age = input("Enter Age: ")
salary = input("Enter Salary: ")
employee_id = input("Enter Employee ID: ")
department = input("Enter Department: ")

# Create Object
manager1 = Manager(name, age, salary, employee_id, department)

# Display Details
manager1.display_details()

