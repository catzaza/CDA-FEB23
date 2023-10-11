# Write a program that displays the following information:
# •	Your name
# •	Your address, with city, state, and zip
# •	Your telephone numbers
# •	Your dream majors

# Collect and display personal information
print("When prompted below, please enter the requested information.")
print()
name = input("Enter your name: ")
address = input("Enter your address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zip_code = input("Enter your zip code: ")
telephone_numbers = input("Enter your telephone numbers (comma-separated): ")
dream_majors = input("Enter your dream majors (comma-separated): ")
print()
print()
print()

# Display the collected information
print("\nYour Information:")
print("Name:", name)
print("Address:", address)
print("City:", city)
print("State:", state)
print("Zip Code:", zip_code)
print()

# Split and display telephone numbers
telephone_numbers_list = telephone_numbers.split(',')
print("Telephone Numbers:")
for number in telephone_numbers_list:
    print("  ", number.strip())
print()

# Split and display dream majors
dream_majors_list = dream_majors.split(',')
print("Dream Majors:")
for major in dream_majors_list:
    print("  ", major.strip())
print()
print()
