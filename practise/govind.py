
# def decorater(func):
#     def wrapper():
#         print("good morinig")
#         func()
#         print("good afternoon")
#     return wrapper    

# @decorater
# def say_hello():
#     print("hello govind")

# say_hello()

# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator
# @repeat(4)
# def greet(name):
#     print(f"hello",{name})     
# greet("govind")

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name;
#         self.salary=salary;
#     @property
#     def first_name(self):
#         l= self.name.split(" ")
#         print(l[0])
#     @first_name.setter
#     def set_firstname(self,first):
#         l=self.name.split(" ")
#         newname=f"{first} {l[1]}"
#         self.name=newname;
# e=Employee("govind kumar",5600)
# # e.project=6;
# # e.set_firstname("shivam")
# # print(e.name)
# print(e.first_name)
# e.set_firstname="sudhanshu"
# print(e.name)

# class Employee:
#     company="dell"
#     def __init__(self,name,salary):
#         self.name=name;
#         self.salary=salary;
# e=Employee("govind",5746)
# e2=Employee("shubham",5737)

# while(True):
#     try:
#         a=int(input("enter the number 1"))
#         b=int(input("enter the number 2"))

#         print(f"the sum is {a+b}")
#     except Exception as e:
#         print("some error occurred",e)
from functools import reduce
number=[1,2,3,4,5]
def square(x):
    return x*x;
new=list(map(square,number))
print(new)

number=[1,2,3,4,5,6,7,8,9,10]
def sum(x,y):
    return x+y
new=reduce(sum,number)
print(new)