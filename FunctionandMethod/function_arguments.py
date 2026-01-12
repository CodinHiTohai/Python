def sum(a,b):#this is parameter
    d=a+b
    return d

h=sum(4,5)#this is arguments
print(h)



# this is positional arguments
def sum(a,b):
    d=a+b
    return d

h=sum(4,5)
print(h)


# this is default afguments
def sum(a,b,plus=5):
    d=a+b+plus
    return d

h=sum(4,5)
print(h)



# this is keyword arguments
def sum(a,b):
    d=a+b
    return d

c1=sum(a=5,b=55)
print(c1)
