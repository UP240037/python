#1. Filter only negative and zero in the list using list comprehension
number  =  [-4,-3,-2,-1,-0,2,4,6]
filtered_numbers  =  [num for num in number if num <=0]
print(filtered_numbers)

#2. Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

filtered_list = [item for sublist in list_of_lists for item in sublist[0]]

print(filtered_list)

#3. Using list comprehension create the following list of tuples:
numbers = [(i,1, i**2,i**3,i**4,i**5) for i in range(0,11)]
print(numbers) 

#4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_codes = {
    'Finland': 'FIN',
    'Sweden': 'SWE',
    'Norway': 'NOR'
}

transformed_countries = [
    [country[0].upper(), country_codes[country[0]], country[1].upper()]
    for sublist in countries for country in sublist
]

print(transformed_countries)

#5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_list = [{'country': item[0][0].upper(), 'city': item[0][1].upper()} for item in countries]

print(dict_list)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

list_names = [item[0][0] + " " + item[0][1] for item in names ]
print(list_names)


#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
pendiente = lambda x1,x2,y1,y2 : (y2-y1) / (x2-x1)

interseccion_y = lambda m,x1,y1 : y1-m*x1

x1,y1,x2,y2 = 1,2,3,6

m = pendiente(x1,x2,y1,y2)

print('La pendiente es:',m)

b = interseccion_y(m,x1,y1)

print('La interseccion es:',b )