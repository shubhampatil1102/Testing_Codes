from math import *

name = "john doey"
char_age = "44"

#  string functions
print("the name is " +name.upper() + " age is " + char_age)

#  If the string is in upper case then it will print True or it will convert in upper case then check.
print(name.upper().isupper())

#  length function
print(str(len(name)) + " is string length")

#  Printing character from string
print( name[2] + " The character is at index 2  ")

# function to return index number of character
print(str(name.index("h")) + " index number at h ")

# replace string
print(name.replace("john","tom"))

# converting number to string using function

print(str(len(name)) + " string length using number with string")

# absolute function

number = 5.3
print(abs(number))

#  power function
print(pow(4,2))

# roundoff number function

print(round(number))

#  Square root

print(sqrt(36))

#  getting input from user

username = input("Enter your name ")
print(username)