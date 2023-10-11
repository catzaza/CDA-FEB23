# Write a python code that will get input from a user asking for 5 items they would like to buy
# from the web.

# Initialize an empty list to store the items
items = []

# Ask the user for 5 items
print("Below, please list five things you would like to buy online.")
for i in range(5):
    item = input(f"Item {i + 1}: ")
    items.append(item)

# Print the list of items
print("You want to buy the following items:")
for i, item in enumerate(items):
    print(f"{i + 1}. {item}")
