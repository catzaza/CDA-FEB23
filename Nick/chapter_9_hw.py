# dictionaries 1
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

print(phonebook)

# 2
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

user_key = input("Enter a name to check in the phonebook: ")

if user_key in phonebook:
    print(f"The phone number for {user_key} is {phonebook[user_key]}.")
else:
    print(f"The name '{user_key}' does not exist in the phonebook.")

# 3
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

phonebook.update({
    "David": "111-222-3333",
    "Emma": "444-555-6666",
    "Frank": "777-888-9999",
    "Grace": "333-111-0000"
})

print(phonebook)

# 4
my_dict = dict({
    "apple": 5,
    "banana": 8,
    "orange": 3,
    "grapes": 6,
    "watermelon": 2
})

for key in my_dict:
    print(key)

# 5
my_dict = dict({
    "apple": 5,
    "banana": 8,
    "orange": 3,
    "grapes": 6,
    "watermelon": 2
})

for value in my_dict.values():
    print(value)
