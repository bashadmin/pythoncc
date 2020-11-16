# Class attributes

# Make classes robust enough that they can depend on themselves, you can put in these local variables.
class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        #Person.number_of_people += 1
        Person.add_person() # Calling the class attribute

    @classmethod # classmethods act on the class themselves, not the objects.
    def current_count(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Jill")
print(Person.current_count())
p2 = Person("John")
# print(Person.number_of_people)
#p2.add_person()
# print(Person.number_of_people)
print(Person.current_count())