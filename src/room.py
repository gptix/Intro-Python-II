# A class to hold room information:
# * name
# * description

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
#        super().__init__()
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return f'<Room - name: {self.name} - description: {self.description}>'