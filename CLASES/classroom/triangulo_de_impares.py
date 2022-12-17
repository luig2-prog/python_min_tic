# Crear un programa en lenguaje de programación Python que 
# reciba un número entero positivo, y muestre un triángulo de 
# números impares cuya cantidad de filas sea igual al número 
# ingresado. 
# El triángulo debe mostrar los números impares en cada fila, 
# ordenados de mayor a menor desde la izquierda.

# Ej. Si el usuario ingresa el número 5, el programa debe mostrar lo siguiente:

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

while True:
    numero = input("ingrese un numero entero positivo: ")
    if numero.isdigit():
        break
    print("Debe ingresar un numero entero positivo sin comas (,) puntos (.) o cualquier caractér")

