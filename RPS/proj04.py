from random import randint

beat = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
moves = ["Rock", "Paper", "Scissors"]
playerchoices = []


def most_common(lst):
    return max(set(lst), key=lst.count)


def grabPlayer(fPlayerChoices):
    print "Choose Rock, Paper, or Scissors"
    choice = raw_input(">>> ")
    for i in moves:
        if choice.lower in i.lower():
            fPlayerChoices.append(i)
            return i
    print "I didnt understand that..."


def bestMove(fPlayerChoices):
    try:
        return most_common(fPlayerChoices)
    except Exception:
        return moves[randint(1, 3)]


def gamePlay(calcChoice, playerChoice):
    print "I chose %s" % calcChoice
    if beat[calcChoice] == playerChoice:
        return "You win..."
    elif beat[playerChoice] == calcChoice:
        return "I win! Haha!"
    else:
        return "Tie...:/"


print "Hello, welcome to Rock, Paper Scissors."
print gamePlay(bestMove(playerchoices), grabPlayer(playerchoices))

