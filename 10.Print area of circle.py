# Python program to take radius from user in cm and print area of circle.
# we know formula for area of circle is pie * r * r

radius = float(input("Enter radius of circle (in cm) : "))
area = 3.14 * radius * radius
print("Area of circle : ", format(area, ".2f"), "cm²")