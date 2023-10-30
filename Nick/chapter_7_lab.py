music = ['Michael Jackson', 'Beyoncé', 'The Beatles']

# lists lab 1
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

number_of_fruits = len(fruits)

print("The number of fruits in the list is:", number_of_fruits)

# 2
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

fruits.append('mango')

print("Updated list of fruits:", fruits)

# 3
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

combined_list = fruits + music

print("Combined list of fruits and music:", combined_list)

# 4
combined_list = ['apple', 'banana', 'orange', 'strawberry', 'kiwi', 'Michael Jackson', 'Beyoncé', 'The Beatles']

for item in combined_list:
    print(item)

# 5
sales_per_day = []

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days:
    sales = float(input(f"Enter sales for {day}: $"))
    sales_per_day.append(sales)

total_sales = sum(sales_per_day)

print(f"\nTotal sales for the week: ${total_sales:.2f}")
