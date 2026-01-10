# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
# n=int(input("enter the number"))
# if(n>0):
#     print("positive number")
# elif(n==0):
#     print("number equal to zero")
# else:
#     print("negaitive number")

#  2 Create a program that checks if a person is eligible to vote (age >= 18).

# age=int(input("enter you age"))
# if(age>=18):
#     print("you can vote")
# else:
#     print("you cannot vote ")

# 3 Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
# num=int(input("enter the number"))
# if(num%2==0):
#     print("this is even number")
# else:
# #     print("this is odd number")

# 4 Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
# num=int(input("enter the number between 1to 7"))
  
# match(num):
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")


# 5 Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

# num1=int(input("enter the the first number"))
# num2=int(input("enter the second number"))
# operator=input("enter the operator")
# match(operator):
#     case '+':
#         print(num1+num2)
#     case '*':
#         print(num1*num2)
#     case '/':
#         print(num1/num2)
#     case '-':
#         print(num1-num2)


#  6  Print numbers from 1 to 10 using a for loop.
# for i in range (1,11):
#     print(i)


#  7  Print the multiplication table of a number (entered by user).

# num=int(input("enter the number you want multiplication table"))
# for i in range(1,11):
#     print(num*i)


#  8 Calculate the sum of all numbers from 1 to 100 using a for loop.
# sum=0;
# for i in range(1,101):
#     sum=sum+i;
# print(sum)

# Print the following pattern using a for loop:
# *
# **
# ***
# ****

# for i in range (1,5):
#     print("*"*i)

# 8 Print numbers from 1 to 10 using a while loop.
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# Write a program that keeps asking the user to enter a password until they enter the correct one.
# password="govind"
# newpass=input("enter the correct password")
# while(password!=newpass):
#     newpass=input("enter you correct password again")
#     if(password!=newpass):
#         print("enter the correct password")

# print("you have succesulyy fetch your password")

#  9 Use a while loop to reverse a given number (e.g., 123 → 321).

# num=123
# rev=0;
# while(num>0):
#     rem=num%10;
#     rev=rev*10+rem
#     num=num//10;
# print(rev)

#  10 Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
# for i in range(1,11):
#     print(i)
#     if(i==7):
#         break;

# Print numbers from 1 to 10, skipping the number 5 (use continue).
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)


# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
for i in range(1,6):
    if(i==3):
        pass
    else:
        print(i)