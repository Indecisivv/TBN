init python:

    class inventory:

        ## item definition ###############################################################
        ##
        ## Args:
        ##  width: The width of the matrix.
        ##  height: The height of the matrix.
        ##  items_matrix: matrix of the items in the inventory
        ##################################################################################
        def __init__(self, width, height, items_matrix):
            self.width = width
            self.height = height
            self.items_matrix = [[None for _ in range(width)] for _ in range(height)]

        ## to string
        def __str__(self):
            return "\n".join(" | ".join(str(item) if item else "None" for item in row) for row in self.items_matrix)

        ## clear inventory
        def clear_inventory(self):
            self.items_matrix = [[None for _ in range(self.width)] for _ in range(self.height)]

        ## add item ######################################################################
        ## Adds item to matrix, assume we are always placing the upper right corner in [row][col]
        ##
        ## Args:
        ##  item: item to add
        ##  row: row of upper right corner
        ##  col: column of upper right corner
        ## Returns:
        ##  True if item had space to be placed and is now in the matrix
        ##  False if item couldn't be placed
        ##################################################################################
        def add_item(self, item, row, col):
            if self.check_neighbors(row, col, item.width, item.height, item):
                if item.item_type == "R":
                    for i in range(item.height):
                        for j in range(item.width):
                            self.items_matrix[row + i][col + j] = item
                    return True
                elif item.item_type == "L":
                    for i in range(item.height):
                        self.items_matrix[row + i][col] = item
                    for j in range(item.width):
                        self.items_matrix[row][col + j] = item
                    return True
            return False

        ## remove item ####################################################################
        ## searches entire matrix for item, if item still has uses left then minus a use and return, 
        ## otherwise continue and delete all instances of item.
        ##
        ## Args:
        ##  item: item to remove
        ## Returns:
        ##  True if item deleted
        ##  False if item had more uses left and not fully deleted
        ##################################################################################
        def remove_item(self, item):
            for i in range(self.height):
                for j in range(self.width):
                    if self.items_matrix[i][j] == item and item.uses <= 1:
                        self.items_matrix[i][j] = None
                    elif self.items_matrix[i][j] == item and item.uses > 1:
                        item.uses -= 1
                        return False
            return True

        ## remomoveve item ####################################################################
        ## searches entire matrix for item, remove it from the matrix so it can be
        ## 
        ##
        ## Args:
        ##  item: item to remove
        ## Returns:
        ##  void
        ##################################################################################
        def move_item(self, item):
            for i in range(self.height):
                for j in range(self.width):
                    if self.items_matrix[i][j] == item:
                        self.items_matrix[i][j] = None


        ## Check Neighbors ################################################################
        ## Check the matrix starting from top right given coordinate[row][col], 
        ## check if the neighbors are empty give the size and item shape type
        ##
        ## Args:
        ##  matrix: The matrix (list of lists)
        ##  row: The row index of the element.
        ##  col: The column index of the element.
        ##  width: The width of the matrix.
        ##  height: The height of the matrix.
        ##  item: 
        ##
        ## Returns:
        ##  True if the given range is all None
        ##  False if any one of the given neighbors are occupied by any item 
        ##################################################################################
        def check_neighbors(self, row, col, width, height, item):
            if item.item_type == "R":
                # Check if the square exceeds matrix boundaries
                if row + height > self.height or col + width > self.width:
                    #renpy.say(e, "square too big")
                    return False  # Out of bounds

                for i in range(height): # Moves downward
                    for j in range(width): # Moves right
                        if self.items_matrix[row + i][col + j] is not None:
                            #renpy.say(e, "no room 1")
                            return False

            elif item.item_type == "L":
                # Check if the L exceeds matrix boundaries
                if row + height > self.height or col + width > self.width:
                    #renpy.say(e, "L too big")
                    return False  # Out of bounds

                for i in range(height): # Check vertical part (going downward)
                    if self.items_matrix[row + i][col] is not None:
                        #renpy.say(e, "no room 2")
                        return False
                for j in range(1, width):  # Check horizontal part (going right)
                    if self.items_matrix[row][col + j] is not None:
                        #renpy.say(e, "no room 3")
                        return False

            return True # if room is free for the item

        ## has item ########################################################################
        ## Checks if an item is already placed anywhere in the inventory matrix
        ##
        ## Args:
        ##  item: The item to search for
        ##
        ## Returns:
        ##  True if the item exists in the inventory
        ##  False otherwise
        ###################################################################################
        def has_item(self, item):
            for row in self.items_matrix:
                if item in row:
                    return True
            return False

# Initialization - Do not delete
default the_inventory = inventory(4, 3, [])