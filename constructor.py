class student:

    def __init__(self,name,id):
        print("MIT ADT")
        self._name=name
        self.id=id
    
    def display(self):
        print ("welcome")
        print(self._name)
        print(self.id)

s1=student("vidit", 5566)
s1.display()
print(s1._name)

