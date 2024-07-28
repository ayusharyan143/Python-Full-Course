# Write a python function which converts inches to cms.

def inches_to_cm(inches):
    return inches * 2.54

inches = float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inches_to_cm(inches)} centimeters")
