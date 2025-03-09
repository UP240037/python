#Ejercicios level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Updated ages:", ages)

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Median age:", median_age)

# Find the average age
average_age = sum(ages) / n
print("Average age:", average_age)

# Find the range of the ages
age_range = max_age - min_age
print("Age range:", age_range)

# Compare the value of (min - average) and (max - average)
diff1 = abs(min_age - average_age)
diff2 = abs(max_age - average_age)
print("(Min - Average) =", diff1)
print("(Max - Average) =", diff2)
if diff1 > diff2:
    print("(Min - Average) is greater than (Max - Average)")
elif diff1 < diff2:
    print("(Max - Average) is greater than (Min - Average)")
else:
    print("(Min - Average) is equal to (Max - Average)")

countries ='https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py'

# Find the middle country(ies)
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
    print("Middle countries:", middle_countries)
else:
    middle_country = countries[middle_index]
    print("Middle country:", middle_country)

# Divide the countries list into two equal lists
middle_index = len(countries) // 2
first_half = countries[:middle_index + len(countries) % 2]
second_half = countries[middle_index + len(countries) % 2:]
print("First half:", first_half)
print("Second half:", second_half)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Unpack the first three countries and the rest as scandic countries
first_three, *scandic_countries = countries
print("First three countries:", first_three)
print("Scandic countries:", scandic_countries)
