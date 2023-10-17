# Write a program that asks for a price of each item, and then displays the subtotal of the sale
def calculate_subtotal():
    subtotal = 0

    while True:
        item_price = input("Enter the price of the item (or 'done' to finish): ")

        if item_price.lower() == 'done':
            break

        try:
            item_price = float(item_price)
            subtotal += item_price
        except ValueError:
            print("Invalid input. Please enter a valid numeric value or 'done'.")

    return subtotal


if __name__ == "__main__":
    print("Welcome to the sales subtotal calculator!")
    subtotal = calculate_subtotal()
    print(f"The subtotal of the sale is: ${subtotal:.2f}")