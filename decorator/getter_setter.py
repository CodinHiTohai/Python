class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def fistname(self):
        l=self.name.split(" ")
        return l[0]
    def setfirstname(self,newname):
        l=self.name.split(" ")
        myname=f"{newname} {l[1]}"
        self.name=myname;


e=Employee("goivnd kumar", 5555)
e.setfirstname("dheeraj")
print(e.name)