# 1. Iterate 0 to 10 using for loop, do the same using while loop.
print("Iterate 0 to 10 using for loop")
i = 0
while i < 11:
    print(i)
    i += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print("Iterate 10 to 0 using for loop")
i = 10
while i >= 0:
    print(i)
    i -= 1


# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("Triangle")
for i in range(1, 8):
    print("*" * i)

# 4. Use nested loops to create the following:
print("Nested loop")
for i in range(1, 8):
    print(str(i) * i)

# 5. Print the following pattern:
print("Print the following pattern")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("Iterate through the list")
list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in list:
    print(item)

# 7. Use while loop to iterate from 0 to 100. Print all even numbers.
print("Print all even numbers")
i = 0
while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
print("Print only odd numbers")
for i in range(101):
    if i % 2 != 0:
        print(i)
