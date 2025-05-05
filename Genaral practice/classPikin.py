

class Person:
    def __init__(self, name: str, age: int):
    	self.name = name
    	self.age = age    
    def __str__(self):
    	return f"{self.name} is {self.age} years old."
        
P1 = Person("Charleson", 25)

print(P1)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        return("My name is " + self.name)
p1 = person("Charleson", 25)
print(p1.myFunc())
