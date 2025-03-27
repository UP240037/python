#Level 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(num_colors):
    hexa_colors = []
    for _ in range(num_colors):
        color = f"#{''.join(random.choice('0123456789abcdef') for _ in range(6))}"
        hexa_colors.append(color)
    return hexa_colors

print(list_of_hexa_colors(5))  # Output: ['#a3e12f', '#03f4b2', '#f1c232', '#bada55', '#c0ffee']

#1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r}, {g}, {b})"
        rgb_colors.append(color)

#1. Write a function generate_colors which can generate any number of hexa or rgb colors.
import random

def generate_colors(color_type, num_colors):
    colors = []
    
    if color_type == 'hexa':
        for _ in range(num_colors):
            color = f"#{''.join(random.choice('0123456789abcdef') for _ in range(6))}"
            colors.append(color)
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f"rgb({r}, {g}, {b})"
            colors.append(color)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."
    
    return colors

print(generate_colors('hexa', 3))  # Output: ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('rgb', 3))   # Output: ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)']
