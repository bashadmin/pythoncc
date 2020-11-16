# In order to help us always set important values, we can use constructor methods
# We can use a special method called constructor
# The consturctor of the class is the method that'[s called when you call the name of the class.
# it's always named init, and this method starts and ends with two underscores.

class Apple():
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor
    
    def __str__(self):
        return f"""
Name: {golden.name}
Color: {golden.color}
Flavor: {golden.flavor}
        """


golden = Apple("Golden Delicous", "Yellow", "Sweet")
print(golden)

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds"""
    return hours*3600+minutes*60+seconds


class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """makes the elevator go up one floor."""
        self.current += 1
    def down(self):
        """makes the elevator go down one floor."""
        self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to a specific floor."""
        if (self.bottom <= floor <= self.top):
            self.current = floor
        return "Please try again."
    def __str__(self):
        return "Top: {}\nBottom: {}\nCurrent: {}".format(self.top, self.bottom, self.current)


ele = Elevator(-1,15,0)
print(ele)
ele.down()
print(ele.current)
ele.go_to(10)
ele.up()
print(ele.current)
ele.go_to(1)
ele.down()
print(ele.current)
