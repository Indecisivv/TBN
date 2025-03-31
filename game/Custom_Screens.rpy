

#Perhaps instead of a drag and drop system we could use a binary up/down left/right button press system?
#Have user manually click keys to cycle between the widgets and select a coordinate to drop on
#This would be more consistent since, as of now, the drag/drop system is a tad finicky when trying to drop on a specific tile
#This would also be more work though, and would be a pain


#The image sizes are going to need to line up with the final inventory space sizing,
#such that when they snap, it looks natural
#we can worry about that later



image ninepatch paper tiled = Frame("ninepatch paper", 40, 40, 40, 40, tile=True)

#Use Default to define items, not Define, since items can change
#Should probably move all this to its own file
default Guitar = item("Guitar", "A Stringed Instrument", 3, 1, 20, "R")
default Flute = item("Flute", "A Wind Instrument", 1, 3, 1, "R")
default Biscuit = item("Biscuit", "A Hearty Pastry", 1, 1, 1, "R")
default Pizza = item("Pizza", "A Savory, Foreign Cuisine", 2, 2, 5, "R")
default Cake = item("Cake", "A Hearty Pastry", 1, 1, 5, "R")


#Every Item in the game MUST be added to this list
#This way it can be found when attempting to add it to the inventory via drag/drop
default ItemList = [Cake, Biscuit, Pizza, Guitar, Flute]


#Drag objects with names that correspond to a specific item
#The name MUST match the desired item
#I would've liked to make a custom class or something,
#but I couldn't get an alternate method/class that linked drag objects with item data to work
#so this will have to do
default biscuit = Drag(d = Solid("#10f609", xysize=(200, 200)), drag_name = "Biscuit", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.5, 0.5))
default pizza = Drag(d = Solid("#ff9811", xysize = (400, 400)), drag_name = "Pizza", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.0, 0.8))
default guitar = Drag(d = Solid("#522801", xysize = (600, 200)), drag_name = "Guitar", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.7, 0.8))
default flute = Drag(d = Solid("#ffdec0", xysize = (200, 600)), drag_name = "Flute", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.0, 0.0))




#All these numbers are subject to change
#Distance between columns
default ColumnParity = 0.125

#At what vertical alignment does the inventory start?
default ColumnStartPoint = 0.3

#Distance between rows
default RowParity = 0.2

#At what horizontal alignment does the inventory start?
default RowStartPoint = 0.2

default Column1Pos = ColumnStartPoint + (ColumnParity * 3)
default Column2Pos = ColumnStartPoint + (ColumnParity * 2)
default Column3Pos = ColumnStartPoint + ColumnParity
default Column4Pos = ColumnStartPoint


default Row1Pos = RowStartPoint
default Row2Pos = RowStartPoint + RowParity
default Row3Pos = RowStartPoint + RowParity + RowParity

default SpaceAnchor = (0.0, 0.0)

#Empty spaces that represent coordinates and locations that items can be placed on
default Space1 = Drag(d = "blank.png", drag_name = "0.0", draggable = False, anchor = SpaceAnchor, pos = (Column1Pos, Row1Pos))
default Space2 = Drag(d = "blank.png", drag_name = "0.1", draggable = False, anchor = SpaceAnchor, pos = (Column2Pos, Row1Pos))
default Space3 = Drag(d = "blank.png", drag_name = "0.2", draggable = False, anchor = SpaceAnchor, pos = (Column3Pos, Row1Pos))
default Space4 = Drag(d = "blank.png", drag_name = "0.3", draggable = False, anchor = SpaceAnchor, pos = (Column4Pos, Row1Pos))

default Space5 = Drag(d = "blank.png", drag_name = "1.0", draggable = False, anchor = SpaceAnchor, pos = (Column1Pos, Row2Pos))
default Space6 = Drag(d = "blank.png", drag_name = "1.1", draggable = False, anchor = SpaceAnchor, pos = (Column2Pos, Row2Pos))
default Space7 = Drag(d = "blank.png", drag_name = "1.2", draggable = False, anchor = SpaceAnchor, pos = (Column3Pos, Row2Pos))
default Space8 = Drag(d = "blank.png", drag_name = "1.3", draggable = False, anchor = SpaceAnchor, pos = (Column4Pos, Row2Pos))

