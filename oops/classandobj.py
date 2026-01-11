#class is a blueprint or a template eg 
#obj is a entities in the real world op specific instance created from an object

class Employee:
    company="micorsoft"
    def getsalary(self):
        return 56000
e=Employee()#an object of class employee is created
print(e.getsalary())#get salary method is calling

e2=Employee()
print(e2.getsalary())
print(e2.company)