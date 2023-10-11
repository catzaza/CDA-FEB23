# Write a python code that will get 3 IP addresses from a user

# Create an empty list to store the IP addresses
ip_addresses = []

# Ask the user for 3 IP addresses
print()
print("Below, please enter three IP addresses.")
print()
for i in range(3):
    while True:
        ip = input(f"Enter IP address {i + 1}: ")
        # You can add validation here to ensure that the input is a valid IP address.
        # You can use regular expressions or other methods to validate the format.

        if len(ip.split(".")) == 4:
            valid = True
            for octet in ip.split("."):
                if not octet.isdigit() or not 0 <= int(octet) <= 255:
                    valid = False
                    break
            if valid:
                break

        print("Invalid IP address format. Please enter a valid IP address (e.g., 192.168.1.1).")

    ip_addresses.append(ip)

# Print the list of IP addresses
print("You entered the following IP addresses:")
for i, ip in enumerate(ip_addresses):
    print(f"IP address {i + 1}: {ip}")
