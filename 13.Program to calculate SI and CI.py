# Program to compute simple interest and compound interest.

p = float(input("Enter the principal amount in rupees:"))
r = float(input("Enter rate of interest (per year) (in %) :"))
t = float(input("Enter time in years :"))

# ---------------SIMPLE INTEREST---------------

SI = ( p * r * t ) / 100
print("Simple interest would be equal to", format(SI,".2f"),"rupees")

# ---------------COMPOUND INTEREST---------------
a = p * ((1 + (r/100))**t)
CI = a - p
print("Compound interest would be equal to", format(CI,".2f"),"rupees")