# bug collector
total_bugs = 0

for day in range(1, 6):
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_collected

print(f"Total bugs collected over five days: {total_bugs}")

# pennies for pay
num_days = int(input("Enter the number of days: "))

total_pay = 0
salary = 0.01  

print("Day\tSalary (in dollars)")

for day in range(1, num_days + 1):
    total_pay += salary
    print(f"{day}\t${salary:.2f}")
    salary *= 2  

print(f"Total pay over {num_days} days: ${total_pay:.2f}")

# tuition increase
tuition = 8000  

num_years = 5

print("Year\tTuition (per semester)")

for year in range(1, num_years + 1):
    print(f"{year}\t${tuition:.2f}")
    tuition += tuition * 0.03