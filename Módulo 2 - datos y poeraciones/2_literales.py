# Los literales son valores constantes que representan datos de diferentes tipos.
print("2" * 5)
print(2 * 5)

print(type("2"))
print(type(2))

# Se puede usar barra baja para separar bloques de números y no influye en el valor numérico.
print(123456789 + 1)
print(1_23_45_6789 + 1)
print(-11111.69)
print(+11111.69)

# Cambio de tipos de números:
# Octal (empieza por 0o) a decimal. Formato hexadecimal empieza por 0x. Formato binario empieza por 0b.
print(0o123)
print(0b1011)

# Flotantes
c = 0.4
c = .4
c = 4.
print(type(4.))
print(type(4))

# Exponentes
c = 3E8
print(c)
c = 3e8
print(c)
print(0.0000000000000000000012)

# Cadena de caracteres
print("Me gusta \"Monty Python\"")
print('Me gusta "Monty Python"')
print("I'm Monty Python.")

# Booleanos
print(True < False)
print(3<6)
print(1>True)
print(0.25 > False)