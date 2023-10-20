# Task 1: Kilometer conversion
def kilometers_to_miles(kilometers):
    return kilometers * 0.6214

# Getting the input from the user
kilometers = float(input("How many kilometers would you like to convert? "))

# Converting and displaying the conversion
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles")




# Task 2: Minimum amount of insurance for the total replacement cost
def minimum_replacement_cost(total_cost):
    return total_cost * 0.80

# Asking the user for the total replacement cost
total_cost = float(input("How much is the total replacement cost? "))

# Calculate the minimum insurance amount (80% of the total cost)
insurance_amount = minimum_replacement_cost(total_cost)

# Outputting the minimum insurance amount for the user
print(f"The minimum amount that you need to have for insurance will be {insurance_amount}")




# Task 3: Calculating ticket sales based on seats sold

# Defining the cost for each class of seats
class_a_seats = 20
class_b_seats = 15
class_c_seats = 10

# Function to calculate the total sales
def total_sales(class_a_sold, class_b_sold, class_c_sold):
    return (class_a_sold * class_a_seats) + (class_b_sold * class_b_seats) + (class_c_sold * class_c_seats)

# Asking the ticket manager for that day's numbers
class_a_sold = int(input("How many class A seats were sold? "))
class_b_sold = int(input("How many class B seats were sold? "))
class_c_sold = int(input("How many class C seats were sold? "))

# Calculate the total sales
total = total_sales(class_a_sold, class_b_sold, class_c_sold)

# Displaying the total number of seats sold and the total sales
print(f"Since you have sold {class_a_sold} Class A seats, {class_b_sold} Class B seats, and {class_c_sold} Class C seats, your total sales are ${total}.")
