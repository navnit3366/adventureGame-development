# All 'uncategorized' functions for the adventure game will be stored here
# Author: Martin A.
# Date: May 2022

import os
import random
import player as p
import enemies as e

def load_game():
    # This function will load the game
    print("Loading game...")

def save_game():
    # This function will save the game
    print("Saving game...")

def attack(enemy, weapon):
    # This function will return the damage done to an enemy
    print("You attack the with your " + weapon)
    damage = random.randint(1, 10)
    return damage

def loot(enemy):
    # This function will loot the enemy
    print("You loot the enemy")

def movement(direction):
    # This function will return the movement of the player
    if direction == "north":
        print("You move north")
    elif direction == "south":
        print("You move south")
    elif direction == "east":
        print("You move east")
    elif direction == "west":
        print("You move west")
    else:
        print("You can't move that way")
        
def fight(enemy):
    if p.health > 0: # ?????
        # This function will start the fight with the enemy
        print("You are fighting " + e.enemy["name"])

        # This will be the loop for the fight
        print("You have " + str(p.health) + " health")
        print("Enemy has " + str(e.enemy["health"]) + " health")
        print("You have " + str(p.weapon) + " weapon")
        print("You have " + str(p.armor) + " armor")
        print("You have " + str(p.gold) + " gold")
        print("You have " + str(p.inventory) + " inventory")
        print("You have " + str(p.level) + " level")
        print("You have " + str(p.exp) + " experience")
        print("You have " + str(p.exp_to_next_level) + " experience to next level")
    else:
        death() ## TODO ## Is this a semi good way to do this?

def level_up():
    # This function will level up the player
    print("You leveled up!")

def death():
    # This function will end the game
    print("You died")

def crafting():
    # This function will start the crafting
    print("You are crafting")

def clear():
    # This function will clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')