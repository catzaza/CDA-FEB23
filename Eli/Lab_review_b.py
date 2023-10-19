# 2.	Write a program that asks the user to enter a distance in kilometers, and then convert that distance to miles. 
#       The conversion formula is as follows:
#       Miles = Kilometers * 0.6214

# Promt user for kilometers and save it to a integer vairable
kilometes=int(input("Please enter Kilometers: "))

# Convert the kilometers to miles using the formula (Miles = Kilometers * 0.6214)
miles=kilometes*0.6214

# Print the results
print(kilometes, "Kilometers is", miles, "Miles.")