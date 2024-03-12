from island import Island
from goat import Goat

class Player():
    def pickUpRock(self, stats, Tree):

        print("you have picked up a rock")
        
        stats.rocksAvailable -= 1

        decision2 = input("Throw rock at goat (A)? or Throw rock at coconut (B)?: ")

        if (decision2 == "A"):
            if(stats.goats <= 0):
                if(stats.coconutsInTrees <= 0 ):
                    print("sorry... no more goats... and no more coconuts...")
                else:
                    print("sorry... no more goats...")
                    self.throwRockAtCoconut(stats, Tree)
            else:    
                self.throwRockAtGoat(stats)
        else:
            if(stats.coconutsInTrees >= 0):
                self.throwRockAtCoconut(stats, Tree)
            else:
                print("sorry there's no more coconuts...")
            
                if(stats.goats <= 0):
                    print("sorry there's no more goats... you can't throw a rock at anything...")
                else:
                    self.throwRockAtGoat(stats)

    def throwRockAtGoat(self, stats):
        Goat.updateGoat(stats)
        stats.hungerLevel += 1

        decision3 = input("Eat meat (A)? or Save meat (B)?")

        if(decision3 == "A"):
            stats.hungerLevel = 0
            print("Hey... your not hungry anymore :)")
        else:
            print(stats.savedMeat)
            stats.savedMeat += 1
            print(stats.savedMeat)
            print("You have saved your meat :)")

    def throwRockAtCoconut(self, stats, Tree):
        Tree.updateCoconuts(stats)
        stats.hungerLevel += 1
        stats.thirstLevel += 1

        print("you threw the rock at the coconut...")
        print("You have 1 more coconut... and 1 less rock")

    def checkIfDead(self, stats):
        Island.useItems(stats)

        if(stats.hungerLevel >= 5 or stats.thirstLevel >= 3):
            Island.gameOver(stats)
    
    def updatePlayerStats(stats):
        stats.thirstLevel += 1
        stats.hungerLevel += 1