# 1
user_string = input("Enter a string: ")

string_length = len(user_string)

for i in range(string_length):
    print(user_string[i])

# 2
def generate_login_name(firstname, lastname, idnumber):
    first3 = firstname[:3]

    last3 = lastname[:3]

    id3 = idnumber[:3]

    login_name = first3 + last3 + id3

    return login_name

# Example usage
firstname = "John"
lastname = "Doe"
idnumber = "123456789"
login = generate_login_name(firstname, lastname, idnumber)
print("Generated Login Name:", login)

# 3
lab = "Hey guys it’s lab time and Daniel is missing in class"

user_input = input("Enter a string to check: ")

if user_input in lab:
    print(f"The entered string '{user_input}' is present in the given string.")
else:
    print(f"The entered string '{user_input}' is not present in the given string.")