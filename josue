import random

# TODO : Create lists for the monsters, weapons, and targets.
monsters = ["goblin", "ghost", "dragon", "random"]
weapons = ["sword", "bow", "magic"]
targets = ["head", "body", "random"]
# TODO : Create a function that gives you the health of a monster. It should take in a monster as a parameter and return the amount of health it starts with.
def monster_health(monster):
	if monster == "goblin":
		monster_health = 10
	elif monster  == "ghost":
		monster_health = 15
	elif monster == "dragon":
		monster_health = 20
	return monster_health
# TODO : Create a function that calculates the amount of damage a player will do to a monster. Its parameters should be the monster, the weapon, and the target and it should return the amount of damage the player will do. You may create additional functions to break up the logic if you wish.
def monster_damage(monster, weapon, target):	
	if monster == "goblin":
		if weapon == "sword":
			if target == "head":
				player_damage = 5
			elif target == "body":
				player_damage = 3
			elif target == "random":
				player_damage = random.randint(0,5)
		elif weapon == "bow":
			if target == "head":
				player_damage = 3
			elif target == "body":
				player_damage == 5
			elif target == "random":
				player_damage = random.randint(0,5)
		elif weapon == "magic":
			if target == "head":
				player_damage = 1
			elif target == "body":
				player_damage = 1
			elif target == "random":
				player_damage = random.randint(0,5)
	if monster == "ghost":
		if weapon == "sword":
			if target == "head":
				player_damage = 3
			elif target == "body":
				player_damage = 5
			elif target == "random":
				player_damage = random.randint(0,5)
		elif weapon == "bow":
			if target == "head":
				player_damage = 1
			elif target == "body":
				player_damage == 1
			elif target == "random":
				player_damage = random.randint(0,5)
		elif weapon == "magic":
			if target == "head":
				player_damage = 5
			elif target == "body":
				player_damage = 3
			elif target == "random":
				player_damage = random.randint(0,5)
	if monster == "dragon":
		if weapon == "sword":
			if target == "head":
				player_damage = 1
			elif target == "body":
				player_damage = 1
			elif target == "random":
				player_damage = random.randint(0,5)
		elif weapon == "bow":
			if target == "head":
				player_damage = 3
			elif target == "body":
				player_damage == 5
			elif target == "random":
				player_damage = random.randint(0,5)
		elif weapon == "magic":
			if target == "head":
				player_damage = 5
			elif target == "body":
				player_damage = 3
			elif target == "random":
				player_damage = random.randint(0,5)
# TODO : Create a function that calculates the amount of damage a monster will do to the player. It should take in a monster as a parameter and return the amount of health it starts with.
def damage(monster):
	if monster == "goblin":
		player_healths = player_healths - random.randint(0,3)
	elif monster == "ghost":
        player_healths = player_healths - random.randint(0,5)
    elif monster == "dragon":
        player_healths = player_healths - random.randint(0,7)
def main():
    player_health = 10
    # TODO : Randomly pick which monster the player will face this game. Set the result equal to the variable 'monster'. """ 
    monster = random.choice(["goblin", "ghost", "dragon"])

    print "A " + str(monster) + " has appeared before you! It looks angry."

    choice = ["fight", "run"]
    while (choice is None):
        # TODO : Ask the player what they want to do. Their options are 'fight' and 'run'. Set the player's choice equal to the variable 'choice'.

        if choice not in ["fight", "run"]:
            print "I didn't understand that..."
            choice = None

    # TODO : Exit the program if the player chose to run away. Otherwise, wish them luck in their fight.
	if choice == "run":
		sys.quit()
    # TODO : Set the monster's starting health by calling your function
	monster_health(monster)
    # TODO : Set the player's starting health to 10
	
	print player_health
    # Turn iterator
    while monster_health > 0 and player_health > 0:
        weapon = None
        while (weapon is None):
            # TODO : Ask the player what weapon they will use to attack the monster. Their options are 'sword', 'bow', and 'magic'. Set the player's choice equal to the variable 'weapon'.
            if weapon not in weapons:
                print "I didn't understand that..."
                weapon = None

        # TODO : Randomly pick where the player will attack the monster. Set the result equal to the variable 'target'.

        # TODO : Set the amount of damage the player will deal to the monster by calling your function

        # TODO : Deal damage to the monster.

        # TODO : If the monster is still alive, set the amount of damage the monster will deal to the player by calling your function

        # TODO : Deal damage to the player.

        # TODO : Inform the player of their health and the monster's health at the end of every turn

    # TODO : Display either a game over or victory message once either the player or the monster has run out of health

main()
