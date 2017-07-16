#!/bin/python
def main():

  import argparse, random

  #the following section allows users to include command line arguments to set the number of players and the number of turns.
  #an example would be to run the following on the command line
  #python MonoPyly.py -p 3 -t 10
  #this would run the simulation with 3 players and 10 turns. The default is 4 players and 10 turns
  # if you try to use more than 10 players you'll get an error which I did not attempt to handle.
  # the list PlayerPosition holds the board position of each player and the maximum number of players is determined by its size

  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('-p', '--players', default=4, type=int, help='the number of players to be included in the game simulation')
  parser.add_argument('-t', '--turns', default=10, type=int, help='the number of turns each player will take')
  parser.add_argument('-g', '--games', default=1, type=int, help='the number of games the sim will run through')
  args = parser.parse_args()

  #most of these functions are just place holders for now. They will be implemented later

  #def move_passGo(spaces,square):
    #if move is in space increments (3 forward 3 back etc.) it will be stored as a positive (forward) or negative (back) int in $spaces
    #if move is to a specific square on the board, $spaces should be 0 and the square number will be specified in $square
    #the players current board square should be checked to determine if go is passed and if so the player should be given \$200.
    #newboardsquare=0
    #return newboardsquare

  #def move_dontpassGo(spaces,square):
    #if move is in space increments (3 forward 3 back etc.) it will be stored as a positive (forward) or negative (back) int in $spaces
    #if move is to a specific square on the board, $spaces should be 0 and the square number will be specified in $square
    #newboardsquare=0
    #return newboardsquare

  #def injail():
    #3 turns
    #turnsremaining=0
    #return turnsremaining

  #def moneymod(dollars):
    #$dollars should be specified as a positive (given money) or negative (pay money) integer
    #playerfunds=0
    #return playerfunds

  #def incometax(dollars):
    #calculate income tax based on the number of $dollars the player has
    #taxamount=0
    #print ("income tax assessed")
    #return taxamount

  #def luxurytax(dollars):
    #calculate luxury tax based on the number of $dollars the player has
    #taxamount=0
    #print ("luxury tax assessed")
    #return taxamount

  #def repairs(houses,hotels):
    #determine dollar amount cost of repairs for houses and hotels
    #repaircost=0
    #return repaircost

  def chance():
    #choose a chance card
    chancecard=0
    print("a chance card has been drawn")
    return chancecard

  def communitychest():
    #choose a community chest card
    comchestcard=0
    print("a community chest card has been drawn")
    return comchestcard

  def SpecialAction(space,dollars,houses,hotels):
    if space in [2,17,33]:
      ActionRequired="Community Chest"
      communitychest()
    elif space == 4:
      ActionRequired="Income Tax"
    elif space in [7,22,36]:
      ActionRequired="Chance"
      chance()
    elif space == 30:
      ActionRequired="Go to Jail"
    elif space == 38:
      ActionRequired="Luxury Tax"
    else:
      ActionRequired="none"

  #create a list of the name of each space on the Monopoly board
  Property=[
  "Go",
  "Mediterranean Avenue",
  "Community Chest 1",
  "Baltic Avenue",
  "Income Tax",
  "Reading Railroad",
  "Oriental Avenue",
  "Chance 1",
  "Vermont Avenue",
  "Connecticut Avenue",
  "Jail",
  "St. Charles Place",
  "Electric Company",
  "States Avenue",
  "Virginia Avenue",
  "Pennsylvania Railroad",
  "St. James Place",
  "Community Chest 2",
  "Tennessee Avenue",
  "New York Avenue",
  "Free Parking",
  "Kentucky Avenue",
  "Chance 2",
  "Indiana Avenue",
  "Illinois Avenue",
  "B.O. Railroad",
  "Atlantic Avenue",
  "Ventnor Avenue",
  "Water Works",
  "Marvin Gardens",
  "Go To Jail",
  "Pacific Avenue",
  "North Carolina Avenue",
  "Community Chest 3",
  "Pennsylvania Ave",
  "Short Line Railroad",
  "Chance 3",
  "Park Place",
  "Luxury Tax",
  "Boardwalk" ]

  #is the property player ownable? 0 for no, 1 for yes
  PropertyOwnable=[0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1]

  #dollar cost of the property
  PropertyCost=[0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]

  #cost of rent with no house
  RentNoHouse=[0,2,0,4,0,0,6,0,6,8,0,10,0,10,12,0,14,0,14,16,0,18,0,18,20,0,22,22,0,24,0,26,26,0,28,0,0,35,0,50]

  #cost of rent with one house
  #RentOneHouse=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #cost of rent with two houses
  #RentTwoHouse=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #cost of rent with three houses
  #RentThreeHouse=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #cost of rent with four houses
  #RentFourHouse=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #cost of rent with Hotel
  #RentHotel=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #cost of each house
  #HouseCost=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #cost of each hotel
  #HotelCost=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #value of mortgage
  #Mortgage=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #global counter that tracks the number of times any player lands on each square (for end game statistical purposes)
  SpaceHitCounter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #chance card deck
  ChanceCards=[
  "Advance to Go (Collect $200)",
  "Advance to Illinois Ave. - If you pass Go, collect $200",
  "Advance to St. Charles Place – If you pass Go, collect $200",
  "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.",
  "Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.",
  "Bank pays you dividend of $50",
  "Get out of jail free",
  "Go back three spaces",
  "Go to jail - go directly to jail - do not pass Go, do not collect $200"
  ]


  #set initial values for other variables
  #this is the inital value of the current game
  GameNumber=0

  #this is the number of players, set with a command line option
  Players=args.players

  #this is the number of turns per game to be played set with a command line option
  Turns=args.turns

  #this is the number of games to be played set with a command line option
  Games=args.games

  #create a loop that will run constantly until the specified number of games has been reached
  while (GameNumber < Games):
    print("#######################################################")
    print("starting game # {0}".format(GameNumber))
    print("#######################################################")
    #reset the number of the current turn to zero at the start of each game
    TurnNumber=0

    #reset the number of the player whose turn it is at the start of each game
    PlayerTurn=0

    #single game space hit counter reset to zero at the start of each new game
    GameSpaceHitCounter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #this list tracks the player position on the board
    PlayerPosition=[0,0,0,0,0,0,0,0,0,0]

    #this list tracks which players are currently in jail, 0 for not in jail, 1 for in jail
    PlayerInJail=[0,0,0,0,0,0,0,0,0,0]

    #this list tracks which players have a get out of jail free card. 0 for does not possess card, 1 for does possess a card
    PlayerGetOutOfJailFree=[0,0,0,0,0,0,0,0,0,0]

    #this list tracks the amount of money in the possession of each player
    PlayerFunds=[1500,1500,1500,1500,1500,1500,1500,1500,1500,1500]

    #this list tracks the property number of the properties still owned by the bank (unowned by a player)
    BankProperties=[1,3,5,6,8,9,11,12,13,14,15,16,18,19,21,23,24,25,26,27,28,29,31,32,34,35,37,39]

    #this list tracks the property numbers of the properties owned by each player
    PlayerProperties=[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]

    #create a loop that will run constantly until the specified number of turns has been reached
    #at the start of each iteration, print the turn number
    #at the end of each iteration, increment the turn number
    #at the end of each iteration, reset PlayerTurn to zero so that the next iteration begins with player 0
    while (TurnNumber < Turns):
      print("\nTurn# {0}".format(TurnNumber))
      #create a loop to handle each player's turn within the current round.
      while (PlayerTurn < Players):
        #print information about the players status at the beginning of the turn
        print("Player {0} occupies {1} at the start of turn {2}".format(PlayerTurn, Property[PlayerPosition[PlayerTurn]], TurnNumber))
        print("Player {0} has ${1} at the start of turn {2}".format(PlayerTurn, PlayerFunds[PlayerTurn], TurnNumber))
        #roll two dice and sum them
        Die1=random.randint(1,6)
        Die2=random.randint(1,6)
        Spaces=Die1+Die2
        #display the outcome of the roll
        print("Player {0} rolled {1}".format(PlayerTurn, Spaces))
        #add the number of spaces indicated by the roll to the players position in PlayerPosition
        PlayerPosition[PlayerTurn]=PlayerPosition[PlayerTurn]+Spaces
        #when a player reaches the end of the board, reset their position to 0 (pass go) and add $200 to their funds
        if (PlayerPosition[PlayerTurn] > 39):
          PlayerPosition[PlayerTurn]=PlayerPosition[PlayerTurn] - 40
          PlayerFunds[PlayerTurn]=PlayerFunds[PlayerTurn]+200
          print("Player {0} has passed go and collected $200".format(PlayerTurn))
        #print information about the players status at the end of the turn
        #print("Player {0} occupies space#{1}".format(PlayerTurn, PlayerPosition[PlayerTurn]))
        print("Player {0} now occupies {1}".format(PlayerTurn, Property[PlayerPosition[PlayerTurn]]))
        #after the player lands on a space, increment the total and game hit counters by one.
        GameSpaceHitCounter[PlayerPosition[PlayerTurn]]=GameSpaceHitCounter[PlayerPosition[PlayerTurn]]+1
        SpaceHitCounter[PlayerPosition[PlayerTurn]]=SpaceHitCounter[PlayerPosition[PlayerTurn]]+1
        if PropertyOwnable[PlayerPosition[PlayerTurn]] == 0:
            print("{0} is not an ownable property".format(Property[PlayerPosition[PlayerTurn]]))
            #because this is not an ownable property special action is required
            SpecialAction(PlayerPosition[PlayerTurn],PlayerFunds[PlayerTurn],0,0)
        else:
            print("{0} is an ownable property".format(Property[PlayerPosition[PlayerTurn]]))
            print("{0} costs ${1}".format(Property[PlayerPosition[PlayerTurn]], PropertyCost[PlayerPosition[PlayerTurn]]))
        print("Player {0} has ${1} at the end of turn {2}".format(PlayerTurn, PlayerFunds[PlayerTurn], TurnNumber))
        print("\n")
        #increment PlayerTurn to allow the next player to go
        PlayerTurn = PlayerTurn +1
      TurnNumber = TurnNumber +1
      PlayerTurn = 0
    #print final statistics about the game
    GameTotalSpaces=sum(GameSpaceHitCounter)
    print("after {0} turns in game {1}, {2} players landed on {3} spaces.".format(Turns, GameNumber, Players, GameTotalSpaces))
    print("space name, # times space was hit, percentage of all hits")
    for space in range(0,40):
      GameSpaceHitPercent=((GameSpaceHitCounter[space]/GameTotalSpaces)*100)
      print("{0}, {1}, {2}%".format(Property[space],GameSpaceHitCounter[space],GameSpaceHitPercent))
    print(GameSpaceHitCounter)
    GameNumber = GameNumber +1
  #print final statistics about the set of games
  TotalSpaces=sum(SpaceHitCounter)

  print(SpaceHitCounter)
  print("{0} games of {1} turns were played with {2} players each. {3} spaces were landed on across all games".format(Games, Turns, Players, TotalSpaces))
  print("space name, # times space was hit, percentage of all hits")
  for space in range(0,40):
    SpaceHitPercent=((SpaceHitCounter[space]/TotalSpaces)*100)
    print("{0}, {1}, {2}%".format(Property[space],SpaceHitCounter[space],SpaceHitPercent))

if __name__ == "__main__":
    main()
