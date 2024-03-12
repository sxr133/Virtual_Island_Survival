from stats import Stats
from player import Player
from tree import Tree
from images.palm import palm

stats = Stats()
player = Player()
tree = Tree()
palm()

playGame = input("Welcome to Virtual Island Survival.  Get Started? (y/n):")

while(stats.playGame == 'y'):
    stats.showStats()
    decision1 = input("Do you want to pick up a rock (A) or shake the tree (B):")
    if (decision1 == "A"):
        player.pickUpRock(stats, tree)
    else:
        tree.shakeTree(stats)

    player.checkIfDead(stats)