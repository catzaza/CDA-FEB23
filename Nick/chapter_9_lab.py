# dictionaries 1
devices = {
    "router": "192.168.1.1",
    "switch": "192.168.1.2",
    "printer": "192.168.1.3",
    "laptop": "192.168.1.4"
}

user_device = input("Enter a device name to check: ")

if user_device in devices:
    print(f"The IP address for {user_device} is: {devices[user_device]}")
    print("Device found. Exiting.")
else:
    print(f"The device '{user_device}' does not exist in the dictionary.")

# 2
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4"
}

usernames = list(user_credentials.keys())
print("Usernames:", usernames)

passwords = list(user_credentials.values())
print("Passwords:", passwords)

# 3
gradebook = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 80],
    "Charlie": [92, 88, 90],
    "David": [75, 80, 79]
}

name = input("Enter a name to update grades: ")

if name in gradebook:
    new_grades = input(f"Enter new grades for {name} separated by spaces: ")
    new_grades_list = list(map(int, new_grades.split()))

    gradebook[name] = new_grades_list
    print(f"Grades for {name} updated to: {gradebook[name]}")
else:
    print(f"The name '{name}' does not exist in the gradebook.")

# 4
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

phonebook.clear()
print("Phonebook after deletion:", phonebook)

my_dict = dict({
    "apple": 5,
    "banana": 8,
    "orange": 3,
    "grapes": 6,
    "watermelon": 2
})

my_dict.clear()
print("Dictionary from Question 2 after deletion:", my_dict)

devices = {
    "router": "192.168.1.1",
    "switch": "192.168.1.2",
    "printer": "192.168.1.3",
    "laptop": "192.168.1.4"
}

devices.clear()
print("Devices dictionary after deletion:", devices)
