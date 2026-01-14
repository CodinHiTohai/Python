class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        
        #instance method
    def print_info(self):
        d=f"the name is {self.name} and the salary is {self.salary}"
        print(d)

    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,newcompany):
        cls.company=newcompany
e1=Employee("goivnd",5553)
e2=Employee("kumar",8834)
#print(Employee.name)
# e1.print_info()
# e2.print_info()

# print(e1.sum(5,4))
print(e1.company)
e1.change_company("dell")
print(e1.company)