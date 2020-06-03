# A class to hold room information:
# * name
# * description
# The Room class should be extended with a list that holds the Items that are currently in that room.

class Room:
    def __init__(self, name, description, items=[]):
#        super().__init__()
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return "<Room - name: {self.name} - description: {self.description} - items: {items}> "
