import random
import tkinter


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
Ghost = type("Ghost")
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
    def __init__(self, name, number, types, HMs, coverage):
        self.name = name
        self.number = number
        self.types = types
        self.HMs = HMs
        self.coverage = coverage

Venusaur = pokemon("Venusaur", 3, [Grass, Poison], [cut], [Grass])
Charizard = pokemon("Charizard", 6, [Fire, Flying], [cut, strength], [Fire, Fighting, Ground])
Blastoise = pokemon("Blastoise", 9, [Water], [surf, strength], [Water, Fighting, Ground, Ice])
Butterfree = pokemon("Butterfree", 12, [Bug, Flying], [], [Grass, Psychic])
Beedrill = pokemon("Beedrill", 15, [Bug, Poison], [cut], [Bug])
Pidgeot = pokemon("Pidgeot", 18, [Normal, Flying], [fly], [Flying])
Raticate = pokemon("Raticate", 20, [Normal], [], [Water, Electric, Ground, Ice])
Fearow = pokemon("Fearow", 22, [Normal, Flying], [fly], [Flying])
Arbok = pokemon("Arbok", 24, [Poison], [strength], [Rock, Ground])
Raichu = pokemon("Raichu", 26, [Electric], [flash], [Electric, Fighting])
Sandslash = pokemon("Sandslash", 28, [Ground], [cut, strength], [Fighting, Rock, Ground])
Nidoqueen = pokemon("Nidoqueen", 31, [Poison, Ground], [surf, strength], [Fire, Water, Electric, Fighting, Rock, Ground, Ice])
Nidoking = pokemon("Nidoking", 34, [Poison, Ground], [surf, strength], [Fire, Water, Electric, Fighting, Rock, Ground, Ice])
Clefable = pokemon("Clefable", 36, [Normal], [strength, flash], [Fire, Water, Electric, Grass, Fighting, Psychic, Ice])
Ninetales = pokemon("Ninetales", 38, [Fire], [], [Fire, Ground])
Wigglytuff = pokemon("Wigglytuff", 40, [Normal], [strength, flash], [Fire, Water, Electric, Grass, Fighting, Psychic, Ice])
Golbat = pokemon("Golbat", 42, [Poison, Flying], [], [])
Vileplume = pokemon("Vileplume", 45, [Poison, Grass], [cut], [Grass])
Parasect = pokemon("Parasect", 47, [Bug, Grass], [cut], [Grass, Ground])
Venomoth = pokemon("Venomoth", 49, [Bug, Poison], [], [Grass, Psychic])
Dugtrio = pokemon("Dugtrio", 51, [Ground], [], [Rock, Ground])
Persian = pokemon("Persian", 53, [Normal], [], [Water, Electric])
Golduck = pokemon("Golduck", 55, [Water], [surf, strength], [Water, Fighting, Ground, Psychic, Ice])
Primeape = pokemon("Primeape", 57, [Fighting], [strength], [Electric, Fighting, Rock, Ground])
Arcanine = pokemon("Arcanine", 59, [Fire], [], [Fire, Ground])
Poliwrath = pokemon("Poliwrath", 62, [Water, Fighting], [surf, strength], [Water, Fighting, Ground, Ice])
Alakazam = pokemon("Alakazam", 65, [Psychic], [flash], [Fighting, Ground, Psychic])
Machamp = pokemon("Machamp", 68, [Fighting], [strength], [Fire, Fighting, Rock, Ground])
Victreebel = pokemon("Victreebel", 71, [Grass, Poison], [cut], [Grass])
Tentacruel = pokemon("Tentacruel", 73, [Water, Poison], [cut, surf], [Water, Ice])
Golem = pokemon("Golem", 76, [Rock, Ground], [strength], [Fire, Fighting, Rock, Ground])
Rapidash = pokemon("Rapidash", 78, [Fire], [], [Fire])
Slowbro = pokemon("Slowbro", 80, [Water, Psychic], [surf, strength, flash], [Fire, Water, Fighting, Ground, Psychic, Ice])
Magneton = pokemon("Magneton", 82, [Electric], [flash], [Electric])
Farfetchd = pokemon("Farfetch'd", 83, [Normal, Flying], [cut, fly], [Flying])
Dodrio = pokemon("Dodrio", 85, [Normal, Flying], [fly], [Flying])
Dewgong = pokemon("Dewgong", 87, [Water, Ice], [surf, strength], [Water, Ice])
Muk = pokemon("Muk", 89, [Poison], [], [Fire, Electric, Poison])
Cloyster = pokemon("Cloyster", 91, [Water, Ice], [surf], [Water, Ice])
Gengar = pokemon("Gengar", 94, [Ghost, Poison], [strength], [Electric, Fighting, Psychic])
Onix = pokemon("Onix", 95, [Rock, Ground], [strength], [Rock, Ground])
Hypno = pokemon("Hypno", 97, [Psychic], [flash], [Fighting, Psychic])
Kingler = pokemon("Kingler", 99, [Water], [cut, surf, strength], [Water, Ice])
Electrode = pokemon("Electrode", 101, [Electric], [flash], [Electric])
Exeggutor = pokemon("Exeggutor", 103, [Grass, Psychic], [strength], [Grass, Psychic])
Marowak = pokemon("Marowak", 105, [Ground], [strength], [Fire, Water, Fighting, Ground, Ice])
Hitmonlee = pokemon("Hitmonlee", 106, [Fighting], [strength], [Fighting])
Hitmonchan = pokemon("Hitmonchan", 107, [Fighting], [strength], [Fire, Electric, Fighting, Ice])
Lickitung = pokemon("Lickitung", 108, [Normal], [cut, surf, strength], [Fire, Water, Electric, Fighting, Ground, Ice])
Weezing = pokemon("Weezing", 110, [Poison], [], [Fire, Electric, Poison])
Rhydon = pokemon("Rhydon", 112, [Ground, Rock], [surf, strength], [Fire, Water, Electric, Fighting, Rock, Ground, Ice])
Chansey = pokemon("Chansey", 113, [Normal], [strength, flash], [Fire, Water, Electric, Grass, Fighting, Psychic, Ice])
Tangela = pokemon("Tangela", 114, [Grass], [cut], [Grass])
Kangaskhan = pokemon("Kangaskhan", 115, [Normal], [surf, strength], [Fire, Water, Electric, Fighting, Rock, Ground, Ice])
Seadra = pokemon("Seadra", 117, [Water], [surf], [Water, Ice])
Seaking = pokemon("Seaking", 119, [Water], [surf], [Water, Ice])
Starmie = pokemon("Starmie", 121, [Water, Psychic], [surf, flash], [Water, Electric, Psychic, Ice])
MrMime = pokemon("Mr. Mime", 122, [Psychic], [flash], [Electric, Grass, Fighting, Psychic])
Scyther = pokemon("Scyther", 123, [Bug, Flying], [cut], [])
Jynx = pokemon("Jynx", 124, [Ice, Psychic], [], [Water, Fighting, Psychic, Ice])
Electabuzz = pokemon("Electabuzz", 125, [Electric], [strength, flash], [Electric, Fighting, Psychic])
Magmar = pokemon("Magmar", 126, [Fire], [strength], [Fire, Fighting, Psychic])
Pinsir = pokemon("Pinsir", 127, [Bug], [cut, strength], [Fighting])
Tauros = pokemon("Tauros", 128, [Normal], [strength], [Fire, Electric, Ground, Ice])
Gyarados = pokemon("Gyarados", 130, [Water, Flying], [surf, strength], [Fire, Water, Electric, Ice])
Lapras = pokemon("Lapras", 131, [Water, Ice], [surf, strength], [Water, Electric, Grass, Psychic, Ice])
Ditto = pokemon("Ditto", 132, [Normal], [], [])
Vaporeon = pokemon("Vaporeon", 134, [Water], [surf], [Water, Ice])
Jolteon = pokemon("Jolteon", 135, [Electric], [flash], [Electric, Fighting])
Flareon = pokemon("Flareon", 136, [Fire], [], [Fire])
Porygon = pokemon("Porygon", 137, [Normal], [flash], [Electric, Psychic, Ice])
Omastar = pokemon("Omastar", 139, [Rock, Water], [surf], [Water, Fighting, Ice])
Kabutops = pokemon("Kabutops", 141, [Rock, Water], [surf], [Water, Fighting, Ice])
Aerodactyl = pokemon("Aerodactyl", 142, [Rock, Flying], [fly], [Fire, Flying])
Snorlax = pokemon("Snorlax", 143, [Normal], [surf, strength], [Fire, Water, Electric, Grass, Fighting, Rock, Ground, Psychic, Ice])
Articuno = pokemon("Articuno", 144, [Ice, Flying], [fly], [Water, Flying, Ice])
Zapdos = pokemon("Zapdos", 145, [Electric, Flying], [fly, flash], [Electric, Flying])
Moltres = pokemon("Moltres", 146, [Fire, Flying], [fly], [Fire, Flying])
Dragonite = pokemon("Dragonite", 149, [Dragon, Flying], [surf, strength], [Fire, Water, Electric, Ice])

