# Task 1: Loop through and print your first name
first_name = "Myblog"
for letter in first_name:
    print(letter)

# Task 2: Loop through the name ANONYMOUS and print
name = "ANONYMOUS"
for letter in name:
    print(letter)

# Task 3: Loop through numbers in the range 1-5
for number in range(1, 6):
    print(number)

# Task 4: Use a while loop to ask for your name and print 'WRONG NAME' if the input is wrong
correct_name = "YourName"
user_input = input("Enter your name: ")
while user_input != correct_name:
    print("WRONG NAME")
    user_input = input("Enter your name: ")
print("Welcome, YourName!")

# Task 5: Create an infinite while loop
import time

while True:
    print("This is an infinite loop. Press Ctrl+C to stop.")
    time.sleep(1)  # Sleep for 1 second before repeating
