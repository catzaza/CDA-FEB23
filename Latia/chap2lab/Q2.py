# get projected total sales from user
total_sales = float(input("Enter the projected total sales: $"))

# calc annual profit which is 23 percent
profit_percentage = 23
annual_profit = (profit_percentage / 100) * total_sales

# pint total calculated annual profit
print(f"Annual profit based on projected sales of ${total_sales:.2f} is ${annual_profit:.2f}")
