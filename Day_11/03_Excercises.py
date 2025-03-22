#Level 3
#1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if number <= 1:
        return False  
    for i in range(2, int(number ** 0.5) + 1):  
        if number % i == 0:
            return False  
    return True

print(is_prime(2))   
print(is_prime(4))   
print(is_prime(17))  
print(is_prime(1)) 

#1. Write a functions which checks if all items are unique in the list.
def are_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_items_unique([1, 2, 3, 4]))  
print(are_items_unique([1, 2, 2, 4])) 
print(are_items_unique([]))           
print(are_items_unique(["a", "b", "c", "a"]))  

#1. Write a function which checks if all the items of the list are of the same data type.
def are_items_same_type(lst):
    if not lst: 
        return True
    first_type = type(lst[0])  
    return all(type(item) == first_type for item in lst)

print(are_items_same_type([1, 2, 3, 4]))     
print(are_items_same_type(["a", "b", "c"]))    
print(are_items_same_type([1, "b", 3.0]))      
print(are_items_same_type([])) 

#1. Write a function which check if provided variable is a valid python variable
import keyword

def is_valid_variable(var_name):

    if not var_name.isidentifier(): 
        return False
    if var_name in keyword.kwlist:  
        return False
    return True

print(is_valid_variable("variable"))   
print(is_valid_variable("123abc"))    
print(is_valid_variable("for"))       
print(is_valid_variable("_valid_var")) 

#1. Go to the data folder and access the countries-data.py file.
#- Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#- Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
from collections import Counter

def most_spoken_languages(countries_data, top_n=10):
    language_counter = Counter()
    for country in countries_data:
        for language in country['languages']:
            language_counter[language] += 1
    return language_counter.most_common(top_n)

def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]
