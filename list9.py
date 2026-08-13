#9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list. 
cities = [ "Kolhapur", "Pune", "Mumbai", "Nagpur", "Nashik"]
user = input("Enter a city name :").title()
if user in cities:
    print("Entered city exists in the Cities list")
else:
    print("Entered city does not exist in the Cities list")