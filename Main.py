import random

class pokemon:
    def __init__(self, name, number):
        self.name = name
        self.number = number

Venusaur = pokemon("Venusaur", 3)
Charizard = pokemon("Charizard", 6)
Blastoise = pokemon("Blastoise", 9)
Beedrill = pokemon("Beedrill", 15)
Pidgeot = pokemon("Pidgeot", 18)
Fearow = pokemon("Fearow", 22)
Arbok = pokemon("Arbok", 24)
Raichu = pokemon("Raichu", 26)
Sandslash = pokemon("Sandslash", 28)
Nidoqueen = pokemon("Nidoqueen", 31)
Clefable = pokemon("Clefable", 36)
Dugtrio = pokemon("Dugtrio", 51)
Alakazam = pokemon("Alakazam", 65)
Machamp = pokemon("Machamp", 68)
Golem = pokemon("Golem", 76)
Dewgong = pokemon("Dewgong", 87)
Gengar = pokemon("Gengar", 94)
Pinsir = pokemon("Pinsir", 127)
Snorlax = pokemon("Snorlax", 143)
Dragonite = pokemon("Dragonite", 149)

pokemonList = [Venusaur, Charizard, Blastoise, Beedrill, Pidgeot, Fearow, Arbok, Raichu,
               Sandslash, Nidoqueen, Clefable, Dugtrio, Alakazam, Machamp, Golem, Dewgong,
               Gengar, Pinsir, Snorlax, Dragonite]

party = []

for i in range(6):
    party.append(random.choice(pokemonList))

# party sorting algorithm
slot1 = 0
slot2 = 0
slot3 = 0
slot4 = 0
slot5 = 0
slot6 = 0
counter = 0
for i in range(6):
    for j in range(6):
        if party[i].number < party[j].number:
            counter += 1
    if counter == 5:
        slot1 = i
    elif counter == 4:
        slot2 = i
    elif counter == 3:
        slot3 = i
    elif counter == 2:
        slot4 = i
    elif counter == 1:
        slot5 = i
    else:
        slot6 = i
    counter = 0
sortedParty = []
sortedParty.append(party[slot1])
sortedParty.append(party[slot2])
sortedParty.append(party[slot3])
sortedParty.append(party[slot4])
sortedParty.append(party[slot5])
sortedParty.append(party[slot6])
party = sortedParty

for i in range(6):
    print(party[i].name)