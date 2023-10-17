wish_list = []

# enter 5 items
for i in range(5):
    item = input(f"Enter item {i + 1}: ")
    wish_list.append(item)

# items the user wants to buy
print("\nItems you want to buy:")
for item in wish_list:
    print(item)


