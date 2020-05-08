# A class to hold room information:
# * name
# * description
# The Room class should be extended with a list that holds the Items that are currently in that room.

class Room:
    def __init__(self, name, description):
#        super().__init__()
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f'<Room - name: {self.name} - description: {self.description} - items: {self.items}>'
    
    def describe(self):
        print(f'\nYou are currently in the {self.name}.')
        print(f'{self.description}')
        item_count = len(self.items)
        if item_count == 0:
            print(f'You don\'t see any particulaly interesting items.')
        elif item_count == 1:
            print(f'You see this item: {self.items[0].name}')
        else:
            print(f'You see these items: {", ".join([itm.name for itm in self.items])}')
                 
    def movement_is_possible(self, direction):
        return hasattr(self, direction + '_to')
    
    def add_item(self, itm):
#         print("In method\n")
#         print(itm)
#         print()
#         print(f'Adding {itm.name} to {self.name}\n')
        self.items.append(itm)
        
    def remove(self, thing_name):
        things = [itm for itm in self.items if itm.name == thing_name]
        if len(things) == 0:
            print(f'This room does not have a {thing_name}.')
            return None
        else:
#             print(self.items)
            thing = things[0]
            self.items = [i for i in self.items if i != thing]
#             print(self.items)
            return thing
    

