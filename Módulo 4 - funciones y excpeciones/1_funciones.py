
#########################-----------LAB 4.3.1.6----------#######################
def is_year_leap(year):
    
    if year <= 1580:
        print ("No esta dentro del período del calendario Gregoriano")
    else:
        if year % 4:
            bisiesto = False
        elif year % 100:
            bisiesto = True
        elif year % 400:
            bisiesto = False
        else:
            bisiesto = True        

    return bisiesto

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
          
#########################-----------LAB 4.3.1.7----------#######################

def is_year_leap(year):

    if year <= 1580:
        print ("No esta dentro del período del calendario Gregoriano")
        return None

    else:
        if year % 4:
            bisiesto = False
        elif year % 100:
            bisiesto = True
        elif year % 400:
            bisiesto = False
        else:
            bisiesto = True        

    return bisiesto

def days_in_month(year, month):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [month for month in range (1,13) if month not in month_31 if month is not 2]
    days_in_month = 0

    if month in month_31:
         days_in_month = 31

    elif month in month_30:
        days_in_month = 30

    elif month == 2:
        if is_year_leap (year):
            days_in_month = 29
        else:
            days_in_month = 28

    else:
         return None
    
    return days_in_month
         
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
          

#########################-----------LAB 4.3.1.8----------#######################

def is_year_leap(year):
    if year <= 1580:
        print ("No esta dentro del período del calendario Gregoriano")
        return None
    else:
        if year % 4:
            bisiesto = False
        elif year % 100:
            bisiesto = True
        elif year % 400:
            bisiesto = False
        else:
            bisiesto = True        
    return bisiesto

def days_in_month(year, month):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [month for month in range (1,13) if month not in month_31 if month is not 2]
    days_in_month = 0

    if month in month_31:
         days_in_month = 31
    elif month in month_30:
        days_in_month = 30
    elif month == 2:
        if is_year_leap (year):
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        return None
    return days_in_month

def day_of_year(year, month, day):
    day_of_the_year = 0
    
    if day > days_in_month (year, month):
        return None
    else:
        for month in range (1, month+1):
            day_of_the_year += days_in_month (year, month)
    return day_of_the_year

print(day_of_year(1581, 2, 28))

#########################-----------LAB 4.3.1.9----------#######################

def is_prime(num):
    prime = True
    divisor = 2
    while prime == True and divisor < num:
        if num%divisor == 0:
            prime = False
            divisor = 10
        else:
            prime = True
            divisor += 1
    return prime
        

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


#########################-----------ÁMBITO DE VARIABLES EN FUNCIONES----------#######################

#--------------------------------------------- Caso 1 ----------------------------------------------#
# Una variable definida en una función no es accesible desde fuera de la función

# def scope_test():
#     x = 123

# scope_test()
# print(x)

#--------------------------------------------- Caso 2 ----------------------------------------------#

# Una variable declarada fuera de la función es visible desde dentro de la función

# x = 123
# def scope_test2():
#     print(x)

# scope_test2()

#--------------------------------------------- Caso 3 ----------------------------------------------#
# redefinición de la variable x

# x = 123

# def scope_test2():

#     x = 321     # provoca la creación de otra variable llamada x
    
#     print("Dentro de la función el valor de x es", x)    


# print("Fuera de la función el valor de x es", x)  

# scope_test2()

# print("Fuera de la función el valor de x es", x)

#--------------------------------------------- Caso 4 ----------------------------------------------#
#  Uso de global

# x = 123

# def scope_test2():

#     global x    # extender el alcance de la variable x al cuerpo de la función
#     x = 321     # ya no se crea una segunda variable x
    
#     print(x)    

# scope_test2()

# print(x)

#########################-----------FUNCIONES RECURSIVAS----------#######################
import time
def funcion_recursiva(numero):
    time.sleep (0.5)
    if numero > 1:                              #Condición de parada ¡¡¡OBLIGATORIO!!!
        print("Ejecutando la funcion", numero)
        funcion_recursiva( numero - 1)
    else:
        print("Ejecutando la funcion", numero)
        print('Terminado!')
        
funcion_recursiva(10)


#------------------------- Serie FIBONACI con función estándar -------------------------#
def fn(n):
    number_pos = n - 1
    if(n > 0):
        list_fib = [1,1]
        for i in range(1,n):
            fib_numer = list_fib[-1] + list_fib[-2] 
            list_fib.append(fib_numer)
        print(list_fib)
        print(list_fib[number_pos])

fn(10)

#------------------------- Serie FIBONACI con función RECURSIVA -------------------------#
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    print("\tfib(",n-1,") + ","fib(",n-2,")", sep="")

    return fib(n - 1) + fib(n - 2)


print("Resultado:",fib(5))

for n in range(1, 10):  # probando
    print(n, "->", fib(n))

#------------------------- Otro ejemplo de función RECURSIVA -------------------------#

def fun(a):
    if a > 30:
        return 3
    else:
        print ("Llamando a la función con valor", a)
        print("Calculando la suma de", a, "+fun(", a+3, ")")
        return a + fun(a + 3)


print(fun(25))