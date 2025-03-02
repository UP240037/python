#ejercicio 1
my_age = 18 

#ejercicio 2
my_height = 1.67

#ejercicio  3
my_complex_number = 3 + 4j

#ejercicio 4
def calcular_area_triangulo():
    """Calcula el área de un triángulo a partir de la base y la altura."""

    try:
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))

        area = 0.5 * base * altura
        print(f"El área del triángulo es: {area}")
```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

#ejercicio 5
def calcular_perimetro_triangulo():

    try:
        lado_a = float(input("Introduce la longitud del lado a: "))
        lado_b = float(input("Introduce la longitud del lado b: "))
        lado_c = float(input("Introduce la longitud del lado c: "))

        perimetro = lado_a + lado_b + lado_c
        print(f"El perímetro del triángulo es: {perimetro}")


```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

#Ejercicio 6
width= float(input('Dame el ancho del rectengulo:'))
length = float(input('Dame el largo del rectangulo: '))

print('El area del rectangulo es de: ', width*length)
print('El perimetro del rectangulo es de:', 2(width+length))

#Ejercicio 7
def calculate_circle_area_circumference():
    """Calcula el area y la circunferencia de un circulo."""

    pi = 3.14  # Define pi

    try:
        radio = float(input("Introduce el radio del circulo: "))

        area = pi * radio * radio
        circumference = 2 * pi * radio

        print(f"el area del circulo es: {area}")
        print(f"la circunferencia del circulo: {circumference}")

def calculate_line_properties(slope, y_intercept_val):
    """calcula la pendiente, la interseccion con el eje x y la interseccion con el eje y de una linea."""

    print(f"Slope (m): {slope}")
    print(f"Y-intercept (b): {y_intercept_val}")

    # Calcular la interseccion con el eje x
    x_intercept = -y_intercept_val / slope
    print(f"X-intercept: ({x_intercept}, 0)")

#Ejercicio 8
# Ecuacion: y = 2x - 2
slope = 2
y_intercept = -2

#ejercicio 9

print('La pendiente de es de:',(y2-y1)/(x2-x1))
#pendiente con los puntos (2,2) (6,10) 9
x1,y1= 2,2
x2,y2=6,10
print('La pendiente de es de:',(y2-y1)/(x2-x1))


10. Compare the slopes in tasks 8 and 9.

#ejercicio 11
x = -3
y = x**2 + 6*x + 9
print ("El valor de y en y = x^2 + 6x + 9 cuando x=-3 es: ", y)

#ejercicio 12
pa1 = 'python'
pa2 = 'dragon'

longitud1 = len(pa1)
longitud2 = len(pa2)

falsy_comparation = longitud1>longitud2
print('El numero de letras de python:',longitud1)
print('El numero de letras de dragon:',longitud2)
print('la comparacion es false porque tienen el mismo numero de letras',falsy_comparation)   

#ejercicio 12
print(len("python")<len("dragon"))

#ejercicio 13
print("on" in "python" and "on" in "dragon")

#ejercicio 14
sentence = "I hope this course is not full of jargon."
word = "jargon"

if word in sentence:
    print(f"'{word}' is in the sentence.")
else:
    print(f"'{word}' is not in the sentence.")

word1 = "dragon"
word2 = "python"

if "on" not in word1 and "on" not in word2:
    print("There is no 'on' in both dragon and python")
else:
    print("There is 'on' in at least one of the words")


#ejercicio 15
word1 = "dragon"
word2 = "python"

if "on" not in word1 and "on" not in word2:
    print("There is no 'on' in both dragon and python")
else:
    print("There is 'on' in at least one of the words")

#ejercicio 16
longitud1_float= float(longitud1)
longitud1_str = str(longitud1_float)

print(type(longitud1_float))
print(type(longitud1_str))

#ejercicio 17
def is_even(number):
  """Checks if a number is even.

  Args:
    number: The number to check.

  Returns:
    True if the number is even, False otherwise.
  """
  if number % 2 == 0:
    return True
  else:
    return False

#ejercicio 18
residuo = 7//3
valor_entero = int(2.7)
comparacion= residuo== valor_entero
print('¿La comapracion es verdadera?',comparacion)

#ejercicio 19
x = (type("10"))
y = (type(10))
res = x == y
print("10 string y 10 int son iguales? ", res)

#ejercicio 20
valor1 = int(9.8)
valor2 = 10
comparacion3= valor1 == valor2
print('¿Son iguales?',comparacion3)

#ejercicio 21
hours = int(input('ingrese las horas que trabajo:'))
tarifa = float(input('Ingresa la tarifa:'))
pago = hours*tarifa
print('El pago de la semana es de:',pago)

#ejercicio 22
years=int(input('Ingresa el numero de años que ha vivido:'))
print('La cantidad de segundos es de:',31536000*years)

#ejercicio 23
def display_table():
  for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
