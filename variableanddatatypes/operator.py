# types of operator
# Arithmetic Operators:

# + (Addition), - (Subtraction), * (Multiplication), / (Division), % (Modulus), ** (Exponentiation), // (Floor Division).
# Example:
print(10 + 5)   # Output: 15
(10 ** 2)  # Output: 100

# Comparison Operators:

# == (Equal), != (Not Equal), > (Greater Than), < (Less Than), >= (Greater Than or Equal), <= (Less Than or Equal).
# Example:
print(10 > 5)   # Output: True
print(10 == 5)  # Output: False

# Logical Operators:

# and, or, not.
# Example:
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False

# Assignment Operators:

# =, +=, -=, *=, /=, %=, **=, //=.
#Example:
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15

# Membership Operators:

# in, not in.
# Example:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True

# Identity Operators:

# is, is not.
 #Example:
x = 10
y = 10
print(x is y)  # Output: True

# Summary
# Variables store data, and Python supports multiple data types.
# Typecasting allows you to convert between data types.
# Use input() to take user input and print() to display output.
# Comments and escape sequences help make your code more readable.
# Python provides a variety of operators for performing operations on data



#arithmetic operator
a=35
b=2;
print(a+b)
print(a*b)
print(a-b)
print(a//b) #this return the floor value 


#comparison operator
print(a>4)
print(a<4)
print(a>=4)
print(a<=4)
print(a==4)
print(a!=4)

#logical operator
c=True
d=False
print(c and d)
print(c or d)
print(c and c)
print(c or d)

print(not(True))
print(not(False))


#assignment operator
a=22;
a+=5
print(a)
#assignment operator
a=22;
a-=5
print(a)
#we also use divide and multiply like this
print(2**5)#exponentiation 
print(5//2) # for floor value


#member ship
vagetable=["potato","onion","lock key","cucumber"]
print("potato" in vagetable)