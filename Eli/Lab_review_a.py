#1.	At one college, the tuition for a full-time student is $8,000 per semester. 
#It has been announced that the tuition will increase by 3 percent each year for the next 5 years. 
#Write a program with a loop that displays the projected semester tuition amount for the next 5 years.

# Set the current tuition and the place holder for the projected tuition
tuition=int(8000)
projectedTuition=[]

# Do the calculation for the first year's increase by multiplaying the current tution by 3% (or 1.03)
projectedTuition.append(int(tuition*1.03))

# Loop through the remaining 4 years calculating for each year's new total
for i in range(0, 4):
    projectedTuition.append(int(projectedTuition[i]*1.03))

# Display each years increase indiviually
print("Tuition will increase to this amount over 5 years:")
for i in range(0, len(projectedTuition)):
    print("Year", i+1, ":", projectedTuition[i])

# Calculate the total after 5 years by adding each year total, including the current tuition
totalTuition=tuition+projectedTuition[0]
for i in range(1, len(projectedTuition)):
    totalTuition=totalTuition+projectedTuition[i]

# Finally Display the total tuition after the 5 years (6 years in total)
print()
print("Total Tuition after 5 years:")
print("Total:", "$"+str(totalTuition))