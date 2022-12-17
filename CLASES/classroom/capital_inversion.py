# Crear un programa en lenguaje de programación Python que pregunte al 
# usuario una cantidad de dinero a invertir, un porcentaje de interés 
# anual y un número de años, y muestre por pantalla el valor del capital 
# que se tendria cada año que dure la inversión.

# El programa debe validar que la cantidad de dinero sea un valor real positivo, 
# que el porcentaje anual sea ingresado en formato percentil y no en formato decimal 
# (Ej: Cincuenta porciento debe ser ingresado como 50, no como 0.5), y que 
# el número de años sea entero positivo, de lo contrario, el programa debe solicitar 
# nuevamente, y de manera indefinida, los valores que hayan sido ingresados incorrectamente.
while True:
    cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
    if cantidad_invertir > 0:
        break
    print("La cantidad a invertir debe ser mayor a cero (0)")

while True:
    porcentaje_interes_anual = input("Ingrese el porcentaje anual: ")
    
    if not (porcentaje_interes_anual.find('.') != -1 or porcentaje_interes_anual.find(',') != -1):
        porcentaje_interes_anual = int(porcentaje_interes_anual)
        if porcentaje_interes_anual > 0:
            break
        else:
            print("El porcentaje de interes anual debe ser mayor a cero (0)")
    
    print("""
    El porcentaje de interes anual debe ser ingresado en formato percentil
    no en formato decimal, y debe contener solo numeros
    (Ej: Si quiere ingresar cincuenta porciento (50%) 
    debe ser ingresado como 50, no como 0.5 o 50%)
    """)  

while True:
    numero_años = int(input("Ingrese el numero de años: "))
    if numero_años > 0:
        break
    print("El numero de años debe ser mayor a cero (0)")

print(f"Cantidad a invertir: {cantidad_invertir}")
print(f"Porcentaje de interes anual: {porcentaje_interes_anual}")
print(f"Numero de años a invertir: {numero_años}")

for contador in range(numero_años):
    cantidad_invertir = (cantidad_invertir + cantidad_invertir * (porcentaje_interes_anual /100))

print(f"El capital es de : {cantidad_invertir}$")