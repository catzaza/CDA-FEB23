# first get variables for subtotal and sales tax, 7 precent
subtotal = 0.0
sales_tax_percentage = 7  

# the get price of each item and calculate the subtotal
for item in range(1, 5):  # Loop through five items
    price = float(input(f"Enter the price of item {item}: $"))
    subtotal += price

# calc sales tax
sales_tax = (sales_tax_percentage / 100) * subtotal

# Calc total (subtotal + sales tax)
total = subtotal + sales_tax

# print results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")



