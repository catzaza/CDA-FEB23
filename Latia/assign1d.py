# to store employee info
employee_info = {
    "username": "",
    "password": "",
    "email": ""
}

# Ask new employee for their info
employee_info["username"] = input("Enter username: ")
employee_info["password"] = input("Enter password: ")
employee_info["email"] = input("Enter email: ")

# Print collected info
print("New Employee Info:")
for key, value in employee_info.items():
    print(f"{key.capitalize()}: {value}")