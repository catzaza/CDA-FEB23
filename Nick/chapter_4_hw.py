# for loop 1
first_name = "John"

for character in first_name:
    print(character)

# for loop 2
name = "ANONYMOUS"

for character in name:
    print(character)

# for loop 3
for number in range(1, 6):
    print(number)

# while loop
expected_name = "Nick"  

while True:
    user_name = input("Please enter your name: ")
    
    if user_name == expected_name:
        print("Correct Name!")
        break
    else:
        print("WRONG NAME")

# while loop 2
while True:
    pass