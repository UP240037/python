#Level 2 

#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):

    evens = 0
    odds = 0
    for i in range(0, n + 1):
        if i % 2 == 0:  
            evens += 1
        else: 
            odds += 1
    return {"evens": evens, "odds": odds}

result = evens_and_odds(100)
print(f"The number of evens are {result['evens']}.")  
print(f"The number of odds are {result['odds']}.")  

#1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):

    if n == 0 or n == 1: 
        return 1
    result = 1
    for i in range(2, n + 1): 
        result *= i
    return result

print(factorial(5))  
print(factorial(0))  
print(factorial(10)) 

#1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
def _is_empty_(param):
    """
    This function takes a parameter and checks if it is empty or not.
    Returns True if empty, otherwise False.
    """
    return not bool(param)

print(_is_empty_([]))      
print(_is_empty_({}))       
print(_is_empty_(""))       
print(_is_empty_([1, 2]))   
print(_is_empty_("Hello"))  

#1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
from statistics import mean, median, mode, variance, stdev

def calculate_mean(lst):
    return mean(lst)

def calculate_median(lst):
    return median(lst)

def calculate_mode(lst):
    return mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return variance(lst)

def calculate_std(lst):
    return stdev(lst)

numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print("Mean:", calculate_mean(numbers))          
print("Median:", calculate_median(numbers))      
print("Mode:", calculate_mode(numbers))         
print("Range:", calculate_range(numbers))       
print("Variance:", calculate_variance(numbers)) 
print("Std Dev:", calculate_std(numbers)) 