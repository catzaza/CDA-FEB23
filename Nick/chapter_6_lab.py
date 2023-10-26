# files 1
with open("helpdesk.txt", "w") as file:
    file.write("New Keyboard\n")
    file.write("New laptop screen\n")
    file.write("Five empty disks\n")

with open("helpdesk.txt", "r") as file:
    contents = file.read()
    print("Contents of helpdesk.txt:")
    print(contents)

# files 2
devices = ["Laptop", "Smartphone", "Tablet", "Smart TV"]

with open("devices.txt", "w") as file:
    for device in devices:
        file.write(device + "\n")

with open("devices.txt", "r") as file:
    contents = file.read()
    print("Contents of devices.txt:")
    print(contents)

# files 3
mac_address = "00:11:22:33:44:55"

with open("macaddress.txt", "w") as file:
    file.write(mac_address)

with open("macaddress.txt", "r") as file:
    mac_address_read = file.read()
    print("Device MAC address from macaddress.txt:", mac_address_read)