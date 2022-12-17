# Buenas practicas es que cuando el usuario ingrese un dato y se quiere comparar didcho dato, primero limpiarlo
# Ya que ej de entrada

nombre_eps = input("Ingrese el nombre de su EPS: ")
# Diferentes entradas que puede hacer el usuario
# sanitas
#  sanitas
# sanitas 
# Sanitas
#  Sanitas
# Sanitas 
# etc 
print(nombre_eps)
# Si el usuario ingresa
# nombre eps = "Sanitas"
# Y hago la comparación 
if nombre_eps == "sanitas":
    print(True)
else:
    print(False)
# El resultado es false, pero es la misma palabra; entonces, para evitar esto se convierte todo en mayusculas lower() y se quitan
# los espacios al principio y final
nombre_eps = nombre_eps.lower().strip()
print(nombre_eps)
if nombre_eps == "sanitas":
    print(True)
else:
    print(False)

nombre = "Luis"

for contador in range(len(nombre)):
    print(nombre[contador])