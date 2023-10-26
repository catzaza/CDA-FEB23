# Using the print function, print your name
print("Nick")

# Create a variable called Name and assign your name to it. Print the output of the variable
name = "Nicholas"
print(name)

# Using input function, create a python code that asks for a user's name and prints it out
username = input("Enter your username: ")
print("Hello, " + username)

# Using the input function, create a python code that asks for a user's phone number and prints it out
phonenumber = input("Please enter your phone number: ")
print("Our records indicate that your phone number is: " + phonenumber)

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