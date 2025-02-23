init python:
    
    class item:

        ## item definition ###############################################################
        ##
        ## Args:
        ##  name: name of item
        ##  description: description of item
        ##  width: The width of the matrix inventory.
        ##  height: The height of the matrix inventory.
        ##  uses: How many times the item can be used before it is removed
        ##  item_type: item_type either "L" for L shaped object or "R" for rectangle/square shaped object
        ##################################################################################
        def __init__(self, name, description, width, height, uses, item_type):
            self.name = name
            self.description = description
            self.width = width
            self.height = height
            self.uses = uses
            self.item_type = item_type

        ## to string
        def __str__(self):
            return f"{self.name} ({self.width}x{self.height}, {self.uses} uses left, {self.item_type})"

        def get_description(description):
            return self.description
        
        def get_name(self):
            return self.name
        
        def get_width(self):
            return self.width
        
        def get_height(self):
            return self.height

        def get_uses(self):
            return self.uses

        def rotate_item(self):
            self.width, self.height = self.height, self.width