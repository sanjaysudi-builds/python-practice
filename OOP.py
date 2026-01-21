#OOP Concepts 
#Small programs using Classes,objects,Method,constructor and self keyword.

1)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

person1 = Person("Arjun",22)
person1.introduce()

2)

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: {self.price}")


laptop1 = Laptop("Dell", 30000)
laptop2 = Laptop("HP", 40000)

laptop1.show_info()
laptop2.show_info()

3)

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")
greet("Bob", "Good Morning")
  
                 