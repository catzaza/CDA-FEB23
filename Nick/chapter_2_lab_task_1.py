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