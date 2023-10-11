# A company has determined that its annual profit is typically 23 percent of total sales.
# Write a program that asks the user to enter the projected amount of total sales,
# and then displays the profit that will be made from that amount.

# Ask the user to enter the projected total sales
print()
print()
print("When prompted below, please enter the requested information.")
print()
# Ask the user to enter the projected total sales
sales_input = input("Enter the projected total sales: ")

print()

# Remove commas from the input and convert it to a float
total_sales = float(sales_input.replace(',', ''))

# Calculate the profit (assuming 23% profit margin)
profit_percentage = 0.23  # 23%
profit = total_sales * profit_percentage

# Format the profit with commas to two decimal places
formatted_profit = "{:,.2f}".format(profit)

# Display the formatted profit
print("The estimated annual profit based on projected sales is: $", formatted_profit)

print()
print()
