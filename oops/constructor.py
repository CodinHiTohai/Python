class Employee:
    def __init__(self,name,salary,bond):
        self.name=name
        self.salary=salary
        self.bond=bond
    

    def print(self):
        print(f"the name of emoloyee is {self.name} and salary is {self.salary} and bond is{self.bond} years")
e1=Employee("govind",5600,5)
e1.print()
