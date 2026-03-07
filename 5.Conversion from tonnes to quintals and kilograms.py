# Python program to convert the value in tonnes to quintals and kilograms.
tonnes = float(input("Enter the value in tonnes :"))
value_in_quintal = tonnes * 10
value_in_kilograms = tonnes * 1000
print("\n",tonnes,"tonnes is equal to ", format (value_in_quintal, ".1f"),"quintal")
print("\n",tonnes,"tonnes is equal to ", format(value_in_kilograms, ".1f"),"kilograms")
