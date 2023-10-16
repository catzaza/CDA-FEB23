# Task 1: Check if variable a is equal to 1
a = 1
if a == 1:
    print("a equals 1")
else:
    print("a is not equal to 1")

# Task 2: Input statement to get a value for variable B and check if it's less than 10
B = int(input("Enter a value for B: "))
if B < 10:
    print("Too small")
else:
    print("Perfect fit")

# Task 3: Check the user's driving speed
speed = int(input("Enter your driving speed: "))
if speed < 50:
    print("Speed in limit")
else:
    print("Speed should be checked")

# Task 4: Determine the age category
age = int(input("Enter your age: "))
if age <= 1:
    print("You are an infant")
elif 1 < age < 13:
    print("You are a child")
elif 13 <= age < 20:
    print("You are a teenager")
else:
    print("You are an adult")

# Task 5: Check if points are within the specified range
points = 5
if 9 <= points <= 51:
    print("Valid points")
else:
    print("Invalid points")
