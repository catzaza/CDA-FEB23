# Task 1: Day of the Week
day_number = int(input("Enter a number in the range of 1 through 7: "))

if 1 <= day_number <= 7:
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"The corresponding day of the week is {days_of_week[day_number - 1]}.")
else:
    print("Error: Please enter a number within the range of 1 through 7.")

# Task 2: Areas of Rectangles
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))
area1 = length1 * width1

length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))
area2 = length2 * width2

if area1 > area2:
    print("The first rectangle has a greater area.")
elif area2 > area1:
    print("The second rectangle has a greater area.")
else:
    print("Both rectangles have the same area.")

# Task 3: Age Classifier
age = int(input("Enter a person's age: "))

if age <= 1:
    print("The person is an infant.")
elif 1 < age < 13:
    print("The person is a child.")
elif 13 <= age < 20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")
