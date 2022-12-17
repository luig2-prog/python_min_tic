#JSON -> Python
json.loads()

import json

with open("pacientes.json", "r") as file:
  content_as_json = file.read()
  print(type(content_as_json))

data_pacients = json.loads(content_as_json)

print(type(data_pacients))

print(data_pacients["edad"])