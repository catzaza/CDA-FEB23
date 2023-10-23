# 3.	Write a program that asks the user to enter a person’s age.  
#       The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. 
#       Following are the guidelines:
#       -	 If the person is a year old or less, he or she is an infant.
#       -	 If the person is older than 1 year, but younger than 13 years, he or she is a child.
#       -	 If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#       -	 If the person is at least 20 years old, he or she is an adult.


# Prompt user to enter an age
age=int(input("Please enter the persons age: "))

# Create elif statments to check which group their age falls under
# Infant age <= 1
if age <= 1:
    print("He or she is an infant at", age, "years old.")

# Child age > 1 and age < 13
elif age > 1 and age < 13:
    print("He or she is a child at", age, "years old.")

# Teenager age >= 13 and age < 20
elif age >= 13 and age < 20:
    print("He or she is a teenager at", age, "years old.")

# Adult any other age
else:
    print("He or she is an adult at", age, "years old.")