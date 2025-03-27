#1. Writ a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id():
    caracteres = string.ascii_letters + string.digits
    random_user_id = ''.join((random.choice(caracteres)) for _ in  range (6))
    return random_user_id
print('User ID:',random_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    caracteres = string.ascii_letters + string.digits

    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(caracteres) for _ in range(num_chars))
        user_ids.append(user_id)

    return user_ids

print("Generated User IDs:", user_id_gen_by_user())

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)  # Generate a random value for red
    g = random.randint(0, 255)  # Generate a random value for green
    b = random.randint(0, 255)  # Generate a random value for blue
    return f"rgb({r}, {g}, {b})"
print("Generated RGB Color:", rgb_color_gen())
