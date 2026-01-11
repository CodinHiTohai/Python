class Employee:
    company="vivo"
    def __init__(self,name,salary,bond,comany):
        self.name=name
        self.salary=salary
        self.bond=bond
        self.company=comany

    

    def print(self):
        print(f"the name of emoloyee is {self.name} and salary is {self.salary} and bond is{self.bond} years and company is {self.company}")
e1=Employee("govind",5600,5,"dell")
e1.print()#this will print a intance company name
print(Employee.company)#this will print a class attribute
