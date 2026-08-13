"""28.	Store scores of a batsman in 10 matches and calculate:
•	Highest score 
•	Lowest score 
•	Total runs 
•	Average runs 
•	Number of centuries (≥100) 
•	Number of half-centuries (50–99)
"""

scores = []

for i in range(10):
    score = int(input("Enter score: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
half = 0

for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half Centuries:", half)