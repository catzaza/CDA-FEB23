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
