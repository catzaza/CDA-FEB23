# Question 1
# Write an if statement that checks if the variable a is equal to 1. 
# If it is equal to 1, print a message saying ‘a equals 1’, 
# else print ‘a is not equal to 1’

# Let's set the variable
a = 1

# Let's set the rules
if(a == 1):
    print('a is equal to 1')

else:
    print('a is not equal to 1')






# Question 2
# Asking a user to enter their age
age = int(input('What is your age?: '))

# if-else statement pertaining to the answer
if age >= 50: 
    print('You are getting there')
else: 
    print('You are healthy and aging gracefully!')






# Question 3
# Ask the price of 5 items, 
# Then calculate the sales tax and total. 

# Let's define some variables
sales_tax = 0.07
subtotal = 0.0

# Create a loop that asks fro thr price of each item.
# Used a for loop for this, as well as the '+=', which
# is an assignment operator used to 
for i in range (5):
    item_price = float(input(f'What is the price of the item? {i + 1}: $'))
    subtotal += item_price

# Let's calculate the sales tax and the total
sales_tax = subtotal * sales_tax
total = subtotal + sales_tax

# Now we just need to display everything
print(f'subtotal: ${subtotal:.2f}')
print(f'sales_tax: ${sales_tax:.2f}')
print(f'total: ${total:.2f}')

# After many syntax errors, I got this to run correctly. 








# Question 4
# It's wanting the inputs for the length and width
# of 2 triangles, and then we need to spit out the area for
# each, and to print out which one has the greater area.

# Let's start with getting the lengths and widths of each rectangle
rectangle_1_width = float(input("What is the width of the 1st rectangle? "))
rectangle_1_length = float(input("What is the length of the 1st triangle? "))
rectangle_2_width = float(input("What is the width of the 2nd triangle? "))
rectangle_2_length = float(input("What is the length of the 2nd triangle? "))

# Now let's define the areas of each so that we can compare
rectangle_1_area = rectangle_1_width * rectangle_1_length
rectangle_2_area = rectangle_2_width * rectangle_2_length

# Let's compare the two. We will use if-else-elif statements for this
if rectangle_1_area > rectangle_2_area:
    print("Rectangle 1 has a greater area.")
elif rectangle_1_area < rectangle_2_area:
    print("Rectangle 2 has a greater area.")
else:
    print("The rectangles have the same area.")







# Question 5
# Asking a user about their driving speed. 
# If the speed is no more than 50, print "Speed in limit"
# If the speed is over, print "Slow the hell down!"

speed = float(input("Dude, what speed are you going right now? "))
if speed <= 50:
    print("Speed in limit")
else:
    print("Slow the hell down! You know that little Johnny was just hit by a truck the other day, it took forever to clean up his remains off of the pavement./n"
          "I'll never forget that day. It's something that you just can't unsee.")
    





# Question 6
# This one is pretty straight forward.
# Assign the variable 'total' the sum of 10 and 14
total = 10 + 14







# Question 7
# Use the input function to asks for a users
# name and then prints it out. 

print(input("Yooooooo, what's up! What's your name, fellow earthling? "))






# Question 8 
# This question is quite similar to question 3. Why?
# Oh well, here's some copy & pasted code from that question. 
# Ask the price of 5 items, 
# then calculate the sales tax and total. 

# Let's define some variables
sales_tax = 0.07
subtotal = 0.0

# Create a loop that asks fro thr price of each item
# Used a for loop for this, as well as the '+=', which
# is an assignment operator used to add things together. 
for i in range (5):
    item_price = float(input(f'What is the price of the item? {i + 1}: $'))
    subtotal += item_price

# Now we just need to display the subtotal
print(f'subtotal: ${subtotal:.2f}')






# Question 9
# Creating a name variable and then assigning my name to it, 
# then printing out the variable output. Thanks for the hint
# on this one. Where was the hint on question 3?!?! Haha
name = "Billy Bob the Bitcoiner"
print(name)







# Question 10
# Writing a statement that gets a value from the user. 
# Add an if-else statement to check the variable. 
B = int(input("Enter a value: ")) 

if B < 10:
    print('Too small')
else:
    print('Perfect fit')
