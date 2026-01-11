class Animal:
    location="zimbawe"
    def __init__(self,name):
        self.name=name
    def spek(self):
        print("this speak generic sound")

class Dog(Animal):
    def spek(self):
        super().spek()
        print("woof")
a=Animal("dog")


d=Dog("bruno")
d.spek()
print(d.location)