
import ast

def name_pokemons(obj_json, pokemons_to_buy):
    list_of_keys =obj_json.keys()
    spending = 0
    pokemons = []
    for pokemon in pokemons_to_buy:
        if pokemon in list_of_keys:
            spending += obj_json[pokemon]
            pokemons.append(pokemon)

    return spending,pokemons

entry_one = ast.literal_eval(input())
entry_two = input()

entry_two_list = entry_two.split(" ")

output = name_pokemons(entry_one, entry_two_list)
variable = " ".join(output[1])
print(f"{output[0]}\n{variable}")