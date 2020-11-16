# Inherentence

"""
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark")
"""

# Ideally we wouldn't want to have to retype the self.name and self.age because only the speak method is different.
# The is the general class and upper level class
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def get_info(self):
        print(f"Name: {self.name}", f"Age: {self.age}", f"Species: {self.species}", sep="\n")

    def speak(self):
        print("Sound unknown.")

# This is the lower level class that is inherating from the upper level class
class Cat(Animal):
    def __init__(self, name, age, species, color):
        super().__init__(name, age, species)
        self.color = color

    def speak(self):
        print("Meow")
    
    def get_info(self):
        print(f"Name: {self.name}", f"Age: {self.age}", f"Species: {self.species}", f"Color: {self.color}", sep="\n")
    


class Dog(Animal):
    def speak(self):
        print("Bark")


class Fish(Animal):
    pass

new_cat01 = Cat("Sam", 12, "Blue Russian", "Orange")
new_dog01 = Dog("Milo", 3, "German Shepherd")
new_dog01.get_info()
new_cat01.speak()
a = Animal("Gary", 1, "Gold Fish")
a.speak()
new_cat01.get_info()