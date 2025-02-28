# ######################----------########################
# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

# numbers[0] = 111
# print(numbers [0])
# print("Nuevo contenido de la lista:", numbers)

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# ######################-----LONGITUD DE LISTA-----########################
# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# ######################-----ELIMINAR ELEMENTO DE LISTA-----########################
# del numbers[1]  # Eliminando el segundo elemento de la lista.
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# ######################-----EMPEZANDO POR EL FINAL DE LISTA-----########################
# numbers = [111, 7, 2, 1]
# print(numbers[-1])
# print(numbers[-2])

# ######################----------Ejercicio 1----------########################
# lista_sombreros = [1, 2, 3, 4, 5]

# # Paso 1
# lista_sombreros[2] = int(input("Ingresa un número entero: "))

# # Paso 2
# del lista_sombreros[-1]

# # Paso 3
# print(len(lista_sombreros))

# # imprimir lista completa para comprobar

# print(lista_sombreros)

# # Concatenar todos los valores como String

# resultado = ""

# for valor in lista_sombreros:
#     resultado += str(valor)
# print(resultado)

# ######################----------MÉTODOS DEL OBJETO LISTA----------########################
# numbers = [111, 7, 2, 1]
# print(numbers)
# print("Longitud actual de la lista: ",len(numbers))
# # # ###
# numbers.append(4)
# print(numbers)
# print("Longitud actual de la lista: ",len(numbers))
# # # # ###
# numbers.insert(0, 222)
# print(numbers)
# print("Longitud actual de la lista: ",len(numbers))
# # # eliminación por valor!!!
# numbers.remove(111)
# print(numbers)
# print("Longitud actual de la lista: ",len(numbers))

# ######################----------MENSAJE INVERTIDO----------########################
# prueba = input("Escribe lo que quieras: ")

# lista = list(prueba)

# print(lista)
# lista.reverse()
# print(lista)
# mensaje = input("Introduce un mensaje: ")

# lista = []

# mensaje_invertido = ''


# for letra in mensaje:
#     lista.insert(0,letra)
#     mensaje_invertido = letra + mensaje_invertido 

# print(lista)
# print(mensaje_invertido)

# ######################----------RECORRER UNA LISTA----------########################
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for indice in range(len(my_list)):
#     total += my_list[indice]

# print(total)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# for elemento in my_list:
#     total += elemento

# print(total)

# ######################----------SINTAXIS DE INTERCAMBIO----------########################
# variable_1 = 1
# variable_2 = 2

# variable_1, variable_2 = variable_2, variable_1
# #----------#
# my_list = [10, 1, 8, 3, 5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)
# #-----------#
# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)

# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)

######################----------Ejercicio 2----------########################
# Beatles = []

# print("Paso 1:", Beatles)


# Beatles.append("John Lenon")
# Beatles.append("Paul McCartney")
# Beatles.append("George Harrison")

# print("Paso 2:", Beatles)

# for _ in range (2):             #Ahorro de crear una variable con el uso de "_"
#     Beatles.append (input("Inserta un nuevo componente de la banda: "))
# print("Paso 3:", Beatles)

# for i in range (2):             #Beatles.remove("Stu Sutcliffe")
#     del Beatles[-1]             #Beatles.remove("Pete Best")

# print("Paso 4:", Beatles)

# Beatles.insert (0, "Ringo Star")
# print("Paso 5:", Beatles)

# # probando la longitud de la lista
# print("Los Fav", len(Beatles))

######################----------Ordenación método BURBUJA----------########################

# my_list = [10, 8, 6, 2, 4]                                          # lista a ordenar

# for i in range(len(my_list) - 1):                                   # necesitamos (5 - 1) comparaciones

#     if my_list[i] > my_list[i + 1]:  
#         print("Cambiando orden")                                    # compara elementos adyacentes
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]     # Si llegamos aquí, tenemos que intercambiar elementos.

#     print("Iteración ", i , ":", my_list)

######################----------Ordenación método BURBUJA COMPLETO----------########################
# my_list = [8, 10, 6, 2, 4]  # lista a ordenar

# swapped = True  # Lo necesitamos verdadero (True) para entrar en el bucle while.

# while swapped == True:

#     swapped = False  # no hay intercambios hasta ahora
    
#     for i in range(len(my_list) - 1):
        
#         if my_list[i] > my_list[i + 1]:
            
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            
#     print("Iteración de bucle while:",my_list)

