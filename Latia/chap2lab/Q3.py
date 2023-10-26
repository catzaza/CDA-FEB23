# first we get number of miles driven from the user
miles_driven = float(input("Enter the number of miles driven: "))

# then get the gallons of gas used from the user
gallons_of_gas = float(input("Enter the gallons of gas used: "))

# calc the MPG (Miles Per Gallon)
mpg = miles_driven / gallons_of_gas

# print the calc MPG
print(f"The car MPG is: {mpg:.2f} miles per gallon")