# A class to hold player information:
# * what room they are in currently.

class Player:
    def __init__(self, current_room, items_holding=[]):
#        super().__init__()
        self.current_room = current_room
        self.items_holding = items_holding

    def __str__(self):
        return f'<Player - current_room: {self.current_room} - items_holding: {self.items_holding}>'
