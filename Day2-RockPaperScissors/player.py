
class Player:
    """Player class that stores the score of the player"""
    
    def __init__(self):
        """Constructor for Player class"""
        
        self.score = 0
        
    def getScore(self):
        """Returns the score

        Returns:
            int: returns Player score
        """
        return self.score
