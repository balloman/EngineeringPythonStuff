from random import randint
from time import sleep

class Character:
    def __init__(self, cname, chealth, cdamage, weapon_damage):
        self.health = chealth
        self.damage = cdamage
        self.name = cname
        self.weapon_damage = weapon_damage
    def damagecalc(self, cdamage):
        return randint(self.damage[0], self.damage[1])

class Weapon:

    def __init__(self, cname, cdamage):
        self.name = cname
        self.damage = cdamage
        

monsterlist = [Character("Goblin", 10, (0,3), {"Sword" : (5, 3), "Bow" : (3, 5), "Magic" : (1, 1)}),
               Character("Ghost", 15, (0,5), {"Sword" : (3, 5), "Bow" : (1, 1), "Magic" : (5,3)}), 
               Character("Dragon", 20, (0,7), {"Sword" : (1,1), "Bow" : (3,5), "Magic" : (5,3)}), 
               Character("Player", 10, (0,1))]

weapons = ["Bow", "Sword", "Magic"]

""" TODO : Create a function that calculates the amount of damage a player will do to a monster. Its parameters should be the monster, the weapon, 
 and the target and it should return the amount of damage the player will do. You may create additional functions to break up the logic if you wish."""

def damagecalc(weapon, location):
    


# TODO : Create a function that calculates the amount of damage a monster will do to the player. It should take in a monster as a parameter and return the amount of health it starts with.

def main():
    # TODO : Randomly pick which monster the player will face this game. Set the result equal to the variable 'monster'.
    monster = monsterlist[randint(0,2)]

    print "A " + monster.name + " has appeared before you! It looks angry."

    choice = None
    while (choice is None):

        choice = raw_input("You can either fight or run. What do you do? >>> ")

        if choice not in ["fight", "run"]:
            print "I didn't understand that..."
            choice = None

    if 'u' in choice:
        exit()
    else:
        print ("Good Luck")
        sleep(2)

    player = monsterlist[3]

    # Turn iterator
    while monster.health > 0 and player.health > 0:
        weapon = None
        while (weapon is None):

            weapon = raw_input("Bow, Magic, or Sword? >>>")
            
            if weapon not in weapons:
                print "I didn't understand that..."
                weapon = None

        location = randint(1, 3)

        # TODO : Set the amount of damage the player will deal to the monster by calling your function

        # TODO : Deal damage to the monster.

        # TODO : If the monster is still alive, set the amount of damage the monster will deal to the player by calling your function

        # TODO : Deal damage to the player.

        # TODO : Inform the player of their health and the monster's health at the end of every turn

    # TODO : Display either a game over or victory message once either the player or the monster has run out of health

main()
