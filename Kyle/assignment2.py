# Ask the user to input a number between 1 and 10
user_input = input("Please enter a number between 1 and 10: ")

# Convert the user input to an integer
try:
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    # Check if the number is higher or lower than 5
    if 1 <= number <= 10:
        if number > 5:
            print("Higher")
        elif number < 5:
            print("Lower")
        else:
            print("It's 5!")
    else:
        print("Number is out of the specified range (1-10).")
