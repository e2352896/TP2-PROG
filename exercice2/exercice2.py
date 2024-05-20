def charger_pokemons_csv(fichier_csv):
     dict_pokemon = {}
     with open(fichier_csv,'r') as fichier:
         lecture = fichier.readlines()
         for ligne in lecture:
             el = ligne.strip().split(',')
             nom_pokemon = el[0]
             stat_pokemon = [int(el) for el in el[1:]]
             dict_pokemon[nom_pokemon] = stat_pokemon
     return dict_pokemon


pkmn = charger_pokemons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokemons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))

