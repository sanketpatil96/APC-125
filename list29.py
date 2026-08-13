"""29.	Store the temperature of 30 days and determine:
•	Hottest day 
•	Coldest day 
•	Average temperature 
•	Days above average temperature 
•	Days below average temperature
"""
# Store temperature of 30 days

temp = []

for i in range(30):
    t = float(input("Enter temperature: "))
    temp.append(t)

highest = max(temp)
lowest = min(temp)
average = sum(temp) / len(temp)

above = 0
below = 0

for i in temp:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Hottest Day Temperature:", highest)
print("Coldest Day Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)