##############################----- Definición de diccionario-----##############################

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary['gato'])
print(phone_numbers['Suzy'])


##############################----- Definir diccionario con SANGRÍA FRANCESA-----##############################

# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
              }

# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
                 'Suzy': 22657854310
                 }


##############################----- iterar en las claves del diccionario-----##############################

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
#--------------------------Asegurar que clave y valor están en el dicccionario------------------------#
for spanish, french in dictionary.items():
    print(spanish, "->", french)
#--------------------------Ordenar en el dicccionario------------------------#
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

#--------------------------Métodos para dicccionarios------------------------#

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.get("perro"))      # devolverá "chien"
dictionary.popitem()                # elemina la última clave
dictionary.clear()                  # Resetea el diccionario, mantiene el objeto
copy_dictionary = dictionary.copy() # Crea un objeto copiado
print(dictionary.update({"pato": "canard"}))   # Añadir pareja clave y valor al diccionario

#--------------------------Modificar valores en dicccionarios------------------------#

dictionary['gato'] = 'minou'
print("Valor modificado:", dictionary)

#--------------------------Añadir nuevas claves en dicccionarios------------------------#

dictionary['cisne'] = 'cygne'
print("Anadir clave;", dictionary)
#               Otra forma                #
dictionary.update({"pato": "canard"})
print(dictionary)

#--------------------------Eliminar elementos de dicccionarios------------------------#

del dictionary['gato'] #Elimina la clave
print("Clave eliminada:", dictionary)    #Eliminar una clave inexistente dará ERROR
dictionary.popitem()     #elemina la última clave
dictionary.clear()      # Resetea el diccionario, mantiene el objeto

