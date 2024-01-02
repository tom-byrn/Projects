import math

#Define variables
principle = 0
monthly_contributions = 0
apr = 0
years = 0


#Get each value
while principle <= 0:
    try:
        principle = float(input("Enter the initial sum invested: "))
    except ValueError:
        print("Please enter a numerical value")
    if principle < 0:
        print("Initial sum must be greater than zero!")
    if principle > 0:
        print(f"The initial sum invested is ${principle}")

while monthly_contributions <= 0:
    try:
        monthly_contributions = float(input("Enter your monthly contributions: "))
    except ValueError:
        print("Please enter a numerical value")
    if monthly_contributions < 0:
        print("Monthly contributions must be greater than zero!")
    if monthly_contributions > 0:
        print(f"Your monthly contributions are ${monthly_contributions}")

while apr <= 0:
    try:
        apr = float(input("Enter the interest (Annual Percentage Rate): "))
    except ValueError:
        print("Please enter a numerical value from 1-100")
    if apr <= 0 or apr > 100:
        print("Must be between 0 and 100")
    if monthly_contributions > 0:
        print(f"Your APR is {apr}%")
apr = (apr/100)

while years <= 0:
    try:
        years = float(input("Enter the amount of years you wish to invest for: "))
    except ValueError:
        print("Please enter a numerical value")
    if years < 0:
        print("Years value must be greater than or equal to zero!")


#Convert to monthly values
months = years*12
mpr = apr / 12 / 100

#Get final value
Final_Value = (monthly_contributions * (((1 + mpr) ** months) - 1)/ mpr) + (principle * ((1+apr)**years))

Final_Value = round(Final_Value, 2)

print(f'Final Value: ${Final_Value}')
