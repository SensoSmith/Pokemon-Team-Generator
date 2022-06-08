import random
import tkinter as tk
from tkinter import ttk
import RedBlue

gen = RedBlue

# function for setting the game version
def setVersion():
    global gameVersion
    gameVersion = combo_versions.get()
    if gameVersion == "Red" or "Blue":
        gen = RedBlue


# function for setting starters
def setStarters():
    global starters
    starters = list(gen.starters)
    if combo_starters.get() == gen.starterOptions[0]:
        starters.clear()
        starters.append(gen.starters[0])
    elif combo_starters.get() == gen.starterOptions[1]:
        starters.clear()
        starters.append(gen.starters[1])
    elif combo_starters.get() == gen.starterOptions[2]:
        starters.clear()
        starters.append(gen.starters[2])
    elif combo_starters.get() == 'None':
        for i in gen.starters:
            starters.remove(i)


# function changing Pokemon availability according to game version
def removeVersionExclusives():
    global availablePokemonList
    global gameVersion
    if gameVersion == gen.versionsList[0]:
        for i in gen.exclusivesListList[1]:
            availablePokemonList.remove(i)
    elif gameVersion == gen.versionsList[1]:
        for i in gen.exclusivesListList[0]:
            availablePokemonList.remove(i)


# function for removing legendaries if necessary
def determineLegendaries():
    global availablePokemonList
    if legendariesCheck.get() == 0:
        for i in gen.legendaries:
            availablePokemonList.remove(i)


# function for preventing adding Pokemon of the same type as previously selected Pokemon
def checkSameType(candidate):
    global party
    if typeOverlapCheck.get() == 0:
        partyTypes = []
        for i in party:
            for j in i.types:
                if partyTypes.count(j) == 0:
                    partyTypes.append(j)
        for i in candidate.types:
            if partyTypes.count(i) > 0:
                return 0
        return 1
    else:
        return 1


# function for preventing selecting mutually exclusive Pokemon
def checkMutuallyExclusive(candidate):
    global party
    for i in gen.MElist:
        if i.count(candidate) > 0:
            for j in party:
                if i.count(j) > 0:
                    return 0
    return 1


# function for verifying HM coverage
def checkHM(candidate, slotNum):
    global party
    hmList = list(gen.hmList)
    coverage = []
    if slotNum == 5:
        for i in party:
            if len(i.HMs) > 0:
                return 1
        if len(candidate.HMs) > 0:
            return 1
        else:
            return 0
    if slotNum == 6:
        for i in party:
            if len(i.HMs) > 0:
                for j in i.HMs:
                    if coverage.count(j) == 0:
                        coverage.append(j)
        if len(candidate.HMs) > 0:
            for i in candidate.HMs:
                if coverage.count(i) == 0:
                    coverage.append(i)
        if len(coverage) == len(hmList):
            return 1
        else:
            return 0


# function for selecting starter Pokemon
def selectStarter():
    global party
    global availablePokemonList
    global starters
    setStarters()
    if len(starters) > 0:
        chosenStarter = random.choice(starters)
    else:
        chosenStarter = random.choice(availablePokemonList)
        availablePokemonList.remove(chosenStarter)
    party.append(chosenStarter)
    # test code start
    #print("TEST: Successfully added member: " + chosenStarter.name)
    # test code end
    for i in gen.starters:
        availablePokemonList.remove(i)
    nextSlotCandidates = list(availablePokemonList)
    if selectSlot(nextSlotCandidates, 2) == 1:
        return 1
    else:
        return 0


