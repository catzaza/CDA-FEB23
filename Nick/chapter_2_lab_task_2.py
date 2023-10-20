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
