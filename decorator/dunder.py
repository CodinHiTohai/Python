class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        return f"the name is {self.name} and the salary is {self.salary}"
e1=Employee("govind",74347)
print(e1.name,e1.salary)
print(str(e1))