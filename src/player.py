# A class to hold player information:
# * what room they are in currently.

class Player:
    def __init__(self, current_room='outside', name='Roger', carrying=[]):
        self.name = name
        self.current_room = current_room
        self.carrying = carrying

    
    def __str__(self):
        return f'<Player - current_room: {self.current_room}>'

    def try_to_move(self, direc):
        # we know that the direction is a legal direction, but it might not
        # be possible from the current room.
        possible_dir_to_attribute_string = direc + '_to'
        next_room = getattr(self.current_room, possible_dir_to_attribute_string, None)

        if next_room is None:
            print(f"I'm sorry Dave, there is no way to go {direc} from here.")

        else:
            self.current_room = next_room


    def try_to_get(self, thing_name):
        # we know that the verb is a get verb, but the thing might not be available.
        item_or_not = [itm for itm in self.current_room.items if itm.name == thing_name]
        there_is_one = len(item_or_not) == 1
        if there_is_one:
            item = item_or_not[0]
            self.carrying.append(item)
            self.current_room.items.remove(item)
        else:
            print(f"I'm sorry Dave, there is no {thing_name} here.")


    def try_to_drop(self, thing_name):
        # we know that the verb is a drop verb, but the thing might not be available.
        item_or_not = [itm for itm in self.carrying if itm.name == thing_name]
        there_is_one = len(item_or_not) == 1
        if there_is_one:
            item = item_or_not[0]
            self.carrying.remove(item)
            self.current_room.items.append(item)
        else:
            print(f"I'm sorry Dave, you have no {thing_name} to drop.")


