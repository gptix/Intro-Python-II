from room import Room
from player import Player
from item import Item

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

item = {
    'torch': Item('tiki', 'A Hawaiian-looking torch'),
    'sword': Item('sword', 'A rusty sword'),
    'jewel': Item('emerald', 'A shiny green rock'),
    'nail': Item('nail', 'Just a nail'),
    'flask': Item('flask', 'A flask with a mysterious liquid'),
    'scroll': Item('scroll', 'A rolled up parchment'),
    'bag': Item('coinbag', 'A leather pouch of shiny doubloons')
}

initial_location = room.get('outside')
player_1 = Player(initial_location)

# Assignments of items to rooms
item_room_setup = [
    ('outside', 'torch'),
    ('foyer', 'sword'),
    ('foyer', 'nail'),
    # ('foyer', 'flask'),
    # ('overlook', 'jewel'),
    # ('narrow', 'flask'),
    # ('narrow', 'scroll'),
    # ('treasure', 'bag')
]

for pair in item_room_setup:
    my_room = room[pair[0]]
    my_item = item[pair[1]]
    my_room.add_item(my_item)






def get_user_input():
    return  input('What shall we do? ').split()


quit_commands = ['q', 'quit', 'cancel', 'end', 'bye', 'goodbye']
move_commands = ['n', 's', 'e', 'w']
get_verbs = ['g', 'get', 't', 'take']
drop_verbs = ['d', 'drop']
verbs = get_verbs + drop_verbs

def find_input_format_problems(u_input):
    input_length = len(u_input)
    problems_exist = (input_length == 0 or 
                    input_length > 2 or
                    (input_length == 1 and (u_input[0] not in quit_commands) and (u_input[0] not in move_commands)) or
                    (input_length == 2 and u_input[0] not in verbs))
    return problems_exist


def give_hints():
    print('Valid commands:')
    print(f"To quit: {', '.join(quit_commands)}")
    print(f"To move: {', '.join(move_commands)}")
    print("To get: g, get, t, take")
    print("To drop: d, drop")
    print("Currently, lowercase only.\n")

def quit_game():
    print("You did super! See you again, soon!")

def identify_location():
    print(f'{player_1.name}, you are currently in the room named \'{player_1.current_room.name}\'\n')


while True:
#     # Describe situation
    identify_location()
    player_1.current_room.describe_location()

    # Ask for orders
    u_input = get_user_input()

    # Check input - number of words, correct first word
    if find_input_format_problems(u_input):
        give_hints()

    else: # we know there is a valid command.  We have not checked any thing to be getted or dropped
        input_count = len(u_input)

        if input_count == 1:

            # We know it is a single=-word command
            if u_input[0] in quit_commands:
                quit_game()
                break

            else: 
                direction = u_input[0]
                player_1.try_to_move(direction)

        else: # we know the command has two parts, and the first one is either get or drop
            thing = u_input[1]
            if u_input[0] in get_verbs:
                player_1.try_to_get(thing)
            else:
                player_1.try_to_drop(thing)