totalPokemonList = [Venusaur, Charizard, Blastoise, Butterfree, Beedrill, Pidgeot, Raticate, Fearow,
                    Arbok, Raichu, Sandslash, Nidoqueen, Nidoking, Clefable, Ninetales, Wigglytuff,
                    Golbat, Vileplume, Parasect, Venomoth, Dugtrio, Persian, Golduck, Primeape,
                    Arcanine, Poliwrath, Alakazam, Machamp, Victreebel, Tentacruel, Golem, Rapidash,
                    Slowbro, Magneton, Farfetchd, Dodrio, Dewgong, Muk, Cloyster, Gengar,
                    Onix, Hypno, Kingler, Electrode, Exeggutor, Marowak, Hitmonlee, Hitmonchan,
                    Lickitung, Weezing, Rhydon, Chansey, Tangela, Kangaskhan, Seadra, Seaking,
                    Starmie, MrMime, Scyther, Jynx, Electabuzz, Magmar, Pinsir, Tauros,
                    Gyarados, Lapras, Ditto, Vaporeon, Jolteon, Flareon, Porygon, Omastar,
                    Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos, Moltres, Dragonite]

availablePokemonList = list(totalPokemonList)

gameVersion = ""

party = []

hmList = [cut, fly, surf, strength, flash]
firstHM = 0
secondHM = 0
thirdHM = 0
fourthHM = 0
fifthHM = 0

