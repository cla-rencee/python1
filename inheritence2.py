class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_name(self):
        print(f"My name is {self.last_name},{self.first_name} and Im {self.age} years old.")
class Student(Person):
    def __init__(self, first_name, last_name, age,):
        super().__init__(first_name, last_name, age)
myStudent = Student("John", "Smith", 25)
myStudent.print_name()
myStudent2 = Student("Jamal", "Mohammed", 27)
myStudent2.print_name()
myStudent3 = Student("Victoria", "Monet", 35)
myStudent3.print_name()