default Space9 = Drag(d = "blank.png", drag_name = "2.0", draggable = False, anchor = SpaceAnchor, pos = (Column1Pos, Row3Pos))
default Space10 = Drag(d = "blank.png", drag_name = "2.1", draggable = False, anchor = SpaceAnchor, pos = (Column2Pos, Row3Pos))
default Space11 = Drag(d = "blank.png", drag_name = "2.2", draggable = False, anchor = SpaceAnchor, pos = (Column3Pos, Row3Pos))
default Space12 = Drag(d = "blank.png", drag_name = "2.3", draggable = False, anchor = SpaceAnchor, pos = (Column4Pos, Row3Pos))



#Add All spaces and drag objects
#drag objects must be in this list as well, 
#otherwise they won't interact with the empty spaces in the way we want
default InventoryGroup = DragGroup(Space1, Space2, Space3, Space4,
Space5, Space6, Space7, Space8,
Space9, Space10, Space11, Space12,
biscuit, guitar, flute, pizza)


#These essentially declare custom functions that you can apply to drag variables such as 'dragged, 'dropped', 'clicked', etc.
#When you try to drop an item on a droppable, check if the matching coordinate in the_inventory is occuppied
#Parse the droppables coordinate from either its location or name
#https://www.renpy.org/doc/html/drag_drop.html
init python:
    #Overloads dragged
    #Dragged is called when you release an item after dragging (when you have dropped a drag after dragging it)
    def drag_placed(dragged_items, dropped_on):
        print("Name: " + dragged_items[0].drag_name)


        #If placed on empty space
        if not dropped_on: 
            print("Nothing There!")
            return

        
        for i in range(len(ItemList)):
            #Search the array for the desired item whos name matches the drop object  
            if (ItemList[i].name == dragged_items[0].drag_name):       
                #If item is successfully added to inventory on drop, snap 
                if (the_inventory.add_item(ItemList[i], int(float(dropped_on.drag_name[0])), int(float(dropped_on.drag_name[2])))): 
                    dragged_items[0].snap((dropped_on.x / config.screen_width) - (ColumnParity  * (ItemList[i].width - 1)), (dropped_on.y / config.screen_height))
                    return
                else:
                    print("SPACE IS OCCUPPIED")
                    print("X: " + dropped_on.drag_name[0])
                    print("Y: " + dropped_on.drag_name[2])
                    return

    #Overload left clicked
    #Remove item from the inventory when clicked if in the inventory
    def OnActivate(dragged_items):
        print("Activated!")
        for i in range(len(ItemList)):
            #Search the array for the desired item whos name matches the drop object  
            if (ItemList[i].name == dragged_items[0].drag_name):       
                print("FOUND MATCHING ITEM IN ITEM LIST")
                if (the_inventory.has_item(ItemList[i])):
                    the_inventory.move_item(ItemList[i])
                    print("REMOVED ITEM")
                    return
                else:
                    print("FAILED TO REMOVE")
                    return




    #Overloads right click
    #Use for rotating?
    def OnRightClick():
        print("Screen Height: " + str(config.screen_height))
        print("Screen Width: " + str(config.screen_width))



screen Inventory_Screen:
    modal True   
    add InventoryGroup

        #image Frame("ninepatch paper", 40, 40, 40, 40, tile=True):
        #   xalign 0.25
        #  size (840, 600)




#WIP
#Main button to display inventory
screen inventory_button():
    frame:
        xalign 0.05 yalign 0.05
        vbox:
            textbutton "Show Inventory" action [Show("Inventory_Screen"), Hide("inventory_button"), Show("close_inventory_button")]


screen close_inventory_button():
    frame:
        xalign 0.05 yalign 0.05
        vbox:
            textbutton "Hide Inventory" action [Hide("Inventory_Screen"), Show("inventory_button"), Hide("close_inventory_button")]





#REFERENCE/TEST SCREEN RIPPED FROM TUTORIAL
screen day_planner():

    # This vbox organizes everything.
    vbox:

        spacing 5

        # A frame containing all the stats.
        frame:
            style_prefix "stat"
            xpadding 150
            xfill True

            vbox:

                hbox:
                    text _("Strength")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Intelligence")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Moxie")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Chutzpah")
                    bar value StaticValue(stat_strength, 100)


        # A grid of three frames, one for each of the periods in the day.
        grid 3 1:

            spacing 5
            xfill True

            for p in day_periods:

                frame:
                    xfill True

                    vbox:
                        label p

                        null height 5

                        for i in day_choices:
                            textbutton i action SetDict(day_plan, p, i)

        # This is a grid containing two empty space and the done button,
        # so everything lines up.
        grid 3 1:
            xfill True
            spacing 5

            null

            frame:
                textbutton _("Done"):
                    action Return(True)
                    xfill True

                    text_xalign 0.5

            null


