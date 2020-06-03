# A class to hold player information:
# * what room they are in currently.

class Player:
    def __init__(self, name='Roger', current_room='outside'):
        self.name = name
        self.current_room = current_room

    
    def __str__(self):
        return f'<Player - current_room: {self.current_room}>'

