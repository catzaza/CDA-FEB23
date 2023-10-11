# A customer in a store is purchasing five items. Write a program that asks for the price of each item,
# and then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

# Initialize variables
subtotal = 0
sales_tax_rate = 0.07  # 7% sales tax rate

# Collect prices for five items
print()
print()
print("When prompted below, please enter the requested information.")
print()

# Initialize variables
subtotal = 0
sales_tax_rate = 0.07  # 7% sales tax rate
item_prices = []

# Collect prices for five items
for i in range(1, 6):
    while True:
        price_input = input(f"Enter the price for item {i}: $")
        # Remove any commas and convert to a float
        try:
            price = float(price_input.replace(',', ''))
            item_prices.append(price)
            break
        except ValueError:
            print("Invalid price format. Please enter a valid price.")

print()
print()
# Calculate the subtotal
subtotal = sum(item_prices)

# Calculate sales tax and total
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax

# Format the subtotal, sales tax, and total with commas and two decimal places
formatted_subtotal = "{:,.2f}".format(subtotal)
formatted_sales_tax = "{:,.2f}".format(sales_tax)
formatted_total = "{:,.2f}".format(total)

# Display the results
print("\nReceipt:")
for i, price in enumerate(item_prices, 1):
    print(f"Item {i}: ${'%.2f' % price}")
print(f"\nSubtotal: ${formatted_subtotal}")
print(f"Sales Tax (7%): ${formatted_sales_tax}")
print(f"Total: ${formatted_total}")

print()
print()