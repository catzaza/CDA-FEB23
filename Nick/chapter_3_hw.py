# if/else/elif hw
# 1
a = 1 

if a == 1:
    print("a equals 1")
else:
    print("a is not equal to 1")

# 2
B = int(input("Enter a value: "))

if B < 10:
    print("Too small")
else:
    print("Perfect fit")

# 3
speed = int(input("Enter your driving speed: "))

if speed < 50:
    print("Speed in limit")
else:
    print("Speed should be checked")

# 4
age = int(input("Please enter your age: "))

if age <= 1:
    print("You are an infant.")
elif age > 1 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 5
points = 5

if points < 9 or points > 51:
    print("Invalid points")
else:
    print("Valid points")