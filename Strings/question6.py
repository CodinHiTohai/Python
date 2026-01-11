# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
# Find the index of the word "Python" in sentence.
# Convert the entire sentence to uppercase and print it.

sentence="coding in python is fun"
print(sentence.replace("fun","awesome"))

print(sentence.find("python"))

print(sentence.upper())

# Write a program that counts how many vowels are in a given string.
# Take a user input string and check if it is a palindrome (same forwards and backwards).
string=input("the the string")
vowel="aeiou"

count=0
for i in string:
    if i in vowel:
        count+=1
print("number of vower",count)


name="racecar"

name2=name[::-1]

if(name==name2):
    print("this is palindrone")
else:
    print("this is not a palidrone")
