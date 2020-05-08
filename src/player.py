# A class to hold player information:
# * what room they are in currently.

class Player:
    def __init__(self, current_room, items=[]):
#        super().__init__()
        self.current_room = current_room
        self.items = items
    
    def __str__(self):
        return f'<Player - current_room: {self.current_room} - items_holding: {self.items_holding}>'
    
    def move(self, direction):
        self.current_room = getattr(self.current_room, direction + '_to')
        
    def take(self, thing):
#         print(self.items)
        self.items.append(thing)
#         print(self.items)
    
    def drop(self, thing_name):
        things = [itm for itm in self.items if itm.name == thing_name]
        if len(things) == 0:
            print(f'You do not have a {thing_name}.')
            return None
        else:
            thing = things[0]
            self.items = [i for i in self.items if i != thing]
            return thing
        
    def describe(self):
        item_count = len(self.items)
        if item_count == 0:
            print(f'You don\'t have any items.')
        elif item_count == 1:
            print(f'You have this: {self.items[0].name}')
        else:
            print(f'You have these: {", ".join([itm.name for itm in self.items])}')