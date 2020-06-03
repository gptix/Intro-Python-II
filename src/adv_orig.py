from room import Room
from player import Player

# Instantiate rooms
rooms = {
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

# Define allowed movement
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# dictinary to convert from letters to words, for use in output.
direction_letter_name = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}

# list of allowed direction letters
direction_letters = direction_letter_name.keys()

def direction_letter_to_word(dir_letter):
    return direction_letter_name[dir_letter]

def is_movement_possible(direction):
    possible_movement_attribute = direction + '_to'
    return hasattr(player_1.current_room, possible_movement_attribute)

def move(direction):
    to = direction + '_to'
    player_1.current_room = getattr(player_1.current_room, to)

def game_loop():
    while True:
        print()
        # * Prints the name of the current room
        print(f'You are currently in room {player_1.current_room.name}.')
        # * Prints the current description
        print(f'{player_1.current_room.description}')
        
        # * Prompts for user input to take next action
        action = input('What shall we do?')
        
        # If input is 'q', the game prints a good-bye message and exits.
        if action == 'q':
            print("You did super! See you again, soon!")
            break      
           
        # If input is in ['n','e','s','w'], the game tries to move there.
        elif action in direction_letters:
            if is_movement_possible(action):
                print(f'We boldly go {direction_letter_name[action]}!')
                move(action)
                
            else: # movement in desired direction is not allowed.
                print(f'Stymied! There is no way to move {direction_letter_name[action]}!')
        
        # invalid data was entered.
        else: 
            print("Please enter one of [n, e, s, w, q (for quit).]")
            
def __main__():
    # Instantiates a 'Player'
    # Assigns 'outside' as the current 'room'
    player_1 = Player(room['outside'])
    game_loop()