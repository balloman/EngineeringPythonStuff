from random import randint
from random import choice as rchoice
from time import sleep

class Character:
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
            return self.weapon_damage[weapon][location]
        else:
            return randint(0, 5)

    def damageToHero(self):
        return randint(self.damage[0], self.damage[1])

    
class Weapon:

    def __init__(self, cname, cdamage):
        self.name = cname
        self.damage = cdamage
        

monsterlist = [Character("Goblin", 10, (0,3), {"Sword" : (5, 3), "Bow" : (3, 5), "Magic" : (1, 1)}),
               Character("Ghost", 15, (0,5), {"Sword" : (3, 5), "Bow" : (1, 1), "Magic" : (5,3)}), 
               Character("Dragon", 20, (0,7), {"Sword" : (1,1), "Bow" : (3,5), "Magic" : (5,3)}),]

weapons = ["Bow", "Sword", "Magic"]


def main():
    """The main program"""
    player = Character(raw_input("What is your name warrior? >>>"), 10, None, None)
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
        print "Good Luck"
        sleep(2)

    player = monsterlist[3]

    # Turn iterator
    while monster.health > 0 and player.health > 0:
        weapon = None
        while weapon is None:

            weapon = raw_input("Bow, Magic, or Sword? >>>")

            if weapon not in weapons:
                print "I didn't understand that..."
                weapon = None

        monster.health = monster.health - monster.damageToMonster(weapon)

        player.health = player.health - monster.damageToHero()


        # TODO : Inform the player of their health and the monster's health at the end of every turn
        print "Your health is %d, and the monster's health is %d" % (player.health, monster.health)

    if player.health > 0:
        print "You Won!"
    else:
        print "You Died!"

main()
