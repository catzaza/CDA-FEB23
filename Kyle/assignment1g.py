# Define the sales tax rate of 7%
sales_tax_rate = 0.07

# Variable to store the subtotal and total
subtotal = 0

# Ask the user to enter the price for each of the five items
for item in range(1, 6):
    price = float(input(f"Enter the price for item {item}: $"))
    subtotal += price

# Calculate the sales tax and total
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax

# Display the results
print("Subtotal: $", subtotal)
print("Sales Tax (7%): $", sales_tax)
print("Total: $", total)
