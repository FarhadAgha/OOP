#This is the Base/Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        pass  
    def info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"
        
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture"

dog = Dog("puppy", 3)
cat = Cat("kitten", 2)

print(dog.info())        
print(dog.speak())       
print(dog.fetch())       

print(cat.info())        
print(cat.speak())       
print(cat.scratch())    
