import random

class type:
    def __init__(self, name):
        self.name = name

Normal = type("Normal")
Fire = type("Fire")
Water = type("Water")
Electric = type("Electric")
Poison = type("Poison")
Bug = type("Bug")
Grass = type("Grass")
Fighting = type("Fighting")
Rock = type("Rock")
Ground = type("Ground")
Flying = type("Flying")
Psychic = type("Psychic")
Ice = type("Ice")
Ghost = type("Ice")
Dragon = type("Dragon")

class HM:
    def __init__(self, name):
        self.name = name

cut = HM("Cut")
fly = HM("Fly")
surf = HM("Surf")
strength = HM("Strength")
flash = HM("Flash")

class pokemon:
    def __init__(self, name, number, types, HMs):
        self.name = name
        self.number = number
        self.types = types
        self.HMs = HMs

Venusaur = pokemon("Venusaur", 3, [Poison, Grass], [cut])
Charizard = pokemon("Charizard", 6, [Fire, Flying], [cut, strength])
Blastoise = pokemon("Blastoise", 9, [Water], [surf, strength])
Butterfree = pokemon("Butterfree", 12, [Bug, Flying], [])
Beedrill = pokemon("Beedrill", 15, [Poison, Bug], [cut])
Pidgeot = pokemon("Pidgeot", 18, [Normal, Flying], [fly])
Raticate = pokemon("Raticate", 20, [Normal], [])
Fearow = pokemon("Fearow", 22, [Normal, Flying], [fly])
Arbok = pokemon("Arbok", 24, [Poison], [strength])
Raichu = pokemon("Raichu", 26, [Electric], [flash])
Sandslash = pokemon("Sandslash", 28, [Ground], [cut, strength])
Nidoqueen = pokemon("Nidoqueen", 31, [Poison, Ground], [surf, strength])
Nidoking = pokemon("Nidoking", 34, [Poison, Ground], [surf, strength])
Clefable = pokemon("Clefable", 36, [Normal], [strength, flash])
Ninetales = pokemon("Ninetales", 38, [Fire], [])
Wigglytuff = pokemon("Wigglytuff", 40, [Normal], [strength, flash])
Golbat = pokemon("Golbat", 42, [Poison, Flying], [])
Vileplume = pokemon("Vileplume", 45, [Poison, Grass], [cut])
Parasect = pokemon("Parasect", 47, [Bug, Grass], [cut])
Venomoth = pokemon("Venomoth", 49, [Poison, Bug], [])
Dugtrio = pokemon("Dugtrio", 51, [Ground], [])
Persian = pokemon("Persian", 53, [Normal], [])
Golduck = pokemon("Golduck", 55, [Water], [surf, strength])
Primeape = pokemon("Primeape", 57, [Fighting], [strength])
Arcanine = pokemon("Arcanine", 59, [Fire], [])
Alakazam = pokemon("Alakazam", 65, [Psychic], [flash])
Machamp = pokemon("Machamp", 68, [Fighting], [strength])
Golem = pokemon("Golem", 76, [Rock, Ground], [strength])
Slowbro = pokemon("Slowbro", 80, [Water, Psychic], [surf, strength, flash])
Farfetchd = pokemon("Farfetch'd", 83, [Normal, Flying], [cut, fly])
Dodrio = pokemon("Dodrio", 85, [Normal, Flying], [fly])
Dewgong = pokemon("Dewgong", 87, [Water, Ice], [surf, strength])
Gengar = pokemon("Gengar", 94, [Poison, Ghost], [strength])
Hitmonlee = pokemon("Hitmonlee", 106, [Fighting], [strength])
Hitmonchan = pokemon("Hitmonchan", 107, [Fighting], [strength])
MrMime = pokemon("Mr. Mime", 122, [Psychic], [flash])
Jynx = pokemon("Jynx", 124, [Psychic, Ice], [])
Pinsir = pokemon("Pinsir", 127, [Bug], [cut, strength])
Vaporeon = pokemon("Vaporeon", 134, [Water], [surf])
Jolteon = pokemon("Jolteon", 135, [Electric], [flash])
Flareon = pokemon("Flareon", 136, [Fire], [])
Omastar = pokemon("Omastar", 139, [Water, Rock], [surf])
Kabutops = pokemon("Kabutops", 141, [Water, Rock], [surf])
Snorlax = pokemon("Snorlax", 143, [Normal], [surf, strength])
Dragonite = pokemon("Dragonite", 149, [Flying, Dragon], [surf, strength])

