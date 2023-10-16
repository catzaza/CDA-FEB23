# Program 1: Tip, Tax, and Total
food_charge = float(input("Enter the charge for the food: $"))
tip_percent = 18
sales_tax_percent = 7

tip_amount = (tip_percent / 100) * food_charge
sales_tax_amount = (sales_tax_percent / 100) * food_charge
total_amount = food_charge + tip_amount + sales_tax_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Sales tax amount: ${sales_tax_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")

# Program 2: Sales Prediction
total_sales = float(input("Enter the projected amount of total sales: $"))
profit_percentage = 23

profit = (profit_percentage / 100) * total_sales

print(f"Projected profit: ${profit:.2f}")

# Program 3: Miles-per-Gallon
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the gallons of gas used: "))

mpg = miles_driven / gallons_used

print(f"Car's MPG: {mpg:.2f} miles per gallon")

# Program 4: Total Purchase
subtotal = 0

for i in range(1, 6):
    item_price = float(input(f"Enter the price of item {i}: $"))
    subtotal += item_price

sales_tax_percent = 7
sales_tax_amount = (sales_tax_percent / 100) * subtotal
total = subtotal + sales_tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales tax amount: ${sales_tax_amount:.2f}")
print(f"Total: ${total:.2f}")
