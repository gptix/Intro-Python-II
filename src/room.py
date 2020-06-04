# A class to hold room information:
# * name
# * description

class Room:
    def __init__(self, name, description, items=[]):
#        super().__init__()
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'<Room - name: {self.name} - description: {self.description}  room_items: {self.items}>'


    def add_item(self, itm):
        # print("In method\n")
        # print(itm)
        # print()
        # print(f'Adding {itm.name} to {self.name}\n')
        self.items.append(itm)



    def describe_location(self):
        # * Prints the current description (the textwrap module might be useful here).
        print(f'{self.description}\n')
        item_names = [itm.name for itm in self.items]
        print(f'You see these items: {item_names}')