totalPokemonList = [Venusaur, Charizard, Blastoise, Butterfree, Beedrill, Pidgeot, Raticate, Fearow,
                    Arbok, Raichu, Sandslash, Nidoqueen, Nidoking, Clefable, Ninetales, Wigglytuff,
                    Golbat, Vileplume, Parasect, Venomoth, Dugtrio, Persian, Golduck, Primeape,
                    Arcanine, Alakazam, Machamp, Golem, Slowbro, Farfetchd, Dodrio, Dewgong,
                    Gengar, Hitmonlee, Hitmonchan, MrMime, Jynx, Pinsir, Vaporeon, Jolteon,
                    Flareon, Omastar, Kabutops, Snorlax, Dragonite]

availablePokemonList = list(totalPokemonList)

starters = [Venusaur, Charizard, Blastoise]

party = []

hmList = [cut, fly, surf, strength, flash]


# function for verifying HM coverage
def checkHM(candidate):
    global party
    global hmList
    counter = 0
    if len(hmList) > 0:
        if len(candidate.HMs) > 0:
            for i in candidate.HMs:
                if hmList.count(i) > 0:
                    counter += 1
            if counter > 0:
                hmCoverage = list(candidate.HMs)
                for i in candidate.HMs:
                    if hmList.count(i) == 0:
                        hmCoverage.remove(i)
                if len(hmCoverage) > 0:
                    hmList.remove(random.choice(hmCoverage))
                    return 1
            else:
                return 0
        else:
            return 0
    else:
        return 1


# function for preventing selecting mutually exclusive Pokemon
def checkMutuallyExclusive(candidate):
    global party
    group1 = [Hitmonlee, Hitmonchan]
    group2 = [Vaporeon, Jolteon, Flareon]
    group3 = [Omastar, Kabutops]
    if group1.count(candidate) > 0:
        for i in party:
            if group1.count(i) > 0:
                return 0
    if group2.count(candidate) > 0:
        for i in party:
            if group2.count(i) > 0:
                return 0
    if group3.count(candidate) > 0:
        for i in party:
            if group3.count(i) > 0:
                return 0
    return 1


def checkSameType(candidate):
    global party
    partyTypes = []
    for i in party:
        for j in i.types:
            if partyTypes.count(j) == 0:
                partyTypes.append(j)
    for i in candidate.types:
        if partyTypes.count(i) > 0:
            return 0
    return 1



# function for selecting starter Pokemon
def selectStarter():
    global party
    global availablePokemonList
    chosenStarter = random.choice(starters)
    party.append(chosenStarter)
    # test code start
    #print("TEST: Successfully added member: " + chosenStarter.name)
    # test code end
    for i in range(3):
        availablePokemonList.remove(starters[i])

    # mark appropriate HMs as covered by the starter
    hmList.remove(random.choice(chosenStarter.HMs))

    secondSlotCandidates = list(availablePokemonList)
    if select2(secondSlotCandidates) == 1:
        return 1
    else:
        print("No valid team could be found with the given starter: " + chosenStarter.name)


# function for selecting the second Pokemon
def select2(pokemonPool):
    global party
    success1 = 0
    while success1 == 0:
        success2 = 0
        while success2 == 0:
            if len(pokemonPool) == 0:
                return 0
            potentialMember = random.choice(pokemonPool)
            if checkSameType(potentialMember) == 1:
                if checkHM(potentialMember) == 1:
                    if checkMutuallyExclusive(potentialMember) == 1:
                        success2 = 1
                    else:
                        pokemonPool.remove(potentialMember)
                else:
                    pokemonPool.remove(potentialMember)
            else:
                pokemonPool.remove(potentialMember)
        party.append(potentialMember)
        # test code start
        #print("TEST: Successfully added member: " + potentialMember.name)
        # test code end
        pokemonPool.remove(potentialMember)
        thirdSlotCandidates = list(pokemonPool)
        if select3(thirdSlotCandidates) == 1:
            success1 = 1
        else:
            party.remove(potentialMember)
    return 1


