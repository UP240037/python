#Level 1
#Ejercicio 1
empty_tuple = ()
print(empty_tuple)

#Ejercicio 2
siblings = ("Sarahi", "Yamileth", "Monse", "Carlos")
print(siblings)

#Ejercicio 3
siblings = ("Sarahi", "Yamileth", "Monse", "Carlos")
print(siblings[1])

#Ejercicio 4
print(len(siblings)) 

#Ejercicio 5
siblings = ("Sarahi", "Yamileth", "Monse", "Carlos")
father = "Martin"
mother = "Cecilia"

# Add the names of your father and mother to the siblings tuple
family_members = (father, mother) + siblings
print(family_members)


#Level 2
#Ejercicio 1
family_members = ("Martin", "Cecilia", "Sarahi", "Yamileth", "Monse", "Carlos")

# Unpack parents and siblings
parents, *siblings = family_members
print("Parents:", parents)
print("Siblings:", siblings)

#Ejercicio 2
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "cauliflower")
animal_products = ("milk", "eggs", "honey")

# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Ejercicio 1
# Convert the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Ejercicio 2
# Slice the food_stuff_lt list and print the sliced list
fruits = food_stuff_lt[0:3]
vegetables = food_stuff_lt[3:6]
animal_products = food_stuff_lt[6:9]
print(fruits)
print(vegetables)
print(animal_products)


#Ejercicio 3
# Slice out the first three items
first_three_items = food_stuff_lt[:3]
print("First three items:", first_three_items)

# Slice out the last three items
last_three_items = food_stuff_lt[-3:]
print("Last three items:", last_three_items)

del food_stuff_tp
my_tuple = (1, 2, 3, 4, 5)

# Check if an item exists in the tuple
item_to_check = 3
print(item_to_check in my_tuple)  # Output: True

item_to_check = 6
print(item_to_check in my_tuple)  # Output: False

# Check if an item exists in the nordic_countries tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)