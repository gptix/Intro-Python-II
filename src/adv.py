from room import Room
from player import Player

# Declare all the rooms
# This is a dictionary, with keys being room names, and values 
#~ being Room objects, which are created when this block is executed.
room = {
    'outside':  Room("outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

valid_directions = ['n', 's', 'e', 'w']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_1 = Player()
# instance is initialized with location outside.


# Write a loop that:
# Main game loop
while True:
    # * Prints the current room name
    print(f'{player_1.name}, you are currently in the room named \'{player_1.current_room}\'')

    # * Prints the current description (the textwrap module might be useful here).
    print(room.get(player_1.current_room).description)

    # * Waits for user input
    command = input('What shall we do? ').split()[0]

    # and decides what to do.
    # If the user enters "q", quit the game.
    if command == 'q':
        print("You were splendid! We shall adventure again soon!")
        break

    # If the user enters a cardinal direction, attempt to move to the room there.
    elif command in valid_directions:
        print(f'So, you\'d like to go {command}, eh?')

        # check_whether_move_is_possible
        movement_attribute = command + '_to'
        if getattr(room.get(player_1.current_room), movement_attribute) is None:
        # Print an error message if the movement isn't allowed.
            print(f'It is impossible to go that direction from here.\n')

        else:
            print(f'Very Well!  To the {command}!\n')
            player_1.current_room = getattr(room.get(player_1.current_room), movement_attribute).name
            print(player_1.current_room)

    else:
        print("Currently, we must use one of (q, n, s, e, w).\n")
