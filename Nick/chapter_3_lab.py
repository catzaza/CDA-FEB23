# day of the week
user_input = input("Enter a number in the range of 1 through 7: ")

try:
    number = int(user_input)

    
    if 1 <= number <= 7:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = days_of_week[number - 1]
        print(f"The corresponding day of the week is {day}.")
    else:
        print("Error: Please enter a number in the range of 1 through 7.")
except ValueError:
    print("Error: Please enter a valid integer.")

# area of triangles
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print("The first rectangle has a greater area.")
elif area2 > area1:
    print("The second rectangle has a greater area.")
else:
    print("Both rectangles have the same area.")

# age classifier
age = int(input("Enter a person's age: "))

if age <= 1:
    category = "infant"
elif age > 1 and age < 13:
    category = "child"
elif age >= 13 and age < 20:
    category = "teenager"
else:
    category = "adult"

print(f"The person is an {category}.")
