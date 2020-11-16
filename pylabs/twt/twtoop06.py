# You want to create classes that organize functions together
"""
def add_one():
    pass

def add_two():
    pass
"""

class Math:

    # creating a statcmethod, something that stays the same and does not have access to an instance
    # They cannot change anything because they do not have access
    # Does something but doesn't change anything
    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def pr():
        print("run")
print(Math.add5(5))
Math.pr()