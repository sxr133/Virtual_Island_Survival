class Island:
  
  def gameOver(stats):
    print("Sorry.. you DIED!")
    stats.playGame = "n"

  def useItems(stats):
    print(stats.coconutsSaved)
    print(stats.savedMeat)
    if(stats.coconutsSaved <= 0 and stats.savedMeat <= 0):
        print("It looks like you ran out of food and water...")
    
    if(stats.coconutsSaved > 0):
        stats.thirstLevel -= stats.coconutsSaved

    if(stats.thirstLevel < 0):
        stats.thirstLevel = 0;

    if(stats.savedMeat < 0):
        stats.hungerLevel = 0;
        stats.savedMeat = 0
        stats.coconutsSaved = 0