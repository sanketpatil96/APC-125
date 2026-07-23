'''A company insures its drivers in the following cases:- If the driver is married.- If the driver is unmarried, male and above 30 years        
         of age.      - If the driver is unmarried, female and above 25 years of age.
         
        In all the other cases, the driver is not insured.        Write a PYTHON program to determine whether the driver     
        is insured or not
        1.create a program to calculate area triangle ,volume of circle and sphere,total suface area of cylender, area of square,
        2.wap to convert pounds into kg,km into miles 
        3.wap to calculate factorial number,to check whether the number is prime of not
        4.wap to check number is pallindrome or not
        5.wap to convert decimal to binary,decimal to octal,to hexadecimal
        6.wap to calculate factors of number
        7.wap to find ascii value of character
        
'''
age=int(input("Enter the age:"))
status=input("Enter the martial status(married/unmarried):")
gender=input("Enter the Gender(male/female):")
if status=='married':
    print("Driver is insured")
elif status=='unmarried' and gender=='male' and age>=30:
    print("Driver is insured")
elif status=='unmarried' and gender=='female' and age>=25:
    print("Driver is insured")
else:
    print("Driver is not insured..")









