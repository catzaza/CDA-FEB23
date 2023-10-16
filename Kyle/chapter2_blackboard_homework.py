# Task 1: Print your name
print("Kyle")

# Task 2: Create a variable called Name and print its value
Name = "Kyle"
print(Name)

# Task 3: Ask for a user's name and print it
user_name = input("Enter your name: ")
print("Hello, " + user_name)

# Task 4: Ask for a user's phone number and print it
phone_number = input("Enter your phone number: ")
print("Your phone number is: " + phone_number)

# Task 5: Total Purchase
subtotal = 0

for i in range(1, 6):
    item_price = float(input(f"Enter the price of item {i}: $"))
    subtotal += item_price

print(f"Subtotal: ${subtotal:.2f}")
