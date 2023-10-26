# tip, tax, total
def calculate_total_amount(food_charge):
    tip_amount = 0.18 * food_charge
    tax_amount = 0.07 * food_charge
    total_amount = food_charge + tax_amount + tip_amount
    return tip_amount, tax_amount, total_amount

def main():
    food_charge = float(input("Please enter the charge for the food: $"))
    tip, tax, total = calculate_total_amount(food_charge)

    print(f"Tip amount (18%): ${tip:.2f}")
    print(f"Sales tax amount (7%): ${tax:.2f}")
    print(f"Total amount: ${total:.2f}")

if __name__ == "__main__":
    main()

# sales prediction

def calculate_profit(total_sales):
    profit_percentage = 0.23
    profit = profit_percentage * total_sales
    return profit

def main():
    total_sales = float(input("Enter the projected total amount of sales: $"))
    profit = calculate_profit(total_sales)
    print(f"The profit from projected total sales is: ${profit:.2f}")

if __name__ == "__main__":
    main()

# miles per gallon

def calculate_mpg(miles_driven, gallons_used):
    mpg = miles_driven / gallons_used
    return mpg


def main():
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons used: "))

    if miles_driven <= 0 or gallons_used <=0:
        print("Miles driven and gallons used must be positive numbers.")
    else:
        mpg = calculate_mpg(miles_driven, gallons_used)
        print(f"The cars mpg is: {mpg:.2f} miles/gallon")

if __name__ == "__main__":
    main()

# total purchase
def calculate_total(items_prices):
    subtotal = sum(items_prices)
    sales_tax = 0.07 * subtotal
    total = subtotal + sales_tax
    return subtotal, sales_tax, total

def main():
    items_prices = []
    for i in range(5):
        item_price = float(input(f"Enter the price of item {i + 1}: $"))
        items_prices.append(item_price)

    subtotal, sales_tax, total = calculate_total(items_prices)

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales tax (7%): ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()