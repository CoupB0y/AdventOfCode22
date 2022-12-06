class Elf:
    """Elf class that keeps track of calories and total calories"""
    
    def __init__(self):
        """Constructor for Elf class"""

        self.calories = []
        self.totalCalories = 0
       
    def addCalories(self, calories):
        """Adds calories to the list of calories and updates the total calories

        Args:
            calories (int): adds calories to the list of calories
        """
        self.calories.append(calories)
        self.totalCalories += calories
        
    def getTotalCalories(self):
        """Returns the total calories the elf is carrying

        Returns:
            int: _description_
        """
        return self.totalCalories
    
    def getCalories(self):
        """Return the list of calories
        Returns:
            list: list of calories
        """

        return self.calories
          