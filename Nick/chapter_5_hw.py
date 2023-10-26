# functions 1
def computer():
    print("Nick")

computer()

# 2
def times_ten(number):
    result = number * 10
    print(f"{number} multiplied by 10 is: {result}")

user_input = float(input("Enter a number: "))
times_ten(user_input)

# 3 
def welcome():
    name = input("Please enter your name: ")
    print(f"Welcome, {name}!")

welcome()

# 4
def get_first_name():
    first_name = input("Please enter your first name: ")
    return first_name

user_first_name = get_first_name()
print("Your first name is:", user_first_name)

# 5
def area(number):
    result = number * 15
    return result

user_input = float(input("Enter a number: "))
result = area(user_input)
print("The result is:", result)