# function for selecting the third Pokemon
def select3(pokemonPool):
    global party
    success1 = 0
    while success1 == 0:
        success2 = 0
        while success2 == 0:
            if len(pokemonPool) == 0:
                return 0
            potentialMember = random.choice(pokemonPool)
            if checkSameType(potentialMember) == 1:
                if checkHM(potentialMember) == 1:
                    if checkMutuallyExclusive(potentialMember) == 1:
                        success2 = 1
                    else:
                        pokemonPool.remove(potentialMember)
                else:
                    pokemonPool.remove(potentialMember)
            else:
                pokemonPool.remove(potentialMember)
        party.append(potentialMember)
        # test code start
        #print("TEST: Successfully added member: " + potentialMember.name)
        # test code end
        pokemonPool.remove(potentialMember)
        fourthSlotCandidates = list(pokemonPool)
        if select4(fourthSlotCandidates) == 1:
            success1 = 1
        else:
            party.remove(potentialMember)
    return 1


# function for selecting the fourth Pokemon
def select4(pokemonPool):
    global party
    success1 = 0
    while success1 == 0:
        success2 = 0
        while success2 == 0:
            if len(pokemonPool) == 0:
                return 0
            potentialMember = random.choice(pokemonPool)
            if checkSameType(potentialMember) == 1:
                if checkHM(potentialMember) == 1:
                    if checkMutuallyExclusive(potentialMember) == 1:
                        success2 = 1
                    else:
                        pokemonPool.remove(potentialMember)
                else:
                    pokemonPool.remove(potentialMember)
            else:
                pokemonPool.remove(potentialMember)
        party.append(potentialMember)
        # test code start
        #print("TEST: Successfully added member: " + potentialMember.name)
        # test code end
        pokemonPool.remove(potentialMember)
        fifthSlotCandidates = list(pokemonPool)
        if select5(fifthSlotCandidates) == 1:
            success1 = 1
        else:
            party.remove(potentialMember)
    return 1


# function for selecting the fifth Pokemon
def select5(pokemonPool):
    global party
    success1 = 0
    while success1 == 0:
        success2 = 0
        while success2 == 0:
            if len(pokemonPool) == 0:
                return 0
            potentialMember = random.choice(pokemonPool)
            if checkSameType(potentialMember) == 1:
                if checkHM(potentialMember) == 1:
                    if checkMutuallyExclusive(potentialMember) == 1:
                        success2 = 1
                    else:
                        pokemonPool.remove(potentialMember)
                else:
                    pokemonPool.remove(potentialMember)
            else:
                pokemonPool.remove(potentialMember)
        party.append(potentialMember)
        # test code start
        #print("TEST: Successfully added member: " + potentialMember.name)
        # test code end
        pokemonPool.remove(potentialMember)
        sixthSlotCandidates = list(pokemonPool)
        if select6(sixthSlotCandidates) == 1:
            success1 = 1
        else:
            party.remove(potentialMember)
    return 1


# function for selecting the sixth Pokemon
def select6(pokemonPool):
    global party
    success = 0
    while success == 0:
        if len(pokemonPool) == 0:
            return 0
        potentialMember = random.choice(pokemonPool)
        if checkSameType(potentialMember) == 1:
            if checkHM(potentialMember) == 1:
                if checkMutuallyExclusive(potentialMember) == 1:
                    success = 1
                else:
                    pokemonPool.remove(potentialMember)
            else:
                pokemonPool.remove(potentialMember)
        else:
            pokemonPool.remove(potentialMember)
    party.append(potentialMember)
    # test code start
    #print("TEST: Successfully added member: " + potentialMember.name)
    # test code end
    return 1


# function for sorting the party
def sortParty():
    global party
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
    return party


# function for displaying the party
def displayParty():
    global party
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


if selectStarter() == 1:
    sortParty()
    displayParty()