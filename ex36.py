# TODO
# [X] Draw dungeon map
# [] Make function for each room
# [] Create traps
# [] Create riddles
# [] Create items
#   [] armor
#   [X] weapons
#   [] potions
# [] Create monsters
# [] Create fight system
# [] Find modules to import, like argv
#   [] from math import * -> floor(), ceil()
#   [] from random import * -> random()
# [] Create character with stats

# - room 1 (start room)
#     - room 2 (treasure)
#     - room 3 (monster blocking room 4)
#         - room 4 (room 6 locked, trap room)
#             - room 5 (key to room 6, treasure)
#             - room 6 (trap)
#                 - room 7 (monster blocking room 8)
#                     - room 8 (room 11 locked)
#                         - room 9  (monster holding key to room 11)
#                         - room 10 (trap, treasure)
#                         - room 11 (end-boss)


from math import *
from random import *
from datetime import *


prompt = "> "
inventory = []
giant_rat_alive = True
big_fat_goblin_alive = True
skeleton_warrior_alive = True
red_dragon_alive = True

giant_rat_attacks = ["bite", "tail strike", "body slam"]
big_fat_goblin_attacks = ["headbutt", "club strike", "kick"]
skeleton_warrior_attacks = ["sword strike", "shield blow", "punch"]
red_dragon_attacks = ["fire breath", "stomp", "fyling kick"]

health = 100
attack = 5
defense = 0


def monster_killed(monster):
    global giant_rat_alive
    global big_fat_goblin_alive
    global skeleton_warrior_alive
    global red_dragon_alive

    if monster == "giant rat":
        giant_rat_alive = False

    if monster == "big fat goblin":
        big_fat_goblin_alive = False

    if monster == "skeleton warrior":
        skeleton_warrior_alive = False

    if monster == "red dragon":
        red_dragon_alive = False


def go_to_room(num):
    if num == 3:
        room3()
    elif num == 4:
        room4()
    elif num == 7:
        room7()
    elif num == 8:
        room8()
    elif num == 9:
        room9()


def heal_self():
    global health
    health = 100


def remove_from_inventory(item):
    inventory.remove(item)


def add_to_inventory(item):
    inventory.append(item)


def monster_move(monster):
    if monster == "giant rat":
        return giant_rat_attacks[randrange(0, 3)]
    elif monster == "big fat goblin":
        return big_fat_goblin_attacks[randrange(0, 3)]
    elif monster == "skeleton warrior":
        return skeleton_warrior_attacks[randrange(0, 3)]
    elif monster == "red dragon":
        return red_dragon_attacks[randrange(0, 3)]
    else:
        return "roundhouse kick"


def fight(monster, monster_health, monster_attack, prev_room, next_room):
    global health

    if "sword" in inventory:
        attack = 20

    if "sword+" in inventory:
        attack = 40

    if "shield" in inventory:
        defense = 20

    if "armor" in inventory:
        defense = 40

    monster_damage = monster_attack - defense

    print(f"You have to fight a {monster}!")

    if "potion" in inventory:
        print("+ You can use a potion to heal yourself.")
    if "sword" in inventory or "sword+" in inventory:
        print(f"+ You can attack the {monster} with your weapon.")
    else:
        print(f"+ You can attack the {monster} with your fists.")

    if "shield" in inventory:
        print("+ You can block an attack with your shield.")

    print("+ Or you can flee from the fight.")

    while True:
        choice = input(prompt)

        if "potion" in choice or "heal" in choice:
            heal_self()
            print(f"You heal yoursel, your healthpoints are now at {health}")
            remove_from_inventory("potion")
            print(
                f"The {monster} uses {monster_move(monster)} and deals {monster_damage} damage")
            health -= monster_damage
            print(f"You have {health} health left.")
        elif "attack" in choice:
            print(f"You swing your sword and deal {attack} damage.")
            monster_health -= attack
            print(f"The {monster} has {monster_health} health left.")
            print(
                f"The {monster} uses {monster_move(monster)} and deals {monster_damage} damage")
            health -= monster_damage
            print(f"You have {health} health left.")
        elif "block" in choice:
            print("You use your shield to block the attack.")
            print(f"The {monster} deals 0 damage")
        elif "flee" in choice:
            print(f"You turn around and flee from the {monster}.")
            go_to_room(prev_room)
        else:
            print("I dont know what that means...")

        if monster_health <= 0:
            print(f"You defeated the {monster}")
            monster_killed(monster)
            go_to_room(next_room)


def start():
    print("You wake up with a terrible headache lying in a small dark room.")
    room1()


def room1():
    if not "sword" in inventory:
        print("Right next to you is a sword on the ground.")
        print("Maybe you should pick it up.")
    else:
        print("This is just a smelly dark little room.")
        print("You should move on.")

    print("To the north is a narrow path.")
    print("To the east is a wooden door.")

    while True:
        choice = input(prompt)

        if "sword" in choice and not "sword" in inventory:
            print("Nice! You are wielding an old rusty sword now.")
            add_to_inventory("sword")
        elif "north" in choice or "path" in choice:
            # north == room2
            room2()
        elif "door" in choice or "east" in choice:
            # east == room3
            print("You open the wooden door and enter the room.")
            room3()
        else:
            print("I dont know what that means...")


def room2():
    print("It looks like you found a knight's room!")

    if not "shield" in inventory:
        print("There is a shield and a red potion on a table.")
        print("Do you want to take it?")
    else:
        print("Nothing of use is left in this room.")

    print("To the south is a narrow path leading back.")

    while True:
        choice = input(prompt)

        if "yes" in choice or "take" in choice:
            add_to_inventory("shield")
            add_to_inventory("potion")
            print("You equip the new shield and put the potion in your backpack.")
        elif "south" in choice or "path" in choice:
            room1()
        else:
            print("I dont know what that means...")


def room3():
    print("To the west is a wooden door.")
    print("To the east is a bridge.")

    if giant_rat_alive == True:
        print("But wait... There is a giant rat blocking the bridge!")
        print("The only way to get to the other side is to fight this monster.")
    else:
        print("The dead rat is still on the bridge...")

    while True:
        choice = input(prompt)

        if "door" in choice or "west" in choice:
            print("You open the wooden door and enter the room.")
            room1()
        elif "bridge" in choice or "east" in choice and giant_rat_alive == False:
            print("You cross the bridge and see the dead rat still lying on the ground.")
            room4()
        elif "bridge" in choice or "east" in choice and giant_rat_alive == True:
            fight("giant rat", 60, 30, 3, 4)
        elif "fight" in choice or "attack" in choice:
            fight("giant rat", 60, 30, 3, 4)
        else:
            print("I dont know what that means...")


def room4():
    print("typ 'back' to go to previous room")
    choice = input(prompt)

    if choice == "back":
        room3()


def room5():
    print()


def room6():
    print()


def room7():
    print()


def room8():
    print()


def room9():
    print()


def room10():
    print()


def room11():
    print()


start()
