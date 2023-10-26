import ipaddress

# Create an empty list to store the valid IP addresses
ip_addresses = []

# Gather 3 valid IP addresses from the user
for i in range(3):
    while True:
        ip = input(f"Enter IP address {i + 1}: ")
        try:
            # Check if the entered IP address is valid
            ip_obj = ipaddress.IPv4Address(ip)
            ip_addresses.append(str(ip_obj))  # Convert to string to store in the list
            break  # Exit the loop if a valid IP is provided
        except ipaddress.AddressValueError:
            print("Invalid IP address. Please try again.")

# Display the gathered valid IP addresses
print("You have entered the following valid IP addresses:")
for ip in ip_addresses:
    print(ip)