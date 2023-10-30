# lists and tuples 1
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

music = ['Michael Jackson', 'Beyoncé', 'The Beatles']

# 2
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

number_of_fruits = len(fruits)

print("The number of fruits in the list is:", number_of_fruits)

# 3
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

fruits.append('pineapple')

print("Updated list of fruits:", fruits)

# 4
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

combined_list = fruits + music

print("Combined list of fruits and music:", combined_list)

# 5
combined_list = ['apple', 'banana', 'orange', 'strawberry', 'kiwi', 'Michael Jackson', 'Beyoncé', 'The Beatles']

for item in combined_list:
    print(item)
