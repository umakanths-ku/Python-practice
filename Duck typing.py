class Animal:#Another way of implementing polymorphism.. Duck typing...
    alive = True 

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meow!") 

class Car:#do make sound but is not not an animal..
    alive = False
    def speak(self):
        print("HONK!")        

animals = [Dog(),Cat(),Car()] 

for animal in animals:
    animal.speak()
    print(animal.alive)
