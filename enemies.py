import random

# list of enemies
enemylist = ["goblin", "orc", "troll", "elf", "human", "dog", "dragon", "dwarf", "treeants", "kobold", "skeleton", "zombie", "wizard", "warlock", "gnome"]

# Enemy functions
def enemy_generator():
    # This function will generate an enemy
    enemy = random.choice(enemylist)
    return enemy

# # Example enemy
# enemy = {
#     "name": "Goblin",
#     "health": 100,
#     "weapon": "fist",
#     "armor": "none",
#     "gold": 0,
#     "inventory": [],
#     "level": 1,
# }