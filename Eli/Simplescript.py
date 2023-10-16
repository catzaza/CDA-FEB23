# 1. Check the name of user
# 2. If user is permitted, then allow access


bob="not allowed"
sam="allowed"
sarah="not allowed"


if sam == "allowed":
    print("Access Granted")
elif bob == "allowed":
    print("Access Granted")
elif sarah == "allowed":
    print("Access Granted")
else:
    print("Access Denied")

print("Thank you")

