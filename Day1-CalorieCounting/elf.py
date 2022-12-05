class Elf:
    def __init__(self):
        self.calories = []
        self.totalCalories = 0
       
    def addCalories(self, calories):
        self.calories.append(calories)
        self.totalCalories += calories
        
    def getTotalCalories(self):
        return self.totalCalories
    
    def getCalories(self):
        return self.calories
    
    def __str__(self):
        return "Calories: " + str(self.calories) + " Total Calories: " + str(self.totalCalories)
           