from item import Item
from room import Room
from player import Player

direction_letter_name = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}
direction_letters = direction_letter_name.keys()

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    'torch': Item('tiki', 'A Hawaiian-looking torch'),
    'sword': Item('sword', 'A rusty sword'),
    'jewel': Item('emerald', 'A shiny green rock'),
    'nail': Item('nail', 'Just a nail'),
    'flask': Item('flask', 'A flask with a mysterious liquid'),
    'scroll': Item('scroll', 'A rolled up parchment'),
    'bag': Item('coinbag', 'A leather pouch of shiny doubloons')
}

# Assignments of items to rooms
item_room_setup = [
    ('outside', 'torch'),
    ('foyer', 'sword'),
    ('foyer', 'nail'),
    ('foyer', 'flask'),
    ('overlook', 'jewel'),
    ('narrow', 'flask'),
    ('narrow', 'scroll'),
    ('treasure', 'bag')
]

for pair in item_room_setup:
    my_room = room[pair[0]]
    my_item = item[pair[1]]
    my_room.add_item(my_item)

player_1 = Player(room['outside'])


def print_hints():
    print()
    print("move commands (single letter) n, e, s, or w")
    print("Or, 'get <thing>'', or 'drop <thing>'")
    print("To quit, q")
    print("Currently, lowercase only.")


def pick_up_thing(player, room, thing_name):
    thing = room.remove(thing_name)
    if thing:
        # print(thing)
        player.take(thing)


def drop_thing(player, room, thing_name):
    thing = player.drop(thing_name)
    if thing:
        # print(thing)
        room.add_item(thing)


def game_loop():
    while True:
        this_room = player_1.current_room
        this_room.describe()
        player_1.describe()

        commands = input('What shall we do?').split()
        command_count = len(commands)

        if command_count == 1:
            action = commands[0]
            if action == 'q':
                print("You did super! See you again, soon!")
                break

            elif action in direction_letters:
                if this_room.movement_is_possible(action):
                    print(f'We boldly go {direction_letter_name[action]}!')
                    player_1.move(action)
                else:
                    print(f'Stymied! There is no way to move {direction_letter_name[action]}!')
            else:
                print_hints()

        elif command_count == 2:
            if commands[0] == 'get':
                thing = commands[1]
                pick_up_thing(player_1, this_room, thing)
                print ("You get the " + commands[1])
            elif commands[0] == 'drop':
                drop_thing(player_1, this_room, thing)
                print ("You drop the " + commands[1])
            else:
                print_hints()

        else:
            print_hints()


def __main__():
    game_loop()