alreadyRun = 0


# function for selecting game version and changing Pokemon availability accordingly
def chooseVersion():
    global availablePokemonList
    global gameVersion
    redExclusives = [Arbok, Vileplume, Primeape, Arcanine, Scyther, Electabuzz]
    blueExclusives = [Sandslash, Ninetales, Persian, Victreebel, Magmar, Pinsir]
    versionsList = ["Red", "Blue"]
    gameVersion = random.choice(versionsList)
    if gameVersion == "Red":
        for i in blueExclusives:
            availablePokemonList.remove(i)
    elif gameVersion == "Blue":
        for i in redExclusives:
            availablePokemonList.remove(i)


# function for preventing adding Pokemon of the same type as previously selected Pokemon
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


# function for verifying HM coverage
def checkHM(candidate, slotNum):
    global party
    global hmList
    global secondHM
    global thirdHM
    global fourthHM
    global fifthHM
    counter = 0
    if len(hmList) > 0:
        if len(candidate.HMs) > 0:
            for i in candidate.HMs:
                if i in hmList:
                    counter += 1
            if counter > 0:
                hmCoverage = list(candidate.HMs)
                for i in candidate.HMs:
                    if i not in hmList:
                        hmCoverage.remove(i)
                if len(hmCoverage) > 0:
                    removeHM = random.choice(hmCoverage)
                    hmList.remove(removeHM)
                    if slotNum == 2:
                        secondHM = removeHM
                    elif slotNum == 3:
                        thirdHM = removeHM
                    elif slotNum == 4:
                        fourthHM = removeHM
                    elif slotNum == 5:
                        fifthHM = removeHM
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


# function for verifying move coverage against all relevant type combinations
def checkMoveCoverage(candidate):
    global party
    firstCheck = [Bug, Fighting, Ground, Ice]
    totalMoveCoverage = []
    for i in party:
        if len(i.coverage) > 0:
            for j in i.coverage:
                totalMoveCoverage.append(j)
    if len(candidate.coverage) > 0:
        for i in candidate.coverage:
            totalMoveCoverage.append(i)
    if all(item in totalMoveCoverage for item in firstCheck):
        if Electric in totalMoveCoverage:
            return 1
        else:
            if Rock in totalMoveCoverage:
                if Grass in totalMoveCoverage:
                    return 1
                else:
                    return 0
            else:
                return 0
    else:
        return 0


# function for selecting starter Pokemon
def selectStarter():
    global party
    global availablePokemonList
    global hmList
    starters = [Venusaur, Charizard, Blastoise]
    chosenStarter = random.choice(starters)
    party.append(chosenStarter)
    # test code start
    #print("TEST: Successfully added member: " + chosenStarter.name)
    # test code end
    for i in range(3):
        availablePokemonList.remove(starters[i])

    # mark appropriate HMs as covered by the starter
    hmList.remove(random.choice(chosenStarter.HMs))

    nextSlotCandidates = list(availablePokemonList)
    if selectSlot(nextSlotCandidates, 2) == 1:
        return 1
    else:
        return 0


