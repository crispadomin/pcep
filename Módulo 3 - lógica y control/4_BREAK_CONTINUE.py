###########################---------------------##################################
# break - ejemplo
# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

# # continue - ejemplo
# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

###########################---Ejercicio 1---##################################
# secret_word = "chupacabra"
# while True:
#   word = input ("Introduce una palabra: ")
#   if word == secret_word:
#       break
# print("Has dejado el bucle con éxito")

###########################---Ejercicio 2---##################################
# user_word = input("Inserta una palabra: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter in "AEIOU":         #se puede escribir if letter in ("A", "E", "I", "O", "U")
#         continue
#     print (letter)

###########################---Ejercicio 3---##################################
# word_without_vowels = ""

# user_word = input("Inserta una palabra: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter in "AEIOU":
#         continue
#     word_without_vowels += letter 

# print (word_without_vowels)

###########################---Ejercicio 4---##################################
# blocks = int(input("Ingresa el número de bloques: "))
# height = 0
# total_blocks = 0

# while total_blocks <= blocks:
#     height += 1
#     total_blocks += height
#     if total_blocks - blocks == 0:
#         break

# print("La altura de la pirámide:", height)

###########################---Ejercicio 5---##################################
# c0 = int(input("Introduce un número: "))
# pasos = 0

# while c0 > 1:
#     if c0 % 2 == 0:         # si es par se divide entre 2
#         c0 = c0 // 2
#     else:                   
#         c0 = 3 * c0 + 1     # en caso de impar se multiplica por 3 y se suma 1    
#     pasos+=1
#     print(c0) 
# print("pasos = ",pasos)


# Ejercicio 5.1
# for i in range(1, 11):
#     if i % 2:
#         print (i)

# Ejercicio 5.2
# x = 1
# while x < 11:
#     if x % 2:
#         print (x)
#     x += 1

# Ejercicio 5.3
# word = ""
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     else:
#         word += ch
# print(word)

# Ejercicio 5.4
# word = ""
# for digit in "0165031806510":
#     if digit == "0":
#         word += "x"
#     else:
#         word += digit
# print(word)