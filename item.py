class Item(object):

    #Deafult contructor
    def __init__(self):
        self.name = ""
        self.cookTime = 0
    
    #Setters
    def setName(self, name):
        self.name = name
    
    def setCookTime(self, time):
        self.cookTime = time

    #Getters
    def getName(self):
        return self.name
    
    def getCookTime(self):
        return self.cookTime
