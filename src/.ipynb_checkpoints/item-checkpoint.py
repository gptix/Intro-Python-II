class Item:
    def __init__(self, name, description):
#         super().__init__()
#The item should have name and description attributes.
        self.name = name
        self.description = description

    def __str__(self):
        return f'<Item - name: {name} - description: {description}>'

#Hint: the name should be one word for ease in parsing later.
#This will be the base class for specialized item types to be declared later.