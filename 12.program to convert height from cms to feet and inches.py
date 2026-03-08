# WAP to convert your height in centimeters to feet and inches.
# 1 foot = 30.48 centimeters.
# 1 inch = 2.54 centimeters.
height = float(input("Whats your height in centimeters :"))
foot = height / 30.48
inches = height / 2.54

print("Your height is", format(height,".2f"), "cms")

print("which is equal to", format(foot,".2f"), "foot")

print("which is also equal to",format(inches,".2f"),"inches")