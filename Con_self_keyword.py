class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        
        print("Cat Mewing")


animal = Animal() 
animal.sound() 
dog = Dog() 
dog.sound() 
cat = Cat()   
cat.sound() 
        
   