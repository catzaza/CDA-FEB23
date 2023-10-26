# km convert
kilometers = float(input("Enter a distance in kilometers: "))

miles = kilometers * 0.6214

print(f"{kilometers} kilometers is equal to {miles} miles.")

#how much insurance
replacement_cost = float(input("Enter the replacement cost of the building: $"))

minimum_insurance = 0.8 * replacement_cost

print(f"You should buy a minimum of ${minimum_insurance:.2f} in insurance for the property.")

# stadium seating
price_class_a = 20
price_class_b = 15
price_class_c = 10

tickets_class_a = int(input("Enter the number of Class A tickets sold: "))
tickets_class_b = int(input("Enter the number of Class B tickets sold: "))
tickets_class_c = int(input("Enter the number of Class C tickets sold: "))

total_income = (tickets_class_a * price_class_a) + (tickets_class_b * price_class_b) + (tickets_class_c * price_class_c)

print(f"Total income from ticket sales: ${total_income:.2f}")