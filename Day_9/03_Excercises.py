#Level 3
#1 Here we have a person dictionary. Feel free to modify it!

#1.1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': '250',
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    skills = person['skills']
    length = len(skills)
    if length % 2 == 0:
        print(skills[length // 2 - 1])
    else:
         print(skills[length // 2])


#1.2 If the person has 'skills' key, check if the person has the 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person doesn't have Python skill.")

#1.3 If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills = person['skills']
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer.")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer.")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

#1.4 If the person is married and if he lives in Finland, print the information in the following format:
#Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], "lives in", person['country'], ". He is married.")
else:
    print("The person is not married or doesn't live in Finland.")





