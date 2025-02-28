############################--------------------------------####################################
# numero = int(input("Inserta un número entero (positivo, negativo o cero:"))

# if numero > 0:
#     print("El número", numero, "es positivo")
# elif numero < 0:
#     print("El núemro", numero, "es negativo")
# else:
#     print("El número es 0")

############################--------------------------------####################################
#     #Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))

# # Elige el número más grande
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# # Imprime el resultado
# print("El número más grande es:", larger_number)

############################--------------------------------####################################
# #Se leen dos números
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))

# #SI L AS SENTENCIAS IF O WLSE ÚNICAMENTE TIENEN UNA LÍNEA DE CÓDIGO
# # Elige el número más grande
# if number1 > number2: larger_number = number1
# else: larger_number = number2

# # Imprime el resultado
# print("El número más grande es:", larger_number)

############################--------------------------------####################################
# numero = 10
# resultado = "numero positivo" if numero > 0 else "numero negativo o cero"
# print(resultado)

############################---Ejercicio 1---####################################
# planta = input ("Introduce una planta:")

# if planta == "ESPATIFILO":
#     print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
# elif planta == "espatifilo":
#     print("No, ¡quiero un gran ESPATIFILIO!")
# else:
#     print("¡ESPATIFILIO!, ¡No ", planta, "!", sep ="")

############################---Ejercicio 2---####################################
# income = float(input("Introduce el ingreso anual:"))

# if income < 85528:
#     tax = 0.18 * income - 556.2
# else:
#     tax = 14839.2 + 0.32 * (income - 85528)

# tax = max(round(tax, 0), 0)
# print("El impuesto es:", tax, "pesos")

# ############################---Ejercicio 3---####################################
# year = int(input("Introduce un año:"))

# if year > 1581:
#     if year % 4:            # year % 4 != 0 --- Todo lo que sea distinto de 0, para Python es 1
#         bisiesto = False
#     elif year % 100:        # year % 100 != 0
#         bisiesto = True
#     elif year % 400:        # year % 400 != 0
#         bisiesto = False
#     else:
#         bisiesto = True
    
#     if bisiesto:
#         print("Ano Bisiesto")
#     else:
#         print("Año común")
# else:
#     print("No dentro del período del calendario Gregoriano")