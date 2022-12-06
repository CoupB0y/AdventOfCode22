import re

def readTextFromFile(filename):
    """Reads text from a file and returns it as a string

    Args:
        filename (String): filename to read from

    Returns:
        String: contents of the file
    """
    
    with open(filename, 'r') as f:
        return f.read()


def removeDuplicates(compartment):
    """Removes duplicate characters from a string

    Args:
        compartment (String): String of items in a compartment

    Returns:
        String: returns a string with no duplicate characters
    """
    return "".join(set(compartment))

    
def determinePriorityItems(rucksackInventory):
    """Adds priority items to a list

    Args:
        rucksackInventory (list): list of items in a compartment

    Returns:
        list: returns a list of priority items
    """

    priorityList = []


    for inventory in rucksackInventory:
        compartment1, compartment2 = inventory[:len(inventory)//2], inventory[len(inventory)//2:]
        compartment1 = removeDuplicates(compartment1)
        compartment2 = removeDuplicates(compartment2)
        for item in compartment1:
            if item in compartment2:
                priorityList.append(item)
            
    return priorityList

def calculateTotalPriority(priorityList):
    """Calculates the total priority of the items in the list

    Args:
        priorityList (list): list of priority items

    Returns:
        int: returns the total priority of the items in the list
    """
    itemPriority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
                    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A':27, 
                    'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 
                    'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52
                    }
    totalPriority = 0
    for item in priorityList:
        totalPriority += itemPriority[item]
    
    return totalPriority


def getBadgeList(fileData): 
    """Returns list of badges in each group of three elves
    Args:
        fildData (String): String of all the data in the file
    
    Returns:
        list: list of badges in each group of three elves
    """
    elfGroups = [x.strip().split('\n') for x in re.findall('((?:[^\n]+\n?){1,3})', fileData)]
    badgeList = []
    for group in elfGroups:
        for i in range(len(group)):
            group[i] = removeDuplicates(group[i])
        for item in group[0]:
            if item in group[1] and item in group[2]:
                badgeList.append(item)
                break
    
    return badgeList

def main():
    """Main function that reads in input file"""
    
    fileData = readTextFromFile("rucksackInventory.txt")
    rucksackInventory = fileData.splitlines()
    priorityList = determinePriorityItems(rucksackInventory)
    totalPriority = calculateTotalPriority(priorityList)
    
    print("Total priority(pt1): ", totalPriority)
    
    badgeList = getBadgeList(fileData)
    badgePriority = calculateTotalPriority(badgeList)
    
    print("Badge priority: ", badgePriority)


if __name__ == '__main__':
    main()