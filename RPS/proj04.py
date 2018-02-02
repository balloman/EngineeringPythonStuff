from random import randint
import sys

beat = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
moves = ["Rock", "Paper", "Scissors"]
playerchoices = []
games = [0, 0, 0, 0]
status = 0


def valuesPicked(lst):
    rock = lst.count(moves[0])
    paper = lst.count(moves[1])
    scissors = lst.count(moves[2])
    return "You chose rock %d time(s), paper %d time(s), and scissors %d time(s)" % (rock, paper, scissors)


def most_common(lst):
    return max(set(lst), key=lst.count)


def grabPlayer(fPlayerChoices, fStatus, fGames):
    print "Choose Rock, Paper, or Scissors"
    choice = raw_input(">>> ")
    if 'q' in choice.lower():
        print "After playing %d time(s). I won %d time(s), You won %d time(s), and we tied %d times" % (fGames[3], fGames[1], fGames[0], fGames[2])
        print valuesPicked(playerchoices)
        sys.exit(0)
    for i in moves:
        if choice.lower() in i.lower():
            fPlayerChoices.append(i)
            return i
    print "I didnt understand that..."


def bestMove(fPlayerChoices):
    try:
        return beat[most_common(fPlayerChoices)]
    except Exception:
        return moves[randint(0, 2)]


def gamePlay(calcChoice, playerChoice, fGames):
    print "I chose %s" % calcChoice
    if beat[calcChoice] == playerChoice:
        fGames[0] += 1
        return "You win..."
    elif beat[playerChoice] == calcChoice:
        fGames[1] += 1
        return "I win! Haha!"
    else:
        fGames[2] += 1
        return "Tie...:/"


def main(beat, moves, playerchoices, games, status):
    print gamePlay(bestMove(playerchoices), grabPlayer(playerchoices, status, games), games)


print "Hello, welcome to Rock, Paper Scissors."
while True:
    main(beat, moves, playerchoices, games, status)
    games[3] += 1


