#ejercicio 1

result = ''.join(['Thirty' , 'days' , 'of', 'Python'])
print(result)

#ejercicio 2
a= 'coding'                
print(a)                        
b = 'for'  
print(b)
c = 'all'
print(c)      
sentence = "Coding for all"
print(sentence)

#ejercicio 3
company = "Coding For All"

#ejercicio 4
print(company)

#ejercicio 5
print(len(company))

#ejercicio 6
print(company.upper())

#ejercicio 7
print(company.lower())

#ejercicio 8
print(company.capitalize())
print(company.title())    
print(company.swapcase())

#ejercicio 9
eliminar_primera = '' .join(company.split()[1:])
print(eliminar_primera)

#ejercicio 10
print('Coding' in company)
print(company.find('Coding'))
if(company.index('Coding')):
    print('Coding')


#ejercicio 11
print(company.replace('Coding', 'Python'))

#ejercicio 12
print(company.replace('Coding For All', 'Python For Everyone'))
print(company.replace(' ', ''))

#ejercicio 13
print(company.split())

#ejercicio 14
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))

#ejercicio 15
print(company[0])

#ejercicio 16
print(company[len(company)-1])

#ejercicio 17
print(company[10])

#ejercicio 18
company1 = 'Python For Everyone'
print(company1[0], company1[7], company1[11])
acronimo = company1[0] + company1[7] + company1[11]
print(acronimo)

#ejercicio 19
acronimo = "".join([word[0] for word in company1.split()])
print(acronimo)

#ejercicio 20
print(company.index('C'))

#ejercicio 21
print(company.index('F'))

#ejercicio 22
print(company.index('l'))

#ejercicio 23
challenge = 'You cannot end a sentence with because because because is a conjunction'
print(challenge.find('because'))  
print(challenge.find('because', 6))  
print(challenge.find('because', 25))  
print(challenge.find('because', 50))

#ejercicio 24
sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.rindex('because')
print(position)

#ejercicio 25
print(challenge.find('because'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[sentence.index('because'):sentence.rindex('because') + len('because')]
print(phrase)

#ejercicio 26
sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.find('because')
print(position)

#ejercicio 27
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase_start = sentence.find('because')
phrase_end = phrase_start + len('because because because')
phrase = sentence[phrase_start:phrase_end]
print(phrase)

#ejercicio 28
substring = "Coding"
string = "'Coding For All'"
if string.startswith(substring):
    print("The string starts with the substring.")
else:
    print("The string does not start with the substring.")


#ejercicio 29
substring = "Python"
string = "'Python For Everyone'"
if string.endswith(substring):
    print("The string ends with the substring.")
else:
    print("The string does not end with the substring.")

#ejercicio 30
string = "&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;"
stripped_string = string.strip()
print(stripped_string)

#ejercicio 31
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1.isidentifier())  # Output: True
print(var2.isidentifier())  # Output: True

#ejercicio 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(libraries)
print(joined_string)

#ejercicio 33
print("I am enjoying this challenge.\nI just wonder what is next.")

#ejercicio 34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#ejercicio 35
radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")

#ejercicio 36
num1 = 8
num2 = 6

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")















