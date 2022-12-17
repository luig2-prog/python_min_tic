import json
import requests

print("---------------------------------------------------")
print("Bienvenido al explorador de municipios de colombia!")
print("Porfavor seleccione uno de los departamentos, ingresando su código identificador")
print("- (1) Antioquia")
print("- (2) Amazonas")
print("- (3) Boyacá")
print("- (4) Chocó")
print("- (5) Nariño")

while True:
  codigo_str = input("Escriba el código: ")

  if codigo_str.isdigit() == False:
    print("Error: El texto ingresado NO es un número!")

  elif len(codigo_str) != 1:
    print("Error: El numero ingresado tiene MAS de UN digito!")

  else:
    codigo_int = int(codigo_str)

    if codigo_int < 1 or codigo_int > 5:
      print("Error: El codigo ingresado NO existe!")
    else:
      print("Procesando....\n")
      break


# Nos conectamos con la plataforma de Datos ABierto Colombia para recibir la informacion de los municipios de colombia
resultado = requests.get("https://www.datos.gov.co/resource/xdk5-pm3f.json")

# Convertimos la informacion recibida (que llegó en formato JSON) a un diccionario en Python
municipios = json.loads(resultado.text)

# Contamos la cantidad de municipios de antioquia
municipios_del_departamento = []

for municipio in municipios:

  nombre_departamento = municipio["departamento"].lower()
  nombre_municipio = municipio["municipio"]

  if codigo_int == 1 and nombre_departamento == "antioquia":
    municipios_del_departamento.append(nombre_municipio)

  elif codigo_int == 2 and nombre_departamento == "amazonas":
    municipios_del_departamento.append(nombre_municipio)

  elif codigo_int == 3 and nombre_departamento == "boyacá":
    municipios_del_departamento.append(nombre_municipio)

  elif codigo_int == 4 and nombre_departamento == "chocó":
    municipios_del_departamento.append(nombre_municipio)

  elif codigo_int == 5 and nombre_departamento == "nariño":
    municipios_del_departamento.append(nombre_municipio)



print(f"Cantidad de municipios es: {len(municipios_del_departamento)}")

for numero_municipio in range(len(municipios_del_departamento)):
  nombre_municipio = municipios_del_departamento[numero_municipio]
  print(f"{numero_municipio}: {nombre_municipio}")