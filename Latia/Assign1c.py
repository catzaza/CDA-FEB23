# import modules to validate ip adds
import ipaddress
# create list to store ip adds
ip_addresses = []
# 'for' to loop 3 times for 3 ip add input
for i in range(3):
    while True:
        try:    # use 'input()' to prompt user for ip adds and store it in variable
            ip = input(f"Enter IP address {i + 1}: ")
            ip = ipaddress.ip_address(ip)
            ip_addresses.append(str(ip))
            break
        except ValueError:   # promt except to msg user that input is invalid 
            print("Invalid IP address. Please enter valid IP address.")

print("You entered the following IP addresses:")
for i, ip in enumerate(ip_addresses, start=1):
    print(f"IP address {i}: {ip}")
