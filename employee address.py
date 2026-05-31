import gc
class Employee:
    count= 0
    class Address:
        def __init__(self, door_no, street, city):
            self.door_no = door_no
            self.street = street
            self.city = city
        def display(self):
            print("Door No : " + str(self.door_no))
            print("Street  : " + self.street)
            print("City    : " + self.city)
    def __init__(self, emp_no, name, door_no, street, city):
        self.emp_no = emp_no
        self.name = name
        self.addr = Employee.Address(door_no, street, city)
        Employee.count += 1
        print("Hired: " + self.name)
    def display(self):
        print("\nEmp No : " + str(self.emp_no))
        print("Name   : " + self.name)
        self.addr.display()
    def __del__(self):
        Employee.count=Employee.count - 1
        print("Resigned: " + self.name)
n = int(input("Enter number of employees: "))
emp_list = []
for i in range(n):
    print("\nEnter details for employee " + str(i+1))
    emp_no = int(input("Employee Number: "))
    name = input("Name: ")
    door_no = input("Door No: ")
    street = input("Street: ")
    city = input("City: ")
    emp = Employee(emp_no, name, door_no, street, city)
    emp_list.append(emp)
print("\n--- Employee List ---")
for e in emp_list:
    e.display()
print("\nTotal Employees: " + str(Employee.count))
num = int(input("\nEnter Employee Number to remove: "))
for e in emp_list:
    if e.emp_no == num:
        emp_list.remove(e)
        del e
        gc.collect()
        break
print("Total Employees after resignation: " + str(Employee.count))
