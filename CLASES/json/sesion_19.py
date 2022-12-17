
def name_pokemons(obj_json, pokemons_to_buy):
    listOfKeys =obj_json.keys()
    spending = 0
    pokemons = []
    for pokemon in pokemons_to_buy:
        if pokemon in listOfKeys:
            spending += obj_json[pokemon]
            pokemons.append(pokemon)

    return spending,pokemons

entry_one = {"Electrode": 56, "Marowak": 19, "Oddish": 50, "Raichu": 37, "Golduck": 38, "Ekans": 14, "Chansey": 87, "Articuno": 37, "Dratini": 76, "Hypno": 36, "Jynx": 41, "Krabby": 30, "Koffing": 43, "Magmar": 28, "Raticate": 40, "Lickitung": 63, "Victreebel": 93, "Metapod": 92, "Parasect": 53, "Paras": 55, "Cubone": 70, "Snorlax": 28, "Dewgong": 96, "Pikachu": 21, "Machoke": 55, "Ponyta": 36, "Ivysaur": 94, "Grimer": 60, "Kadabra": 82, "Golbat": 87, "Nidorino": 99, "Diglett": 25, "Arbok": 41, "Scyther": 60, "Clefable": 38, "Weedle": 34, "Starmie": 34, "Geodude": 13, "Magnemite": 26, "Charizard": 61, "Machop": 23, "Hitmonchan": 17, "Blastoise": 24, "Shellder": 51, "Magneton": 83, "Porygon": 61, "Nidorina": 51, "Dragonite": 24, "Slowbro": 16, "Vaporeon": 97, "Seaking": 64, "Horsea": 36, "Poliwag": 43, "Primeape": 13, "Hitmonlee": 40, "Sandshrew": 97, "Goldeen": 92, "Dragonair": 31, "Growlithe": 69}
entry_two = "Golem Sandslash Slowbro Cubone Bulbasaur Machoke Aerodactyl Seaking Vileplume Charmander Gengar Victreebel Hitmonlee Kakuna Tauros Fearow Clefable Graveler Rhyhorn Clefairy Magneton Dragonite Blastoise Cloyster Sandshrew Ponyta Abra Pinsir Voltorb Squirtle Chansey Shellder Golduck Kingler Dugtrio Omastar Weedle Raichu Tangela Electrode Zubat Grimer Flareon Exeggutor Butterfree Koffing Onix Rapidash Venomoth Jolteon Articuno Vaporeon Pidgey"

entry_two_list = entry_two.split(" ")

output = name_pokemons(entry_one, entry_two_list)
print(output[0])
print(" ".join(output[1]))
variable = " ".join(output[1])
result_test = f"{output[0]}\n{variable}"
expected_test = "1180\nSlowbro Cubone Machoke Seaking Victreebel Hitmonlee Clefable Magneton Dragonite Blastoise Sandshrew Ponyta Chansey Shellder Golduck Weedle Raichu Electrode Grimer Koffing Articuno Vaporeon"
print(result_test == expected_test)