# function for selecting the remaining five Pokemon
def selectSlot(pokemonPool, slotNum):
    global party
    global hmList
    global secondHM
    global thirdHM
    global fourthHM
    global fifthHM
    success1 = 0
    while success1 == 0:
        success2 = 0
        while success2 == 0:
            if len(pokemonPool) == 0:
                return 0
            potentialMember = random.choice(pokemonPool)
            if checkSameType(potentialMember) == 1:
                if checkHM(potentialMember, slotNum) == 1:
                    if checkMutuallyExclusive(potentialMember) == 1:
                        if slotNum == 6:
                            if checkMoveCoverage(potentialMember) == 1:
                                success2 = 1
                            else:
                                pokemonPool.remove(potentialMember)
                        else:
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
        nextSlotCandidates = list(pokemonPool)
        if slotNum < 6:
            if selectSlot(nextSlotCandidates, slotNum + 1) == 1:
                success1 = 1
            else:
                party.remove(potentialMember)
                if slotNum == 2:
                    hmList.append(secondHM)
                elif slotNum == 3:
                    hmList.append(thirdHM)
                elif slotNum == 4:
                    hmList.append(fourthHM)
                elif slotNum == 5:
                    hmList.append(fifthHM)
        else:
            success1 = 1
    return 1


# function for sorting the party
def sortParty():
    global party
    if len(party) == 6:
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
def displayResult(success):
    global party
    global label_memberList
    global label_noTeam
    if success == 1:
        for i in range(6):
            if len(party[i].HMs) == 0:
                label_memberList[i] = tkinter.Label(text=party[i].name + ' - None')
                label_memberList[i].pack(side = 'top')
            elif len(party[i].HMs) == 1:
                label_memberList[i] = tkinter.Label(text=party[i].name + ' - ' + party[i].HMs[0].name)
                label_memberList[i].pack(side = 'top')
            elif len(party[i].HMs) == 2:
                label_memberList[i] = tkinter.Label(text=party[i].name + ' - ' + party[i].HMs[0].name + ', ' + party[i].HMs[1].name)
                label_memberList[i].pack(side = 'top')
            elif len(party[i].HMs) == 3:
                label_memberList[i] = tkinter.Label(text=party[i].name + ' - ' + party[i].HMs[0].name + ', ' + party[i].HMs[1].name + ', ' + party[i].HMs[2].name)
                label_memberList[i].pack(side = 'top')
    else:
        label_noTeam = tkinter.Label(text='No valid team could be found with the given starter: ' + party[0].name)
        label_noTeam.pack(side = 'top')


# function for clearing the screen when repeating team generation
def hideResult():
    global label_version
    global label_memberList
    global label_noTeam
    if label_version.winfo_viewable() == True:
        label_version.pack_forget()
    if label_memberList[5].winfo_viewable() == True:
        for i in label_memberList:
            i.pack_forget()
    if label_noTeam.winfo_viewable() == True:
        label_noTeam.pack_forget()


def doTheThing():
    global availablePokemonList
    global gameVersion
    global party
    global hmList
    global firstHM
    global secondHM
    global thirdHM
    global fourthHM
    global fifthHM
    global alreadyRun
    availablePokemonList = list(totalPokemonList)
    gameVersion = ""
    party = []
    hmList = [cut, fly, surf, strength, flash]
    firstHM = 0
    secondHM = 0
    thirdHM = 0
    fourthHM = 0
    fifthHM = 0
    hideResult()
    chooseVersion()
    success = selectStarter()
    global label_version
    label_version = tkinter.Label(text=gameVersion + ' Version')
    label_version.pack(side = 'top')
    sortParty()
    displayResult(success)
        
        


root = tkinter.Tk()
root.geometry('400x190')
root.title('Pokemon Team Generator')

label_version = tkinter.Label()
label_member1 = tkinter.Label()
label_member2 = tkinter.Label()
label_member3 = tkinter.Label()
label_member4 = tkinter.Label()
label_member5 = tkinter.Label()
label_member6 = tkinter.Label()
label_memberList = [label_member1, label_member2, label_member3, label_member4, label_member5, label_member6]
label_noTeam = tkinter.Label()

button = tkinter.Button(root, text = 'Generate a Team', command = doTheThing)
button.pack(side = 'top')

root.mainloop()