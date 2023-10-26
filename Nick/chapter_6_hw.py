# files 1
ip_addresses = ["10.2.4.6", "10.10.160.23", "10.54.167.20"]

with open("addresses.txt", "w") as file:
    for ip in ip_addresses:
        file.write(ip + "\n")

with open("addresses.txt", "r") as file:
    contents = file.read()
    print("Contents of addresses.txt:")
    print(contents)

# 2


# 3
with open("helpdesk.txt", "w") as file:
    file.write("New Keyboard\n")
    file.write("New laptop screen\n")
    file.write("Five empty disks\n")

with open("helpdesk.txt", "r") as file:
    contents = file.read()
    print("Contents of helpdesk.txt:")
    print(contents)

# 4
devices = ["Laptop", "Smartphone", "Tablet", "Smart TV"]

with open("devices.txt", "w") as file:
    for device in devices:
        file.write(device + "\n")

with open("devices.txt", "r") as file:
    contents = file.read()
    print("Contents of devices.txt:")
    print(contents)

# 5
mac_address = "00:11:22:33:44:55"

with open("macaddress.txt", "w") as file:
    file.write(mac_address)