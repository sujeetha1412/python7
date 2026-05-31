import sys
import gc
class Company:
    def __init__(self, cname):
        self.cname = cname
        self.employees = []
    class Employee:
        def __init__(self, emp_id, emp_name, company):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.company = company
        def display_details(self):
            print("\nEmployee ID   : " + str(self.emp_id))
            print("Employee Name : " + self.emp_name)
            print("Company Name  : " + self.company.cname)
        def __del__(self):
            print("Employee Removed: " + self.emp_name)
    def add_employee(self, emp_id, emp_name):
        e = Company.Employee(emp_id, emp_name, self)
        self.employees.append(e)
        print("Employee Added: " + emp_name)
        print("Reference count of employee:", sys.getrefcount(e))
        print("Reference count of company :", sys.getrefcount(self))
    def remove_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                self.employees.remove(e)
                del e
                gc.collect()
                print("Employee with ID", emp_id, "removed")
                break
    def display_all(self):
        print("\n--- Employee List of " + self.cname + " ---")
        for e in self.employees:
            e.display_details()
name = input("Enter company name: ")
c = Company(name)
n = int(input("Enter number of employees: "))
for i in range(n):
    print("\nEnter employee details")
    emp_id = int(input("Emp ID: "))
    emp_name = input("Emp Name: ")
    c.add_employee(emp_id, emp_name)
c.display_all()
m = int(input("\nEnter number of employees to remove: "))
for i in range(m):
    emp_id = int(input("Enter Emp ID to remove: "))
    c.remove_employee(emp_id)
c.display_all()
