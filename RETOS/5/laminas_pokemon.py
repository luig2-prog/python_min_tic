
def hacer_lista(cadena_input):
  cadena = ''
  for i in range(len(cadena_input)):
    # print(entrada_clases[i])
    if cadena_input[i] == '[' or cadena_input[i] == ']' or cadena_input[i] == ',' or cadena_input[i] == ' ':
      continue
    cadena += cadena_input[i] + " "
    
  cadena = cadena.strip()

  return cadena.split(' ')


def lista_clases(clases):
  resultado = []
  # Algoritmo
  #laminas_disponibles = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran(Hembra)','Nidorina','Nidoqueen','Nidoran(Macho)','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetchd','Doduo','Dodrio','Seel','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','MrMime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew']
  for clase in range(len(clases)):
    if not(clases[clase] in resultado):
      resultado.append(clases[clase])
  return resultado

clases = hacer_lista(input())

print(lista_clases(clases))


# #######################################

def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
  resultado = []
  # Algoritmo
  for item in indices:
    for i in range(len(clases)):
      if clases[i] == clase_a_verificar or item==i:
        resultado.append(item)

  return resultado


indices = hacer_lista(input())
clases = hacer_lista(input())
clase_a_verificar = int(input())


print(laminas_faltantes_por_clase(indices, clases, clase_a_verificar))



##############################################

def laminas_faltantes(laminas_persona_1, laminas_persona_2):
  resultado = []
  # Algoritmo
  for lamina_p_1 in laminas_persona_1:
    if not(lamina_p_1 in laminas_persona_2):
      resultado.append(lamina_p_1)
  return resultado


laminas_persona_1 = hacer_lista(input())
laminas_persona_2 = hacer_lista(input())
print(laminas_faltantes(laminas_persona_1, laminas_persona_2))

##########################

def cantidad_laminas_cambiables(laminas_persona_1, laminas_persona_2):
  resultado = 0
  if(len(laminas_persona_1)>len(laminas_persona_2)):
    for l in laminas_persona_2:
      if(laminas_persona_1.count(l)==0):
        resultado+=1
  else:
     for l in laminas_persona_1:
      if(laminas_persona_2.count(l)==0):
        resultado+=1
  return resultado


laminas_persona_1 = hacer_lista(input())
laminas_persona_2 = hacer_lista(input())
print(laminas_persona_1, laminas_persona_2)
