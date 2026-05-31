import gc
import sys
class university:
        def __init__(self,university_name):
            self.university_name = university_name
            self.students = []
        class student:
            def __init__(self,rollno,name,university):
                self.rollno = rollno
                self.name = name
                self.university = university
            def display_details(self):
                print("Roll No : " ,str(self.rollno))
                print("Name : " ,self.name)
                print("University : " ,self.university.university_name)
            def __del__(self):
                print("student object deleted:"+self.name)
        def add_student(self,rollno,name):
            s=university.student(rollno,name,self)
            self.students.append(s)
            print("student added :" ,name)
            print("reference count of student:",sys.getrefcount(s))
            print("reference count of university:",sys.getrefcount(s))
        def remove_student(self,rollno):
            for s in self.students:
                if s.rollno == rollno:
                    self.students.remove(s)
                    del s
                    gc.collect()
                    print("student removed ")
                    break
        def display_all(self):
            print("student list:")
            for s in self.students:
                s.display_details()
uni_name=input("enter university name:")
uni = university(uni_name)
n=int(input("Enter no. of students: "))
for i in range(n):
    print("Enter student details")
    roll=int(input("Enter roll no: "))
    name=input("Enter name of student: ")
    uni.add_student(roll,name)
uni.display_all()
r=int(input("Enter roll no. to remove : "))
uni.remove_student(r)
print("\nAfter Deletion:")
uni.display_all()