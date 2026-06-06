class Animal: 
    def __init__(self,name):
      self.name = name
      self.is_alive = True  

    def eat(self): 
       print(f"{self.name} is eating")

    def sleep(self):
       print(f"{self.name} is sleeping")

class Dog(Animal):
   def speak(self): 
      print("WOOF")

class Cat(Animal):
  def speak(self): 
      print("Meow")


class mouse(Animal):
   def speak(self): 
      print("SQUEEK")


dog = Dog("Scooby")
cat = Cat("Garfield")
Mouse = mouse("Mickey") 

print(dog.name)
print(cat.name)
print(Mouse.is_alive) 
dog.speak()
cat.eat()
Mouse.speak()




