###########--------- MANEJO DE EXCEPCIONES --------################

try:
    value = input("Introduce un número natural")   
    value = int(value)
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('valor inválido')
    print('No se que hacer con', value)


###########--------- MANEJO DE EXCEPCIONES --------################
    
try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.') 
except:
    print("Ha ocurrido algún otro error")

###########--------- MANEJO DE EXCEPCIONES --------################

while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor incorrecto o se ha roto la regla de división entre cero.")
    except:
        print("Lo siento, algo salió mal...")