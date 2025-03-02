#Dia 2: Programacion en python
import math as m


nombre = "Damaris"
apellido = "Perez"
completo = "Damaris Sarahi Perez Cuevas"
pais = "Mexico"
ciudad = "Encarnacion de diaz"
edad = ("18")
año = ("2024")
is_married = True
is_true = True
nomb, animal, pais  =  "Damaris", "Perro", "Mexico"

print (type("nombre"))
print (type("apellido"))
print (type("completo"))
print (type("pais"))
print (type("ciudad"))
print (type("edad"))
print (type("año"))
print (type("is_married"))
print (type("is_true"))

print (len("nombre"))
print (len("apellido"))

num_uno = 5
num_dos = 4
total = num_uno + num_dos
diff = num_uno - num_dos
mult = num_uno * num_dos
div = num_uno / num_dos 
remaider = num_uno % num_dos 
exp = num_uno ** num_dos
floor_division = num_uno // num_dos

radio = 30
math = 3.1416
area_del_circulo = math * radio**2
print ("el area del circulo es:", area_del_circulo)
circunferencia_del_circulo = 2 * radio
print ("la circunferencia del circulo es: ",circunferencia_del_circulo)


radio_usuario = float(input("introduce el radio del circulo en metros: "))
print("El area del circulo" , radio**2 * math)


nombre = input("introduce tu nombre: ")
apellido = input("introduce tu apellido: ")
pais = input("introduce tu pais: ")
edad = input("introduce tu edad: ")

print("tu nombre es:", nombre)
print("tu apellido es:", apellido)
print("tu pais es:", pais)
print("tu edad es:", edad)

import keyword
print (keyword.kwlist)