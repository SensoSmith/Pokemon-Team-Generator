import random

class pokemon:
    def __init__(self, name):
        self.name = name

Venusaur = pokemon("Venusaur")
Charizard = pokemon("Charizard")
Blastoise = pokemon("Blastoise")
Raichu = pokemon("Raichu")
Snorlax = pokemon("Snorlax")
Arbok = pokemon("Arbok")
Pinsir = pokemon("Pinsir")
Machamp = pokemon("Machamp")
Golem = pokemon("Golem")
Dugtrio = pokemon("Dugtrio")
Pidgeot = pokemon("Pidgeot")
Alakazam = pokemon("Alakazam")
Dewgong = pokemon("Dewgong")
Gengar = pokemon("Gengar")
Dragonite = pokemon("Dragonite")

pokemonList = [Venusaur, Charizard, Blastoise, Raichu, Snorlax, Arbok, Pinsir, Machamp, Golem, Dugtrio,
               Pidgeot, Alakazam, Dewgong, Gengar, Dragonite]

party = []

for i in range(6):
    party.append(random.choice(pokemonList))

for i in range(6):
    print(party[i].name)