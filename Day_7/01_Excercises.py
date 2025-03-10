#Level 1
# # 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.update(['Twitter', 'Linkedin', 'Instagram'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('Google')
print(it_companies)

# 5. What is the difference between remove and discard
# remove() will raise an error if the element does not exist in the set
# discard() will not raise an error if the element does not exist in the set

#Level 2
# 1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.union(B))

# 2. Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.intersection(B))

# 3. Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.issubset(B))

# 4. Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.isdisjoint(B))

# 5. Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.union(B))
print(B.union(A))

# 6. What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.symmetric_difference(B))

# 7. Delete the sets completely
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
del A
del B

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


