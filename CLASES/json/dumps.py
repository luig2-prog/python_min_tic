# Python -> JSON
#json.dumps()

import json

pacientes_covid = {
  "edad": 45,
  True: "TieneComorbilidades",
  "ciudad": "Pereira",
  "estado_civil": "divorciado",
  3456: "id_paciente",
  "hijos": 8,
  "parientes":["Carlos", "Jimena"],
  "amigos":("Carlos", "Jimena"),
  "viajes":{
    "destino1": "Madrid",
    "destino2": "New York",
    "destino3": "Tokio"
  }
}

with open("pacientes.txt", "w") as file:
  file.write(str(pacientes_covid))


pacientes_as_json = json.dumps(pacientes_covid)

with open("pacientes.json", "w") as file:
  file.write(pacientes_as_json)