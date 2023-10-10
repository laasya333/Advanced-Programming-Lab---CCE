class Employee:
    total_emp=0
    
    def __init__(self, empid, name, salary, department):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.department=department
        Employee.total_emp+=1

    def display_emp(self):
        print(f"employee id: {self.empid}")
        print(f"employee name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"department : {self.department}")

    @staticmethod
    def create_record():
        eid=int(input("emp_id: "))
        name=input("name: ")
        salary=int(input("salary: "))
        dept=input("department: ")
        return Employee(eid,name,salary,dept)
    
def search(l, eid):
    for employee in l1:
        if(employee.empid==eid):
            employee.display_emp()
            
n=int(input("enter number of employees: "))
l1=[];

for i in range(n):
    print(f" employee {i+1}: ")
    e=Employee.create_record()
    print()
    l1.append(e)
    
s=int(input("id to be searched: "))
search(l1,s)
