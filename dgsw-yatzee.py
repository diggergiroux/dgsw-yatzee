import random

print("Yatzee")
points_taken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_of_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_of_dice = [0, 0, 0, 0, 0]
keepDice = "00000"

def simple_number(theNumber):
    """
    method for the first 6 bins
    """
    numFound = list_of_dice.count(theNumber)
    list_of_points[(theNumber - 1)] = numFound * theNumber     

def of_a_kind(minCount):
    mostCommon = max(list_of_dice, key = list_of_dice.count)
    numFound = list_of_dice.count(mostCommon)
    if numFound >= minCount:
        if minCount == 3:
            list_of_points[6] = sum(list_of_dice)
        elif minCount == 4:
            list_of_points[7] = sum(list_of_dice)
        else:
            list_of_points[11] = 50

def fullhouse():
    mostCommon = max(list_of_dice, key = list_of_dice.count)
    numFound = list_of_dice.count(mostCommon)
    if numFound == 3:
        leastCommon = min(list_of_dice, key = list_of_dice.count)
        numFound = list_of_dice.count(leastCommon)
        if numFound == 2:
            list_of_points[8] = sum(list_of_dice)
    elif numFound == 5:
        list_of_points[8] = sum(list_of_dice)

def straight(minCount):
    dieFound = [0, 0, 0, 0, 0, 0]
    for z in range (0, 5):
        thisDie = list_of_dice[z]
        thisDie -= 1
        dieFound[thisDie] = 1
    maxLength = 0
    curLength = 0
    for z in range (0, 6):
        if dieFound[z] == 1:
            curLength += 1
            if curLength > maxLength:
                maxLength = curLength
        else:
            curLength = 0
    if maxLength >= minCount:
        if minCount == 4:
            list_of_points[9] = 35
        elif minCount == 5:
            list_of_points[10] = 40

for x in range(0, 13):
    list_of_dice = [0, 0, 0, 0, 0]
    for y in range(0, 3):
        for z in range(0, 5):
            if list_of_dice[z] == 0:
                list_of_dice[z] = random.randrange(1, 7) 
        print(list_of_dice)
        if y < 2:
            keepDice = input("Select Dice to Keep\n")
            for z in range(0, len(list_of_dice)):
                die = keepDice[z]
                if die == "0":
                    list_of_dice[z] = 0
    sBI = 0
    while (sBI == 0):
        selectBin = input("Select Bin to Use\n")
        sBI = int(selectBin)
        if sBI > 0 and sBI < 13:
            if points_taken[sBI] == 1:
                sBI = 0
            else:
                points_taken[sBI] = 1
    if sBI > 0 and sBI < 7:
        simple_number(sBI)
    elif sBI == 7:
        of_a_kind(3)
    elif sBI == 8:
        of_a_kind(4)
    elif sBI == 9:
        fullhouse()
    elif sBI == 10:
        straight(4)
    elif sBI == 11:
        straight(5)
    elif sBI == 12:
        of_a_kind(5)
    else :
        list_of_points[12] = sum(list_of_dice)
    print(list_of_points)
topScore = 0
for z in range (0, 6):
    topScore += list_of_points[z]
totalScore = sum(list_of_points)
if topScore >= 63:
    totalScore += 35
print(totalScore)
print("The End")