# function for selecting the remaining five Pokemon
def selectSlot(pokemonPool, slotNum):
    global party
    success1 = 0
    while success1 == 0:
        success2 = 0
        while success2 == 0:
            if len(pokemonPool) == 0:
                return 0
            potentialMember = random.choice(pokemonPool)
            if checkSameType(potentialMember) == 1:
                if checkMutuallyExclusive(potentialMember) == 1:
                    if slotNum >= 5:
                        if checkHM(potentialMember, slotNum) == 1:
                            if slotNum == 5:
                                success2 = 1
                            elif slotNum == 6:
                                if gen.checkMoveCoverage(party, potentialMember) == 1:
                                    success2 = 1
                                else:
                                    pokemonPool.remove(potentialMember)
                        else:
                            pokemonPool.remove(potentialMember)
                    else:
                        success2 = 1
                else:
                    pokemonPool.remove(potentialMember)
            else:
                pokemonPool.remove(potentialMember)
        party.append(potentialMember)
        # test code start
        #print("TEST: Added member: " + potentialMember.name)
        # test code end
        pokemonPool.remove(potentialMember)
        nextSlotCandidates = list(pokemonPool)
        if slotNum < 6:
            if selectSlot(nextSlotCandidates, slotNum + 1) == 1:
                success1 = 1
            else:
                party.remove(potentialMember)
                # test code start
                #print("TEST: Removed member: " + potentialMember.name)
                # test code end
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
    if success == 1:
        for i in range(6):
            if len(party[i].HMs) == 0:
                label_memberList[i].config(text=party[i].name + ' - None')
            elif len(party[i].HMs) == 1:
                label_memberList[i].config(text=party[i].name + ' - ' + party[i].HMs[0].name)
            elif len(party[i].HMs) == 2:
                label_memberList[i].config(text=party[i].name + ' - ' + party[i].HMs[0].name + ', ' + party[i].HMs[1].name)
            elif len(party[i].HMs) == 3:
                label_memberList[i].config(text=party[i].name + ' - ' + party[i].HMs[0].name + ', ' + party[i].HMs[1].name + ', ' + party[i].HMs[2].name)
    else:
        label_memberList[0].config(text='No valid team could be found with the given starter: ' + party[0].name)


# function for clearing the screen when repeating team generation
def hideResult():
    global label_memberList
    for i in label_memberList:
        i.config(text = '')


# function to run the entire process of team generation
def generateTeam():
    hideResult()
    setVersion()
    global gameVersion
    global availablePokemonList
    global party
    availablePokemonList = list(gen.totalPokemonList)
    party = []
    removeVersionExclusives()
    determineLegendaries()
    teamFound = selectStarter()
    sortParty()
    displayResult(teamFound)


root = tk.Tk()
root.geometry('400x270')
root.title('Pokemon Team Generator')

button = tk.Button(root, text = 'Generate a Team', command = generateTeam)
button.pack(side = 'top')

legendariesCheck = tk.IntVar()
chkBtn_allowLegendaries = tk.Checkbutton(root, text = 'Allow Legendaries', variable = legendariesCheck, onvalue = 1, offvalue = 0)
chkBtn_allowLegendaries.pack(side = 'bottom')

typeOverlapCheck = tk.IntVar()
chkBtn_allowTypeOverlap = tk.Checkbutton(root, text = 'Allow Overlapping Types', variable = typeOverlapCheck, onvalue = 1, offvalue = 0)
chkBtn_allowTypeOverlap.pack(side = 'bottom')

versionOptions = ['Red', 'Blue']
versionCheck = tk.StringVar
combo_versions = ttk.Combobox(root, textvariable = versionOptions, values = versionOptions)
combo_versions.current(0)
combo_versions.pack(side = 'top')

starterOptions = list(gen.starterOptions)
starterOptions.append('Random')
starterOptions.append('None')
starterCheck = tk.StringVar
combo_starters = ttk.Combobox(root, textvariable = starterOptions, values = starterOptions)
combo_starters.current(0)
combo_starters.pack(side = 'top')

label_member1 = tk.Label(text = '')
label_member2 = tk.Label(text = '')
label_member3 = tk.Label(text = '')
label_member4 = tk.Label(text = '')
label_member5 = tk.Label(text = '')
label_member6 = tk.Label(text = '')
label_memberList = [label_member1, label_member2, label_member3, label_member4, label_member5, label_member6]
for i in label_memberList:
    i.pack(side = 'top')

root.mainloop()