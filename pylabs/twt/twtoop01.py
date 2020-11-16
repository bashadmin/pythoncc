# make the int object x
x = 1

# shows that when we assigned the variable we made something of the class/object int
#print(type(x))

# make the function object, a built in type object
def hello():
    print("Hello")

# An object is an istance of a specfic class
#print(type(hello))

# Methods are things we can preform on objects

# Here we make a new object dog, and start defining new functions as it's method, or what the type can do.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def bark(self):
        print("bark")
    
    def whimper(self):
        return "ahhuhahhuh"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

# I made a new var d and assigned it a new instance of the class Dog (also known as instanciating)
"""d = Dog()
print(type(d))
# shows an object of the class dog from the main module
d.whimper()
# I can call a method on my new dog object
print(d.whimper())"""
milo = Dog("Milo", 3)
milo.set_age(4)
print(milo.get_age())