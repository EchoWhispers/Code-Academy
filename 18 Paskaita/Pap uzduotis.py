# Create a base class Person with attributes name and age
# and method display_info
# that prints name and age. Then, create a child class Student that inherits from Person.
# The Student class should have a private attribute __student_id and provide methods set_student_id and get_student_id to set and get the student ID.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"name:{self.name}, Age:{self.age}")


class Student(Person):

    def __init__(self,name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self):
      return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id


s = Student(name= "Auri" , age= 35, student_id= 895965)

s.display_info()
print("student_id", s.get_student_id())
s.set_student_id("885588")
print("updated ID: ", s.get_student_id())
