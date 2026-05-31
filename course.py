import sys
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    class Course:
        def __init__(self, course_name, student):
            self.course_name = course_name
            self.student = student
        def display_course(self):
            print("Course : " + self.course_name)
    def add_course(self, course_name):
        c = Student.Course(course_name, self)
        self.courses.append(c)
        print("Course Added: " + course_name)
        print("Reference count of course: " + str(sys.getrefcount(c)))
        print("Reference count of student: " + str(sys.getrefcount(self)))
    def display_student(self):
        print("\nStudent Name : " + self.name)
        print("Courses Enrolled:")
        for c in self.courses:
            c.display_course()
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nEnter details for student " + str(i+1))
    name = input("Enter student name: ")
    s = Student(name)
    m = int(input("Enter number of courses: "))
    for j in range(m):
        cname = input("Enter course name: ")
        s.add_course(cname)
    students.append(s)
print("\n--- STUDENT LIST ---")
for s in students:
    s.display_student()
