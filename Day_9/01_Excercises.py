#Level 1
#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#Enter your age: 30
#You are old enough to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print("You need", 18 - age, "more years to learn to drive.")
    
#2. Compare the values of my_age and your_age using if/else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
my_age = 30
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print("I am older than you.")
elif my_age < your_age:
    print("You are older than me.")
else:
    print("We are of the same age.")
    
#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")

