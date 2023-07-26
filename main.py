# Import libraries
import functions as f
import player as p
import locations as l
import enemies as e

# Variables

f.clear()
print("Welcome to adventurers world!")
p.get_player_name()

print("Hi " + p.player["name"] + "!\n") ### WORKING ###
p.get_player_age()

f.clear()
print("Very nice, welcome to the Hung Forest!")

# print("You are " + str(p.player["age"]) + " years old") ### WORKING ###