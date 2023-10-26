# Task 1: Bug Collector
total_bugs = 0

for day in range(1, 6):
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_collected

print(f"Total bugs collected over 5 days: {total_bugs} bugs")

# Task 2: Pennies for Pay
days = int(input("Enter the number of days: "))
total_pay = 0

print("Day\tSalary")
print("---------------")

for day in range(1, days + 1):
    salary = 2 ** (day - 1)  # Calculate salary for the day
    total_pay += salary
    print(f"{day}\t${salary / 100:.2f}")

print(f"Total pay after {days} days: ${total_pay / 100:.2f}")

# Task 3: Tuition Increase
tuition = 8000  # Initial tuition for the first semester
tuition_increase = 0.03  # 3% increase each year

print("Year\tProjected Tuition")
print("-------------------------")

for year in range(1, 6):
    tuition += tuition * tuition_increase  # Calculate tuition for the year
    print(f"{year}\t${tuition:.2f}")

