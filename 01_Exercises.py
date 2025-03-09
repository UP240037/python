#Ejercicio 1
my_empty_list = []
#Ejericio 2
my_empty_list.append('apple')
my_empty_list.append('banana')
my_empty_list.append('orange')
my_empty_list.append('mango')
my_empty_list.append('lemon')
#Ejercicio 3 y 4
print(my_empty_list[0])
print(my_empty_list)
my_empty_list.insert(2, 'lime')
print(my_empty_list)
my_empty_list.remove('apple')
print(my_empty_list)
my_empty_list.pop()
print(my_empty_list)
del my_empty_list[0]
print(my_empty_list)
my_empty_list.clear()
print(my_empty_list)

#Ejercicio 5
mixed_data_types = {
    "Name": "John Doe",
    "Age": 30,
    "Height": 1.75,
    "Marital Status": "Single",
    "Address": "123 Main St, Mexico City",
}
print(mixed_data_types["Name"])
print(mixed_data_types["Age"])
print(mixed_data_types["Height"])
print(mixed_data_types["Marital Status"])
print(mixed_data_types["Address"])

#Ejercicio 6-17
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list
print(it_companies)

# Print the number of companies
print(len(it_companies))

# Print the first, middle, and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# Modify one of the companies
it_companies[0] = "it_companies[0].upper()"
print(it_companies)

# Add an IT company
it_companies.append("Twitter")
print(it_companies)

# Insert an IT company in the middle
it_companies.insert(len(it_companies) // 2, "Tesla")
print(it_companies)

# Change one of the company names to uppercase
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;&nbsp; '
joined_string = '#;&nbsp; '.join(it_companies)
print(joined_string)

# Check if a certain company exists in the it_companies list
company = "Microsoft"
if company in it_companies:
    print(f"{company} exists in the list.")
else:
    print(f"{company} does not exist in the list.")

# Sort the list using sort() method
it_companies.sort()
print("Sorted list:", it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Reversed list:", it_companies)

#Ejercicio 18-20
# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print("First three companies:", first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Last three companies:", last_three_companies)

# Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies) // 2]
print("Middle company:", middle_company)

#Ejercicio 21-25
# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Ejercicio 26-27
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 23. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)