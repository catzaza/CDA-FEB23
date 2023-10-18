# Ask new employees for their username, password, and email.
# Print the output.

# Welcoming the new employee
print("Hello and welcome to Billy Bob's Boolean Bounce Castle, we are pleased that you will be joining us")

# Asking the new employee to create their username, password, email. 
#This will provide some basic checks as well
email = input("What is your preferred email?: ")
username = input("What would you like your username to be?\n"
                 "Here are some guidelines:\n"
                 "- It must be at least 5 characters\n"
                 "- It cannot contain numbers\n"
                 "- It cannot contain special characters:\n" 
                 
                 "username: ")

# Here is the basic check for the username
if len(username) < 5:
    print("Username must be at least 5 characters long.")
elif any(char.isdigit() for char in username):
    print("Username cannot contain numbers.")
elif any(not char.isalnum() for char in username):
    print("Username cannot contain special characters.")
else:
    print("Username is valid.")

# Here is the code for the password
password = input("What password would you like to create?\n"
                 "Here are some guidelines to follow:\n"
                 "- It must contain a mixture of lowercase & uppercase letters, numbers, and at least 3 special characters\n"
                 "password: ")

# Here are some checks to ensure a complex password is created.
has_lowercase = any(char.islower() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
special_chars = set("@#$%^&*!")

# Count the number of special characters in the password
num_special_chars = sum(1 for char in password if char in special_chars)

# Check if the password meets the criteria
if has_lowercase and has_uppercase and has_digit and num_special_chars >= 3:
    print("Password is valid.")
else:
    print("Invalid password. Please follow the guidelines.")

# Ran the code debugger and fixed minor issues.
# I have validated that everything is working now. 




