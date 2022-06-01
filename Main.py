import random

class HM:
    def __init__(self, name):
        self.name = name

class pokemon:
    def __init__(self, name, number, HMs):
        self.name = name
        self.number = number
        self.HMs = HMs

cut = HM("Cut")
fly = HM("Fly")
surf = HM("Surf")
strength = HM("Strength")
flash = HM("Flash")

Venusaur = pokemon("Venusaur", 3, [cut])
Charizard = pokemon("Charizard", 6, [cut, strength])
Blastoise = pokemon("Blastoise", 9, [surf, strength])
Beedrill = pokemon("Beedrill", 15, [cut])
Pidgeot = pokemon("Pidgeot", 18, [fly])
Raticate = pokemon("Raticate", 20, [])
Fearow = pokemon("Fearow", 22, [fly])
Arbok = pokemon("Arbok", 24, [strength])
Raichu = pokemon("Raichu", 26, [flash])
Sandslash = pokemon("Sandslash", 28, [cut, strength])
Nidoqueen = pokemon("Nidoqueen", 31, [surf, strength])
Nidoking = pokemon("Nidoking", 34, [surf, strength])
Clefable = pokemon("Clefable", 36, [strength, flash])
Ninetales = pokemon("Ninetales", 38, [])
Wigglytuff = pokemon("Wigglytuff", 40, [strength, flash])
Golbat = pokemon("Golbat", 42, [])
Vileplume = pokemon("Vileplume", 45, [cut])
Dugtrio = pokemon("Dugtrio", 51, [])
Alakazam = pokemon("Alakazam", 65, [flash])
Machamp = pokemon("Machamp", 68, [strength])
Golem = pokemon("Golem", 76, [strength])
Slowbro = pokemon("Slowbro", 80, [surf, strength, flash])
Farfetchd = pokemon("Farfetch'd", 83, [cut, fly])
Dodrio = pokemon("Dodrio", 85, [fly])
Dewgong = pokemon("Dewgong", 87, [surf, strength])
Gengar = pokemon("Gengar", 94, [strength])
Jynx = pokemon("Jynx", 124, [])
Pinsir = pokemon("Pinsir", 127, [cut, strength])
Snorlax = pokemon("Snorlax", 143, [surf, strength])
Dragonite = pokemon("Dragonite", 149, [surf, strength])

totalPokemonList = [Venusaur, Charizard, Blastoise, Beedrill, Pidgeot, Raticate, Fearow, Arbok,
                    Raichu, Sandslash, Nidoqueen, Nidoking, Clefable, Ninetales, Wigglytuff, Golbat,
                    Vileplume, Dugtrio, Alakazam, Machamp, Golem, Slowbro, Farfetchd, Dodrio,
                    Dewgong, Gengar, Jynx, Pinsir, Snorlax, Dragonite]

availablePokemonList = list(totalPokemonList)

starters = [Venusaur, Charizard, Blastoise]

party = []

hmList = [cut, fly, surf, strength, flash]

# randomly select starter
chosenStarter = random.choice(starters)
party.append(chosenStarter)
# test code start
#print("TEST: Successfully added member: " + chosenStarter.name)
# test code end

# remove starters from available Pokemon list
for i in range(3):
    availablePokemonList.remove(starters[i])

# mark appropriate HMs as covered by the starter
hmList.remove(random.choice(chosenStarter.HMs))

# randomly select five other party members
for i in range(5):
    counter = 0
    success = 0
    while success == 0:
        potentialMember = random.choice(availablePokemonList)
        if len(hmList) > 0:
            if len(potentialMember.HMs) > 0:
                for i in potentialMember.HMs:
                    if hmList.count(i) > 0:
                        counter += 1
                if counter > 0:
                    hmCoverage = list(potentialMember.HMs)
                    for i in potentialMember.HMs:
                        if hmList.count(i) == 0:
                            hmCoverage.remove(i)
                    if len(hmCoverage) > 0:
                        hmList.remove(random.choice(hmCoverage))
                        success = 1
        else:
            success = 1
    party.append(potentialMember)
    # test code start
    #print("TEST: Successfully added member: " + potentialMember.name)
    # test code end
    availablePokemonList.remove(potentialMember)

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

# display the selected party Pokemon, along with the HMs each is able to cover
for i in range(6):
    print(party[i].name + " - ", end="")
    if len(party[i].HMs) == 0:
        print("None")
    elif len(party[i].HMs) == 1:
        print(party[i].HMs[0].name)
    elif len(party[i].HMs) == 2:
        print(party[i].HMs[0].name + ", " + party[i].HMs[1].name)
    elif len(party[i].HMs) == 3:
        print(party[i].HMs[0].name + ", " + party[i].HMs[1].name + ", " + party[i].HMs[2].name)