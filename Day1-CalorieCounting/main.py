from elf import Elf
from itertools import groupby


def readTextFromFile(filename):
    with open(filename, 'r') as f:
        return f.read()
    

''' 
finds elf carrying the most calories 
used in pt1
'''   
def getMaxCalories(elves):
    maxCalories = 0
    for elf in elves:
        if elf.getTotalCalories() > maxCalories:
            maxCalories = elf.getTotalCalories()
    return maxCalories

'''
returns list of top three elves with most calories
used in pt2
'''
def getTopThree(elves):
    topThree = []
    for elf in elves:
        if len(topThree) < 3:
            topThree.append(elf)
        else:
            for i in range(0, len(topThree)):
                if elf.getTotalCalories() > topThree[i].getTotalCalories():
                    topThree[i] = elf
                    break
    return topThree


def main():
    elves = []
    fileData = readTextFromFile("calorie_count.txt").splitlines()
    calorielList = [list(g) for k, g in groupby(fileData, key=bool) if k]
    for subList in calorielList:
        elf = Elf()
        for calories in subList:
            elf.addCalories(int(calories))
        elves.append(elf)
    print("Part 1: " + str(getMaxCalories(elves)))
    
    topThree = getTopThree(elves)
    maxColories = 0
    for elf in getTopThree(elves):
        maxColories += elf.getTotalCalories()
    print("Part 2: " + str(maxColories))
    
        
if __name__ == "__main__":
    main()
    