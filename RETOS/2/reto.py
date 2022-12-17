
def cadena_final(team_pedro,team_jimena,winning_teams):
    points_pedro = 0
    points_jimena = 0
    join_list = ''
    for character in winning_teams:
        if team_pedro.find(character) != -1: points_pedro += 1         
        if team_jimena.find(character) != -1: points_jimena += 1
        if points_jimena > points_pedro: join_list += 'J'
        elif points_pedro > points_jimena: join_list += 'P'
        else:join_list += 'E'
    
    return join_list

#Caso 1
resultado_esperado = "PPEEEJJJ"
resultado_obtenido = cadena_final("GMJO","NEBT","GZEZKBTO")

prueba_1 = True if resultado_obtenido == resultado_esperado else False
print(f"Caso #1: {prueba_1}")

#Caso 2
resultado_esperado = "EEPPPPEPEEPPPEEEEJJEJJJEEJ"
resultado_obtenido = cadena_final("CSYQR","QJEBP","OMSZREBRPMRQAJAQMBNCBERYGP")

prueba2: bool = True if resultado_obtenido == resultado_esperado else False
print(f"Caso #2: {prueba2}")

#Caso 3
prueba3: bool = True if cadena_final("YCTAD","RCAYP","EGMPYBTBMGZPBQBDZESRDMGEM") == "EEEJJJEEEEEJJJJEEEEJEEEEE"else False
print(f"Caso #3: {prueba3}")

#Caso 4
prueba4: bool = True if cadena_final("MBO","JNS","QETESSTPGZPGBYOABCCSJDYQCKNO") == "EEEEJJJJJJJJJJEEPPPEJJJJJJJJ" else False
print(f"Caso #4: {prueba4}")

#Caso 5
prueba5: bool = True if cadena_final("DPBA","MZDT","OCOKPGCNMOAERANNYTYCPMSKKEE") == "EEEEPPPPEEPPPPPPPPPPPPPPPPP" else False
print(f"Caso #5: {prueba5}")