#Write a PYTHON program to check a year for leap year.
year=int(input("Enter the Year:"))
if year %4==0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")
