# OOP

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        #self.is_active = False
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def addMany_students(self, *args):
        if len(self.students) < self.max_students:
            for arg in args:
                self.students.append(arg)
            return True
        return False

    def get_students(self):
        return self.students

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.get_students())

student_01 = Student("John", 23, 86)
student_02 = Student("Marty", 22, 67)
student_03 = Student("Kim", 20, 91)
new_course = Course("Python", 4)

new_course.addMany_students(student_01,student_02,student_03)
# new_course.add_student(student_01)
# new_course.add_student(student_02)
# new_course.add_student(student_03)
print(new_course.get_students())
print(new_course)
print(new_course.students[0].name)
print(new_course.students[0])
print(new_course.students[1])
print(new_course.students[2].name)
print(new_course.get_average_grade())