"""
File: item.py
Item class and all relevant methods
"""
class Item(object):

    # Deafult contructor
    def __init__(self):
        self.name = ""
        self.cost = 0.0
        self.cookTime = 0

    def __init__(self, inputName, inputTime, inputCost):
        self.name = inputName
        self.cookTime = inputTime
        self.cost = inputCost

    # Setters
    def setName(self, name):
        self.name = name

    def setCookTime(self, time):
        self.cookTime = time

    def setCost(self, cost):
        self.cost = cost

    # Getters
    def getName(self):
        return self.name

    def getCookTime(self):
        return self.cookTime

    def getCost(self):
        return self.cost

    # Override toString, to allow printing
    def __str__(self):
        """Returns the string representation of the queue."""
        return "%s" % self.name
