from random import randrange

randNumber = randrange(1, 100)

if(randNumber == 100):
    print("Congrats u won a ferrari")

else:
    print("ggs try again")

class Animals:
    alive = True
    
class Dog(Animals):
    def speak(self):
        print("woof woof")
        
class Cat(Animals):
    def speak(self):
        print("meoooooooooow")
        
class Car:
    def Horn(self):
        print("meep meep")
        
animals = [Dog(), Cat()]
        
for animal in animals:
    animal.speak()