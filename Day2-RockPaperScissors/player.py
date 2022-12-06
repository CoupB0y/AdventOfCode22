
class Player:
    """Player class
    """
    def __init__(self):
        """Constructor for Player class
        """
        self.score = 0
        
    def getScore(self):
        """Returns the score

        Returns:
            int: returns Player score
        """
        return self.score
    
    def setScore(self, score):
        """Sets the score"""
        self.score = score
