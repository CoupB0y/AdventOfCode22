from elf import Elf
from itertools import groupby


def readTextFromFile(filename):
    """Reads text from a file and returns it as a string

    Args:
        filename (String): filename to read from

    Returns:
        String: contents of the file
    """
    
    with open(filename, 'r') as f:
        return f.read()
    
  
def getMaxCalories(elves):
    """Finds the elf carrying the most calories

    Args:
        elves (list): List Elf objects

    Returns:
        int: Total calories carried by the elf wih the most calories
    """
    
    maxCalories = 0
    for elf in elves:
        if elf.getTotalCalories() > maxCalories:
            maxCalories = elf.getTotalCalories()
    return maxCalories


def getTopThree(elves):
    """Returns the top three elves carrying the most calories

    Args:
        elves (list): list of Elf objects

    Returns:
        list: list of top three Elf objects carrying the most calories
    """
    
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
    """Main function that reads the input file and creates Elf objects"""
    
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
    