player = {
    "name": "", # TODO ## Ask Mikkul about putting the input("Type your name: ") in the player dictionary
    "age": "",
    "health": 100,
    "weapon": "fist",
    "armor": "none",
    "gold": 0,
    "inventory": [],
    "level": 1,
    "exp": 0,
    "exp_to_next_level": 100,
    "location": 0,
    "crit_chance": 0,
    "crit_damage": 0,
    "dodge_chance": 0,
    "dodge_damage": 0,
    "block_chance": 0,
    "block_damage": 0,
    "damage_reduction": 0,
    "speed": 1,
}

def get_player_name():
    # This function will get the player's name and return it
    newName = input("Type your character's name: ")
    player.update({'name': newName}) 
    return player["name"]

def get_player_age():
    # This function will get the player's age and return it
    try:
        newAge = int(input("Type your character's age: "))
        player.update({'age': newAge})
        return player["age"]
    except ValueError:
        print("That's not a number!")
        get_player_age()