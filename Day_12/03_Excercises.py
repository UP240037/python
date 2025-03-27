#Level 3
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst):
    shuffled = lst[:] 
    random.shuffle(shuffled)  
    return shuffled
original_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(original_list)
print("Original List:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Shuffled List:", shuffled_list)  # Output: [3, 1, 5, 2, 4] 

#1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())  # Output: [3, 7, 1, 9, 0, 5, 8] 