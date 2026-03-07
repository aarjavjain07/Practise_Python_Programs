# Python program to swap numbers as 1st number becomes 2nd and 2nd becomes 3rd and 3rd becomes 1st
x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
z = int(input("Enter third number :"))
a = x
b = y
c = z

x = c
y = a
z = b

print("Numbers after swapping :", x,y,z)