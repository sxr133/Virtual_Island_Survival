from player import Player

class Tree():
    
    def updateCoconuts(stats):
        stats.coconutsInTrees -= 1
        stats.coconutsSaved += 1

    def shakeTree(self, stats):
        stats.coconutsInTrees -= 1
        Player.updatePlayerStats(stats)
        print("You shook the tree, and a coconut fell on the ground! Congrats")

        decision2 = input("Open coconut with rock? (A) or save coconut for later? (B):")

        if(decision2 == "A"):
            self.openCoconut(stats)
        else:
            stats.coconutsSaved += 1
            print("You have used energy to shake the tree and open a coconut.")
            print("You are slightly more hungry, but you satisfied your thirst")

    def openCoconut(self, stats):
        stats.thirstLevel = 0
        stats.hungerLevel -= 1
        print("You have used energy to shake the tree and open a coconut.")
        print("You are slightly more hungry, but you satisfied your thirst")
