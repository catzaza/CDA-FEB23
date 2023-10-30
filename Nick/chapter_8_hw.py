# strings 1
word = "Hippopotamus"

for char in word:
    print(char)

# 2
word = "Hippopotamus"

print("Character at index 6:", word[6])

print("Character at index 8:", word[8])

# 3
user_string = input("Enter a string: ")

string_length = len(user_string)

print(f"The length of the entered string is: {string_length}")

# 4
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

full_name = name1 + " " + name2

print("Combined names:", full_name)

# 5
full_name = 'Patty Lynn Smith'

names = full_name.split()

middle_name = names[len(names) // 2]

print("Middle Name:", middle_name)
