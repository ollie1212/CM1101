player = {"name": "Ollie", "health": 100, "experience": 50, "mana": 70, "Alive": True, "inventory": []}
player["inventory"] = "Sword of Azeroth"
import random

def print_player(player):
    print("Player Stats:")
    for key in player:
        print(key + " is " + str(player[key]))
    


def compute_experience(damage):
    experience = random.randint(0,damage*2)
    return experience



def take_damage(player,damage):
    player["health"] = player["health"] - damage
    player["experience"] = player["experience"] + compute_experience(damage)
    if player["health"] == 0 or player["health"] < 0:
        player["Alive"] = False    
        
    return player    

while player["health"] > 0:
    
    take_damage(player, 50)
    print(print_player(player))

if player["health"] <= 0:
    print("you are dead")
