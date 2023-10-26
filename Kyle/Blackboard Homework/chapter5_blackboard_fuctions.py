# Task 1: Write a function named computer() that prints your name.
def computer():
    print("Kyle")

# Call the function
computer()





# Task 2: Write a function named times_ten() the function should accept an argument from a user 
# and display the product of its argument multiplied times 10.
# Ask the user to input a number
user_input = float(input("Enter a number: "))

# Calculate and display the result
result = user_input * 10
print(f"The result of {user_input} multiplied by 10 is {result}")





# Task 3: Write a function named welcome() that asks the user to enter his or her name and displays it followed by a welcome message.
# Let's define the function
def welcome():
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

# Call the function to welcome the user
welcome()





# Task 4: Write a function named get_first_name() that asks the user to enter his or her first name and returns it.
# Let's define the function
def get_first_name():
    first_name = input("Enter your first name: ")
    return first_name

# Call the function and store the result in a variable
user_first_name = get_first_name()

# Display the user's first name
print(f"Your first name is: {user_first_name}")






# Task 5: Write a function named area() that gets a number from a user and multiplies it by 15.
# Let's define the function
def area(number):
    result = number * 15
    return result

# Get the input
user_input = float(input("Enter a number: "))

# Call the function and display the result
result = area(user_input)
print(f"{user_input} multiplied by 15 is {result}")
