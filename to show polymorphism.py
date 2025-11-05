class Animal: 
    def make_sound(self): 
        print("Some generic animal sounds") 

class Dog(Animal): 
    def __init__(self, name="Shepherd"): 
        self.name = name 
    def make_sound(self): 
        print(f"The dog {self.name} says Bow!") 

class Cat(Animal): 
    def __init__(self, name="Jerry"): 
        self.name = name 
    def make_sound(self): 
        print(f"The cat {self.name} says Meow!") 

class Bird(Animal): 
    def __init__(self, name="kiddd"): 
        self.name = name 
    def make_sound(self): 
        print(f"The bird {self.name} says Tweet!") 

animals = [Dog(), Cat(), Bird()] 
for a in animals: 
    a.make_sound()
