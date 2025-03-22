# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    return a + b

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.

import math

def area_of_circle(r):
    return math.pi * r * r

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        return "All arguments must be numbers."
    return sum(args)

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    elif month in ['september', 'october', 'november']:
        return "Autumn"
    else:
        return "Invalid month"
    
#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
import math

def solve_quadratic_eqn(a, b, c):
    determinant = b**2 - 4*a*c
    
    if determinant < 0:
        return []
    
    elif determinant == 0:
        solution = -b / (2*a)
        return [solution]

    else:
        solution1 = (-b + math.sqrt(determinant)) / (2*a)
        solution2 = (-b - math.sqrt(determinant)) / (2*a)
        return [solution1, solution2]
    
#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for item in list:
        print(item)

number_list = [1, 2, 3, 4, 5]
print_list(number_list)
    
#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list
numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))  # Output: [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    capitalized_list = [item.capitalize() for item in list]
    return capitalized_list
items = ["apple", "banana", "cherry"]
print(capitalize_list_items(items))

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(input_list, item):
    input_list.extend([item])
    return input_list

food_staff = ['Potato', 'Tomato', 'Pepper', 'Carrot']
print(add_item(food_staff, 'Meat'))  # Output: ['Potato', 'Tomato', 'Pepper', 'Carrot', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) 

#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

vegetables = ['Potato', 'Tomato', 'Pepper', 'Carrot']
print(remove_item(vegetables, 'Tomato'))  # Output: ['Potato', 'Pepper', 'Carrot']

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 7))  # Output: [2, 3, 9]
print(remove_item(numbers, 10))  # Output: [2, 3, 9] (item not found)

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_of_numbers(5))  # Output: 15
print(sum_of_numbers(10))  # Output: 55 
print(sum_of_numbers(100)) # 5050

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  
            total += i
    return total

print(sum_of_odds(5))  # Output: 9 (1 + 3 + 5)
print(sum_of_odds(10))  # Output: 25 (1 + 3 + 5 + 7 + 9)

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    
    total = 0
    for i in range(0, n + 1):
        if i % 2 == 0:  # Check if the number is even
            total += i
    return total

print(sum_of_even(5))  # Output: 6 (0 + 2 + 4)
print(sum_of_even(10))  # Output: 30 (0 + 2 + 4 + 6 + 8 + 10)