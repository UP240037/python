#Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print(len(ages) > len(ages_set))

# Explain the difference between the following data types: string, list, tuple and set
# string: a sequence of characters enclosed in single or double quotes
# list: a collection of elements enclosed in square brackets, mutable
# tuple: a collection of elements enclosed in parentheses, immutable
# set: a collection of unique elements enclosed in curly braces

# 2. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
unique_words = set(words)
print(len(unique_words))
