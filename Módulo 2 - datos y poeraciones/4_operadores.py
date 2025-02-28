# Operadores

print("3 + 2 = ", 3+2)  # Suma
print (-4 - 4)
print("3 - 2 =", 3-2)   # Resta
print(type(3.2+5))  # Si uno de los sumendos es float, el resultado es float
print("Exponenete: 2^3 =", 2**3)    # Exponente

# Multiplicación
print("3 x 2 =", 3*2)
print(type(3*2))

# División (el resultado siempre es un float)
print("6/3 =", 6/3)
print(type(6/3))

print ("5/2 parte entera:", 5//2) # Parte entera
print(type(5//2))

print("Resto de 5/2 =", 5%2) # Resto
print(type(5%2))

# Cómo NO dividir --> Zero division ERROR
# print(2/0)
# print(2//0)
# print(2%0)

# Operadores abreviados
var = 2
var = var / 2 * 4   # Se evalúa la operación de izquierda a derecha
print(var)

var = 2
var /= 2 * 4    # CUIDADO!!! Evalúa antes 2*4: los operadores abreviados tienen menos prioridad que TODOS los normales.
print(var)

# Ejercicio 1
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.61*kilometers
kilometers_to_miles = kilometers/1.61

print()
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
print()

# Ejercicio 2

eur = 5.6
dollar = 15.8

eur_to_dollar = 1.08 * eur
dollar_to_eur = 1/1.08 * dollar

print(eur, "€ son ", "$", str(round(eur_to_dollar, 2)).replace(".", ","), sep ="")
print("$", dollar, " son ", str(round(dollar_to_eur, 2)).replace(".", ","), "€", sep = "")
print()