######################----------Ordenación método SORT----------########################

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)

######################----------Ejercicio 3----------########################
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []
# for number in my_list:              # Recorremos todos los números de la lista original.
#     if number not in new_list:      # Si el número no aparece dentro de la nueva lista ...
#         new_list.append(number)     # ... añadirlo aquí.
# my_list = new_list                  # Asignamos la nueva lista a la variable original.
# del new_list
# print("La lista con elementos únicos:")
# print(my_list)

            ###########---Otra solución---##########
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []
# for number in my_list:              # Recorremos todos los números de la lista original.
#     if number not in new_list:      # Si el número no aparece dentro de la nueva lista ...
#         new_list.append(number)     # ... añadirlo aquí.
# my_list = new_list                  # Asignamos la nueva lista a la variable original.
# del new_list
# print("La lista con elementos únicos:")
# print(my_list)

            ###########---Otra solución---##########
# miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# for i in range(len(miLista)):
#     if miLista[i] in miLista[i:]:
#         del miLista[i]

# print(miLista)

######################----------COMPRENSIÓN DE LISTAS----------########################

# row = []

# for i in range(8):
#     row.append("peón blanco")
# print(row)

# row = ["peón blanco" for i in range(8)]
# print(row)

# # Ejemplo #1:

# squares = [numero ** 2 for numero in range(10)]
# print(squares)

# # # Ejemplo #2:

# twos = [2 ** i for i in range(8)]
# print(twos)

# # # Ejemplo #3:

# impares = [elemento for elemento in squares if elemento % 2 != 0 ]

# print(impares)

# # # Ejemplo #4:

# lista_letras = [letra for letra in 'Palabra']

# print(lista_letras)

########################--- Otro ejemplo ---##############################3
# filas = int(input("¿Cuántas filas quieres crear? "))
# columnas = int(input("¿Cuántas columnas quieres crear? "))

# matriz = []

# for fila in range(filas):
#     matriz.append([])               # crea una lista vacía por cada fila

#     for columna in range(columnas):
#         matriz[fila].append(str(fila) + "-" + str(columna))

# print(matriz)

# #  Impresión de la matriz con formato

# for fila in range(len(matriz)):
#     print() 
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna], end =" ")


##############---Ejemplo temperatura-dia-mes###############
        
# import random

# temps = [[0.0 for h in range(24)] for d in range(31)]

# total = 0.0

# # # Rellenar con valores aleatorios

# for fila in range(len(temps)):
#     for columna in range(len(temps[fila])):
#         temps[fila][columna] = random.choice(range(10, 450))/10

# for day in temps:
#     total += day[11] # Las 12:00 horas

# average = total / 31

# print("Temperatura promedio al mediodía:", round(average,1), "grados centígrados")
        
# # Imprimir lista con formato

# for fila in range(len(temps)):
#     print("\nDía", fila + 1)
#     for columna in range(len(temps[fila])):
#         print(temps[fila][columna], end = "  ")

##########------------ Ejemplo hotels------------###########
rooms = [[[False for habitacion in range(20)] for planta in range(15)] for edificio in range(3)]

rooms[1][9][13] = True

rooms[0][4][1] = False

# # ##  Habitaciones ocupadas en la planta 15 del tercer hotel

rooms[2][14][0] = True    # Edificio 3, Planta 15, Habitación 1
rooms[2][14][1] = True    # Edificio 3, Planta 15, Habitación 2

vacancy = 0

# #  Número de habitaciones libres en la planta 15 del tercer hotel

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("Hay", vacancy, "habitaciones libres en la planta 15 del tercer edificio")

# función sorted() y método sort()

def longitud(e):
  return len(e)

#####################################-----ORDENACIÓN CON SORTED-----######################################

lista1 = ['zapatería','barca','fenómeno','cocina','dedo','armario']

lista2 = sorted(lista1)         # crea una nueva lista

# print(lista1)
# print(lista2)

lista2 = sorted(lista1, key = longitud, reverse = True)

print('\nLlamando a la función sorted() con parámetros key=longitud y reverse = True:\n')

for elemento in lista2:
    print(elemento)
    
    
#######################################-----ORDENACIÓN CON SORT-----#######################################

lista1.sort(key = longitud, reverse = True)     # no produce una nueva lista, sino que ordena la lista actual

print('\nLlamando al método sort() con parámetro key=longitud y reverse = True:\n')

for elemento in lista1:
    print(elemento)