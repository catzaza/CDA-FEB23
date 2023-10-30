# sets 1
new = {10, 20, 30, 40, 50}

for value in new:
    print(value)

# 2
empty = set()

empty.add(42)
empty.add("apple")
empty.add(3.14)
empty.add(True)
empty.add((1, 2, 3))

for value in empty:
    print(value)

# 3
my_set = {10, 20, 30, 40, 50}

user_value = input("Enter a value to check in the set: ")

if user_value in my_set:
    print(f"The value '{user_value}' is in the set.")
else:
    print(f"The value '{user_value}' is not in the set.")

# 4 
my_set = {10, 20, 30, 40, 50}

my_set.remove(30)
my_set.remove(40)

print("Set after removal:", my_set)

# 5
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

combined_set = set1 | set2

print("Combined set using union operator:", combined_set)
