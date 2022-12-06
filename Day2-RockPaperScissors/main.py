from player import Player


def readTextFromFile(filename):
    """Reads text from a file and returns it as a string

    Args:
        filename (String): filename to read from

    Returns:
        String: contents of the file
    """
    with open(filename, 'r') as f:
        return f.read()


def determineOutcome1(strategyList, player): # used in pt1
    """Determines the outcome of the game using pt1 strategy and adds to the Player's score

    Args:
        strategyList (list): list of move strategies for the Player
        player (Player): Player object
    """
    userMoveScores = {'X': 1 , 'Y': 2, 'Z': 3}
    
    for round in strategyList: 
        roundList = round.split()
        if (roundList[0] == 'A' and roundList[1] == 'Y'):
            player.score += 6
            player.score += userMoveScores[roundList[1]]
        elif ((roundList[0] == 'A' and roundList[1] == 'Z') or (roundList[0] == 'B' and roundList[1] == 'X') or (roundList[0] == 'C' and roundList[1] == 'Y')):
            player.score += 0
            player.score += userMoveScores[roundList[1]]
        elif ((roundList[0] == 'A' and roundList[1] == 'Y') or (roundList[0] == 'B' and roundList[1] == 'Z') or (roundList[0] == 'C' and roundList[1] == 'X')):
            player.score += 6
            player.score += userMoveScores[roundList[1]]
        else:
            player.score += 3
            player.score += userMoveScores[roundList[1]]         

def determineOutcome2(strategyList, player): # used in pt2 
    """Determines the outcome of the game using pt2 strategy and adds to the Player's score
    Args:
        strategyList (list): list of move strategies for the Player
        player (Player): Player object
    """
    for round in strategyList:
        roundList = round.split()
        if (roundList[1] == 'X'):
            if(roundList[0] == 'A'):
                player.score += 3
            if(roundList[0] == 'B'):
                player.score += 1
            if(roundList[0] == 'C'):
                player.score += 2

        if (roundList[1] == 'Y'):
            player.score += 3

            if(roundList[0] == 'A'):
                player.score += 1
            if(roundList[0] == 'B'):
                player.score += 2
            if(roundList[0] == 'C'):
                player.score += 3

        if (roundList[1] == 'Z'):
            player.score += 6

            if(roundList[0] == 'A'):
                player.score += 2
            if(roundList[0] == 'B'):
                player.score += 3
            if(roundList[0] == 'C'):
                player.score += 1


def main():
    """Main function
    """
    
    player = Player()
    fileData = readTextFromFile('strategy_guide.txt')
    strategyList = fileData.splitlines()
    # determineOutcome1(strategyList, player)
    determineOutcome2(strategyList, player)

    print(f"Total Score: {player.getScore()}")


if __name__ == '__main__':
    main()
