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

trap_room4 = True
trap_room6 = True

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


def dead():
    print("Game over!  Good luck next time.")
    print("-" * 32)
    print()
    start()


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

            if health <= 0:
                dead()

            print(f"You have {health} health left.")

        elif "attack" in choice:
            print(f"You swing your sword and deal {attack} damage.")

            monster_health -= attack

            if monster_health <= 0:
                print(f"You defeated the {monster}")
                print()
                monster_killed(monster)
                go_to_room(next_room)

            print(f"The {monster} has {monster_health} health left.")
            print(
                f"The {monster} uses {monster_move(monster)} and deals {monster_damage} damage")

            health -= monster_damage

            if health <= 0:
                dead()

            print(f"You have {health} health left.")
        elif "block" in choice:
            print("You use your shield to block the attack.")
            print(f"The {monster} deals 0 damage")
        elif "flee" in choice:
            print(f"You turn around and flee from the {monster}.")
            go_to_room(prev_room)
        else:
            print("I dont know what that means...")


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
    global giant_rat_alive

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
    global trap_room4
    global health

    print("You enter a room with a big tree in the middle and light rays shimmering through a hole in the ceiling.")
    print("To the west is a bridge.")
    print("To the north is a wooden door.")

    if trap_room4 == True:
        print("To the east is a ladder.")
    else:
        print("To the east is a broken ladder.")

    if "iron key" in inventory:
        print("To the south is an iron door with a lock.")
    else:
        print("To the south is an iron door.")

    while True:
        choice = input(prompt)

        if "west" in choice or "bridge" in choice:
            room3()
        elif "north" in choice or "wooden door" in choice:
            room5()
        elif "east" in choice or "ladder" in choice:
            if trap_room4 == True:
                print("You attempt to climb the ladder but the ladder breaks.")
                print(
                    "You fall backwards to the ground, hit your head and loose 20 healthpoints.")
                health -= 20

                if health <= 0:
                    dead()

                print(f"You have {health} healthpoints.")
                trap_room4 = False
            else:
                print("The ladder is broken.")
        elif "south" in choice or "iron door" in choice:
            if "iron key" in inventory:
                room6()
            else:
                print("The iron door is locked, go find the key.")
        else:
            print("I dont know what that means...")


def room5():
    print("You enter the room and you look around.")
    print("There are shelfs with books and other stuff in this room.")

    if not "armor" in inventory:
        print("And in the corner is an armor.")

    if not "potion" in inventory:
        print("Next to some books you see a red potion.")

    print("To the south is a wooden door.")

    while True:
        choice = input(prompt)

        if "armor" in choice and not "armor" in inventory:
            print("You take the armor and put it on.")
            print("Lucky you, it fits perfectly.")
            add_to_inventory("armor")
        elif "potion" in choice and not "potion" in inventory:
            print("You take the potion.")
            add_to_inventory("potion")
        elif "shelf" in choice or "key" in choice and not "iron key" in inventory:
            print("Wow! You found an iron key.")
            add_to_inventory("iron key")
        elif "south" in choice or "door" in choice:
            room4()
        else:
            print("I dont know what that means...")


def room6():
    global health
    global trap_room6

    print("You enter a pretty dark room.")
    print("The only light source comes through that hole in the wall.")
    print("In a corner you can see a lever.")
    print("To the north is an iron door.")
    print("To the east is a hole.")

    while True:
        choice = input(prompt)

        if "north" in choice or "door" in choice:
            room4()
        elif "east" in choice or "hole" in choice:
            room7()
        elif "lever" in choice:
            if trap_room6 == True:
                print("A rock falls from the ceiling and hits your head.")
                health -= 10
                trap_room6 = False
                print(f"That hurts... You have {health} healthpoints left.")
            else:
                print("Nothing happens.")
        else:
            print("I dont know what that means...")


def room7():
    global big_fat_goblin_alive

    if big_fat_goblin_alive == True:
        print("You squeeze yourself through that hole and see a big fat goblin holding a torch.")
        fight("big fat goblin", 80, 50, 6, 8)
    else:
        print("This room is empty except for that dead fat goblin.")

    print("To the west is a hole in the wall.")
    print("To the east is a wooden door.")

    while True:
        choice = input(prompt)

        if "west" in choice or "hole" in choice:
            room6()
        elif "east" in choice or "door" in choice:
            room8()
        else:
            print("I dont know what that means...")


def room8():
    print("You enter a room with a bunch of torches on the walls.")
    print("To the west is a wooden door.")
    print("To the north is an iron door with a skull on it.")
    print("To the east is a narrow path.")
    print("To the south is a ladder.")

    while True:
        chocie = input(prompt)

        if "west" in choice or "wooden door" in choice:
            room7()
        elif "north" in choice or "iron door" in choice:
            if not "golden key" in inventory:
                print("The door is locked you need a key.")
            else:
                room11()
        elif "east" in choice or "path" in choice:
            room9()
        elif "south" in choice or "ladder" in choice:
            print("You climb the ladder succesfully.")
            room10()
        else:
            print("I dont know what that means...")


def room9():
    global skeleton_warrior_alive

    if skeleton_warrior_alive == True:
        print("You take the narrow path and enter a room and a skeleton suddenly attacks you! ")
        fight("skeleton warrior", 100, 55, 8, 8)

        add_to_inventory("golden key")

        print("The skeleton dropped a shiny golden key.")
        print("You take the key and return to the previous room.")
    else:
        print("You take the narrow path and enter the room.")
        print("There is only a couple of bones on the floor nothing and nothing else.")

    print("To the west is a narrow path.")

    while True:
        choice = input(prompt)

        if "west" in choice or "path" in choice:
            room8()
        else:
            print("I dont know what that means...")


def room10():
    print("You see a blacksmith sitting alone in the corner.")

    if "sword+" in inventory:
        print("Blacksmith: Hi young adventurer, would you like me to repair your sword?")

        choice = input(prompt)

        if "yes" in choice or "repair" in choice:
            print(
                "The blacksmith takes your sword and his hammer and starts working...")
            print("He gives you back your fixed sword, damn looks good.")
            print("Blacksmith: Take this potion too, you might need it soon.")

            add_to_inventory("potion")
            add_to_inventory("sword+")
        elif "no" in choice:
            print("Totally up to you my friend.")
        else:
            pass

        print("To the north is a ladder.")

        while True:
            choice = input(prompt)

            if "north" in choice or "ladder" in choice:
                room8()
            elif "repair" in choice or "blacksmith" in choice:
                print("Looks like he is ignoring you...")
            else:
                print("I dont know what that means...")


def room11():
    print("room 11")

    print("You use the golden key to open this creepy looking door.")
    print("You are pushing the door really hard to open it.")
    print("A deep voice in this dark room: Who dares to disturb my sleep?")
    print("Flames light up the room and you see a really really really big red dragon!")

    while True:
        choice = input(prompt)

        if "fight" in choice or "attack" in choice or "hit" in choice:
            fight("red dragon", 170, 65, 8, 12)
            room12()
        elif "sing" in choice or "lullaby" in choice:
            print("You start singing for the dragon.")
            print("The dragon's eyes become heavy and he falls back to a deep sleep.")
            print("Crazy but this really worked.")

            room12()
        else:
            print("I dont know what that means...")


def room12():
    print("You see another door behind the dragon.")
    print("You open the door and you found the dragon's treasures!")
    print("It's a huge room full of gold, gems and other fancy looking medieval stuff.")
    print("Yay! Victory!!!")


start()
