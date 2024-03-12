class Stats():
    def __init__(self, coconutsInTrees=10, hungerLevel=0, thirstLevel=0,  coconutsSaved=0,  rocksAvailable=3, goats=1, savedMeat=0, daysSurvived=0, playGame = 'y'):
        self.coconutsInTrees = coconutsInTrees
        self.hungerLevel = hungerLevel
        self.thirstLevel = thirstLevel
        self.coconutsSaved = coconutsSaved
        self.rocksAvailable = rocksAvailable
        self.goats = goats
        self.savedMeat = savedMeat
        self.daysSurvived = daysSurvived 
        self.playGame = playGame

    def showStats(self):
        print("-------------- STATS ---------------------")
        print("Coconuts In Trees: ", self.coconutsInTrees)
        print("Hunger Level: ", self.hungerLevel)
        print("Thirst Level: ", self.thirstLevel)
        print("Coconuts Saved: ", self.coconutsSaved)
        print("Rocks Available: ", self.rocksAvailable)
        print("Goats: ", self.goats)
        print("Saved Meat: ", self.savedMeat)
        print("Survival Time", self.daysSurvived)
        print("------------------------------------------")

        self.daysSurvived += 1
        self.hungerLevel += 1
        self.thirstLevel += 1
      