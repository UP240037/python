#Level 2
#1. Write a code which gives grade to students according to their marks:
#marks greater than or equal to 90 then A grade
#marks between 80 and 90 then B grade
#marks between 70 and 80 then C grade
#marks between 60 and 70 then D grade
#marks less than 60 then F grade
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
elif marks >= 70:
    print("C grade")
elif marks >= 60:
    print("D grade")
else:
    print("F grade")

#2. Check the season depending on the month and day
#Spring runs from March 20 to June 20
#Summer runs from June 21 to September 21
#Fall (autumn) runs from September 22 to December 20
#Winter runs from December 21 to March 19
month = input("Enter the month: ")
day = int(input("Enter the day: "))
if month == "March":
    if day >= 20:
        print("Spring")
    else:
        print("Winter")
elif month == "April" or month == "May":
    print("Spring")
elif month == "June":
    if day < 21:
        print("Spring")
    else:
        print("Summer")
elif month == "July" or month == "August":
    print("Summer")
elif month == "September":
    if day < 22:
        print("Summer")
    else:
        print("Fall")
elif month == "October" or month == "November":
    print("Fall")
elif month == "December":
    if day < 21:
        print("Fall")
    else:
        print("Winter")
elif month == "January" or month == "February":
    print("Winter")
else:
    print("Invalid month")

#3. The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print(fruits)
