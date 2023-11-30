class Item(object):

    #Deafult contructor
    def __init__(self):
        self.name = ""
        self.cookTime = 0

    def __init__(self, inputName, inputTime):
        self.name = inputName
        self.cookTime = inputTime
    
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
