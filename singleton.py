class printer:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            print("creating printer.......")
            cls._instance=super().__new__(cls)

        return cls._instance
    
p1=printer()
p2=printer()
p3=printer()

print(id(p1))
print(id(p2))
print(id(p3))