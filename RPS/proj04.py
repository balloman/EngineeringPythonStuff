import sys
from random import randint

# aDDED A COMMENT
beat = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
moves = ["Rock", "Paper", "Scissors"]
# Empty list that will soon hold all of the player choices
playerchoices = []
# A list that has all the gamedata in the format specified below
# [Number of times human has won, number of times pc has won, number of ties, number of games]
games = [0, 0, 0, 0]


def listHistory(fGames):
    print "After playing %d time(s). I won %d time(s), You won %d time(s), and we tied %d times" % (
          fGames[3], fGames[1], fGames[0], fGames[2])
    print valuesPicked(playerchoices)

    
def valuesPicked(lst):
    """Returns the gamedata at the end of the game by counting the occurence of each move in the list of moves"""
    return "You chose rock %d time(s), paper %d time(s), and scissors %d time(s)" % (lst.count(moves[0]), lst.count(moves[1]), lst.count(moves[2])

                                                                                     
def most_common(lst):
    """Function I found on the internet to return the most common element in a list"""
    return max(set(lst), key=lst.count)

                                                                                     
def grabPlayer(fPlayerChoices, fGames):
    """Gets the player's decision and returns what they chose. Also handles quit"""
    choice = None
    while choice == None:
      print "Choose Rock, Paper, or Scissors"
      choice = raw_input(">>> ")
      if 'q' in choice.lower():
          # Multiline statement that prints quit info
          print "After playing %d time(s). I won %d time(s), You won %d time(s), and we tied %d times" % (
              fGames[3], fGames[1], fGames[0], fGames[2])
          print valuesPicked(playerchoices)
          sys.exit(0)
      elif choice.lower() in 'history':
          listHistory(fGames)
          choice = None
          continue
          
      for i in moves:
          if choice.lower() in i.lower():
              # Adds player choice to list of choices for move calculation
              fPlayerChoices.append(i)
              return i
      print "I didnt understand that..."
      choice = None

                                                                                     
def bestMove(fPlayerChoices):
    """Calculates the best move based on the most common user choices"""
    ''' try except case is because the most_common function fails if there are multiple common values 
        This ensures that if the function fails, we can catch the exception without breaking the code and fall back
        on a random move
    '''
    try:
        return beat[most_common(fPlayerChoices)]
    except Exception:
        return moves[randint(0, 2)]

                                                                                     
def gamePlay(calcChoice, playerChoice, fGames):
    """Handles the output of the game once calculated"""
    print "I chose %s" % calcChoice
    if beat[calcChoice] == playerChoice:
        # Adds to the counter for human wins
        fGames[0] += 1
        return "You win..."
    elif beat[playerChoice] == calcChoice:
        # Adds to the counter for pc wins
        fGames[1] += 1
        return "I win! Haha!"
    else:
        # Adds to the counter for ties
        fGames[2] += 1
        return "Tie...:/"

                                                                                     
def main(beat, moves, playerchoices, games):
    """Throw the thing in main so that I can run it multiple times"""
    print gamePlay(bestMove(playerchoices), grabPlayer(playerchoices, games), games)

                                                                                     
print "Hello, welcome to Rock, Paper Scissors."
while True:
    # Proceed to run it multiple times
    main(beat, moves, playerchoices, games)
    games[3] += 1
