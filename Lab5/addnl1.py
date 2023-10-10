class Employee:
    emp_counter=2912
    
    def __init__(self, empid, name, salary, department):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.department=department

    def __del__(self):
        print(f"employee records of id {self.empid} are deleted.")

    def display_emp(self):
        print(f"employee id: {self.empid}")
        print(f"employee name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"department : {self.department}")

    @staticmethod
    def create_record():
        eid=Employee.emp_counter
        Employee.emp_counter+=1
        name=input("name: ")
        salary=int(input("salary: "))
        dept=input("department: ")
        return Employee(eid,name,salary,dept)

    @classmethod
    def total_salary(cls,l):
        sum=0
        for employee in l:
            sum=sum+employee.salary
        return sum
    
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
    
print(f"total salary of all employees is: {Employee.total_salary(l1)}")

s=int(input("id to be searched: "))
search(l1,s)
