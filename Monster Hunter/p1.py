from random import randint
from random import choice as rchoice
from time import sleep
import simplejson as json

class Character:
    """Class for the characters in the game"""
    def __init__(self, cname, chealth, cdamage, weapon_damage):
        self.health = chealth
        self.damage = cdamage
        self.name = cname
        self.weapon_damage = weapon_damage

    def damageToMonster(self, weapon):
        location = None
        head = 0
        body = 1
        seed = randint(1, 3)
        if seed == 1:
            location = head
        elif seed == 2:
            location = body
        else:
            location = 2
        if location != 2:
            locationstr = None
            if location == 0:
                locationstr = "in the head"
            elif location == 1:
                locationstr = "in the body"
            return [self.weapon_damage[weapon][location], locationstr]
        else:
            return [randint(0, 5), "a random area"]

    def damageToHero(self):
        return randint(self.damage[0], self.damage[1])

    
class Weapon:
    """Class that gives the weapons damage"""
    def __init__(self, cname, cdamage):
        self.name = cname
        self.damage = cdamage

monsterlist = [Character("Goblin", 10, (0,3), {"Sword" : (5, 3), "Bow" : (3, 5), "Magic" : (1, 1)}),
               Character("Ghost", 15, (0,5), {"Sword" : (3, 5), "Bow" : (1, 1), "Magic" : (5,3)}), 
               Character("Dragon", 20, (0,7), {"Sword" : (1,1), "Bow" : (3,5), "Magic" : (5,3)}),]

weapons = ["Bow", "Sword", "Magic"]
try:
    f = open('playerdata.mh', 'r+')
except IOError:
    f = open('playerdata.mh', 'w+')
    f = open('playerdata.mh', 'r+')
try:
    data = json.load(f)
except ValueError:
    data = {}

f = open('playerdata.mh', 'w+')
def loading():
    """Creates a loading string for the game"""
    for i in ('.', '.', '.'):
        sleep(0.5)
        print i,
        sleep(0.5)
    print ""

def main(fplayer):
    """The main program"""
    
    monster = rchoice(monsterlist)

    print "A " + monster.name + " has appeared before you! It looks angry."

    choice = None
    while choice is None:

        choice = raw_input("You can either fight or run. What do you do? >>> ")

        if choice not in ["fight", "run"]:
            print "I didn't understand that..."
            choice = None

    if 'u' in choice:
        exit()
    else:
        print "Good Luck %s." % fplayer.name
        sleep(2)

    # Turn iterator
    while monster.health > 0 and fplayer.health > 0:
        weapon = None
        while weapon is None:

            weapon = raw_input("Bow, Magic, or Sword? >>>")

            if weapon not in weapons:
                print "I didn't understand that..."
                weapon = None

        dth = monster.damageToHero()
        dtm = monster.damageToMonster(weapon)
        chance = randint(0, 100)
        if chance < 15:
            dtm[0] = float(dtm[0]) * 1.5
            dtm[0] = round(dtm)
            print "Critical Strike!"
        monster.health = monster.health - dtm[0]
        fplayer.health = fplayer.health - dth

        print "You blow hits the %s in %s." % (monster.name, dtm[1])
        print "You did %d damage to the monster." % dtm[0]

        if monster.health < 0:
            break
        else:
            sleep(0.5)
            print "You were unable to kill the monster, and it attacks you!"
            loading()
            print "The %s did %d damage to you." % (monster.name, dth)

        print "Your health is %d, and the monster's health is %d" % (fplayer.health, monster.health)
        sleep(1)

    if monster.health <= 0:
        loading()
        sleep(3)
        print "You Won!"
        try:
            data[fplayer.name] = data[fplayer.name] + 10
        except KeyError:
            data[fplayer.name] = 1

        json.dump(data, f)
    else:
        print "You Died!"

def xpReq(level):
    """Calculates the next level"""
    return round((4 * (level**3)) / 5)
    
player = Character(raw_input("What is your name warrior? >>>"), 10, None, None)
level = 0
i = 0
while True:
    
    try:
        if xpReq(i) < data[player.name]:
            print i
            print "Loop"
        else:
            level = i
            break
    except KeyError:
        print "KeyError"
        data[player.name] = 1
        i -= 1
    i += 1

monstercount = level
while level > 0:
    main(player)
    level -= 1
raw_input("Press enter to exit...")
