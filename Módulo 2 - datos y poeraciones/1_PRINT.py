print("Hola mundo")
print('Hola mundo')
print('¡', "Hola",'Mundo',"!")

#help(print)

resultado = print("hola")
print(resultado)

# No se debe escribir más de una función en una línea, pero se puede desde la versión python 3.6
print('hola'); print('mundo'), print("!")

# Misma forma de escribir lo mismo, es más eficiente cuando se llama únicamente 2 veces a la función.
print("1. La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

print("2. La Witsi Witsi Araña subió a su telaraña.")
print("\nVino la lluvia y se la llevó.")

print("3. La Witsi Witsi Araña subió a su telaraña.\n")
print("Vino la lluvia y se la llevó.")

print("4. La Witsi Witsi Araña subió a su telaraña."
"Vino la lluvia y se la llevó.")

print("5. La Witsi Witsi Araña subió a su telaraña."
"\n\nVino la lluvia y se la llevó.")

print("6. La Witsi Witsi Araña subió a su" \
      "telaraña.")

print("7. La Witsi Witsi Araña subió a su"
      "telaraña.")

# Cambiando los parámetros de palabra clave de la función print
print("1. Mi nombre es", "Python", end = "****\n****", sep = "____")
print("Monty Python")

print("2. Mi nombre es", "Python", end = "", sep = "____")
print("Monty Python")

# Ejercicio
print("    *", "   * *", "  *   *", " *     *", "***   ***",
"  *   *", "  *   *", "  *****", sep = "\n")

print("    *", "   * *", "  *   *", " *     *", "***   ***",
"  *   *", "  *   *", "  *****", sep = "\n\n")

print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)