def validad_valor_producto():
  valor_producto_string = input("Ingrese Valor del Producto: ") # "2.56"

  # Validacion: Convertimos la coma decimal en punto decimal
  valor_producto_sin_puntos = valor_producto_string.replace(".", "") # "256"
  valor_producto_sin_comas = valor_producto_sin_puntos.replace(",", "") # "256"

  print(f"valor_producto_sin_comas:{valor_producto_sin_comas}") # "256"

  return (valor_producto_sin_comas, valor_producto_string.replace(",", ".")) # ("Hola", "Hola")


productos = []

cantidad_productos = int(input("Cantidad Productos: "))

for conteo in range(0, cantidad_productos):
  valor_string = validad_valor_producto()

  # Validacion: Que tenga solo digitos numericos
  while valor_string[0].isdigit() == False: # "256"
    print("El valor ingresado NO es un número!\n\n")
    valor_string = validad_valor_producto()

  valor_producto = float(valor_string[1])
  productos.append(valor_producto)

total = 0
for item in productos:
  total += item

print(f"Total: {total}")