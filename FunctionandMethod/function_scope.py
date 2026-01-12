def sum(a,b):
    # a and b are local variable
    d=a+b
    z=1#z is a global variable
    print(z)
    return d

z=8 #z is a global variable
print(z)
print(sum(5,4))
# print(a)#local variable

print(z)