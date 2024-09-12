
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self, student, math_course, grade):
        print(f"Student: {student.name}, Course: {math_course}, Grade: {grade}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return self.subject
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            math_course.attendance_record = self.attendance.get(student, [])
            attendance_status = "VIRUS VIRUS VIRUS"
            print(f"Student: {student.name}, Attendance: {math_course.attendance_record}")

            # math_course.add_lesson(lesson1)
            # math_course.add_lesson(lesson2)
            #
            # math_course.get_lessons()

    def add_lesson(self):
       self.lesson.append(lesson1)
       self.lesson.append(lesson2)



    def get_lessons(self):

        return self.lesson()

        print(self.lessons())




class Lesson():
    def __init__(self, lesson_name, lesson_date, lesson_book):
        self.lesson_name = lesson_name
        self.lesson_date = lesson_date
        self.lesson_book = lesson_book
        self.lesson = []

    def show(self):
        print(f"Lesson name: {self.lesson_name}, Date: {self.lesson_date}, Book: {self.lesson_book}")


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report(student= alice, math_course= "Mathematics", grade="A")
bob.performance_report(student= bob, math_course= "Mathematics", grade="B")
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

# Lesson impletemented methods
lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])
lesson1.show()
lesson2.show()



