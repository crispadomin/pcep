##########-----Forma 1-----##########
print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")

##########-----Forma 2-----##########
# print("Dime algo...")
anything = input("Dime algo...\n")
print("Mmm...", anything, "...¿en serio?")

##########-----Forma 3-----########## REFACTORIZACIÓN
# print("Dime algo...")
# anything = input("Dime algo...\n")
print("Mmm...", input("Dime algo...\n"), "...¿en serio?")



# input() siempre devolverá una cadena de caracteres
# para operar con valores introducidos hay que convertirlos a numéricos (CASTING)
anything = input("Inserta un número: ")
something = int(anything)** 2.0                 # ó float(anything)
print(anything, "al cuadrado es", something)



# Ejercicio 1
leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", round(hypo, 2))

# Ejercicio 2
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + fnam + " " + lnam + ".")

# Ejercicio 3
num_1 = float(input("Introduce un valor decimal: "))
num_2 = float(input("Introduce otro valor decimal: "))

print("La suma de los valores introducidos es:", num_1 + num_2)
print("La multiplicación de los valores introducidos es:", num_1 * num_2)
print("La división de los valores introducidos es:", num_1 / num_2)

print("\n¡Eso es todo, amigos!")

# Ejercicio 4
x = float(input("Ingresa el valor para x: "))
y = 1 / (x + (1 / (x + 1 / (x + (1/x)))))
print("y =", y)

# Ejercicio 5
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_horas = hour + (mins + dura) / 60
total_dias = total_horas // 24

hora_final = int(total_horas - 24 * total_dias)
min_final = int((mins + dura) % 60)

print(hora_final, ":", min_final, sep ="")