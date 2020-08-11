from room import Room
from player import Player
from item import Item

import random
import sys
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons. You see a rope lying on the ground at the mouth of the cave.", items = [Item(name = 'rope', description = "this looks like it may be able to support my weight")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. You see a sword leaned against the wall, and a map posted above it.""", items = [Item(name = 'sword', description = "a rusty one-handed sword"),
                                          Item(name = 'map', description = "this looks like a map of the cave")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items = [Item(name = 'pebble', description = 'the ground is covered with small, smooth pebbles')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, all you see is an old, empty treasure chest. The only exit is to the south.""", items = [Item(name = 'treasure chest', description = 'this is a treasure chest')])
}



# Randomly spawn items in rooms
# for x in room.values():
#     for i in random.sample(items.keys(), random.randint(0,3)):
#         x.items.append(items[i])

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

if __name__ == '__main__':

    p_name = input("Hello and welcome! Please enter your name:")
    player = Player(name=p_name, current_room=room['outside'])

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#


    while True:
        print("--" * 20)
        print("Location", player.current_room.name)
        print( player.current_room.description)
        
        player_input = input("What would you like to do?")
        player_input_first = player_input.split()[0]
        if player_input == "q":
            print("Exiting Game")
            sys.exit()
        if player_input == 'i' or player_input == 'inventory':
            print("Inventory:", [item.name for item in player.items])
            continue
        directional_commands = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
        item_commands = ['get', 'drop', 'i', 'inventory']
        try:
            player.current_room = getattr(player.current_room, directional_commands[player_input_first.lower()])
            continue
        except AttributeError:
            if player_input_first not in item_commands:
                print("Cannot go in that direction")
                continue
        except KeyError as e:
            if player_input_first not in item_commands:
                print("Invalid command!")
                continue
        except Exception as e:
            print(e)
        player_input_itemname = player_input.split()[1]
        p_item = None
        if player_input_first == 'get':
            for item in player.current_room.items:
                if item.name == player_input_itemname:
                    p_item = item
            if p_item is not None:
                player.items.append(p_item)
                p_item.on_take()
                player.current_room.remove_item(p_item)
        elif player_input_first == 'drop':
            for item in player.items:
                if item.name == player_input_itemname:
                    p_item = item
            if p_item is not None:
                player.items.remove(p_item)
                p_item.on_drop()
                player.current_room.add_item(p_item)