def charger_pokemons_csv(unfichiercsv):
    les_pokemons = {}
    with open(unfichiercsv,'r') as fichier:
        lecture = fichier.readlines()
        for l in lecture:
            leselements=l.strip().split(',')
            nomdupokemon=leselements[0]
            lesstatistiques=[int(el) for el in leselements[1:]]
            les_pokemons[nomdupokemon] = lesstatistiques
    return les_pokemons


pkmn = charger_pokemons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokemons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))

