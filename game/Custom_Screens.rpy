#Perhaps instead of a drag and drop system we could use a binary up/down left/right button press system?
#Have user manually click keys to cycle between the widgets and select a coordinate to drop on
#This would be more consistent since, as of now, the drag/drop system is a tad finicky when trying to drop on a specific tile
#This would also be more work though, and would be a pain


image ninepatch paper tiled = Frame("ninepatch paper", 40, 40, 40, 40, tile=True)

image InventoryBackground = Frame("gui/inventory bg.png")


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

         
        #If item is successfully added to inventory on drop, snap 
        if (the_inventory.add_item(ItemDictionary[dragged_items[0]], int(float(dropped_on.drag_name[0])), int(float(dropped_on.drag_name[2])))): 
            dragged_items[0].snap((dropped_on.x / config.screen_width) - (ColumnParity  * (ItemDictionary[dragged_items[0]].width - 1)), (dropped_on.y / config.screen_height))
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
        if (the_inventory.has_item(ItemDictionary[dragged_items[0]])):
            the_inventory.move_item(ItemDictionary[dragged_items[0]])


        else:
            print("FAILED TO REMOVE")
            return


    #Overloads right click
    #Use for rotating?
    def OnRightClick():
        print("Screen Height: " + str(config.screen_height))
        print("Screen Width: " + str(config.screen_width))


    #The hide/show functions below are expected to be one-and-done calls tied to player progression
    #For example, calling HideDayOneItems will hide the items not taken after the player has finished choosing items and moved on
    #This is because of how the inventory group works, all draggables must be in the same group
    #So when they inventory group is shown, ALL draggables are shown
    #But we don't want day 2 items to appear until the day 2 shop
    #So the day 2 items must be hidden until the day 2 shop comes, at which they will be shown, and then hidden again when the player progresses
    #When they get hidden, they still technically exist, but can't be interacted with  
    #Janky Ass Solution but it will do 

    #Cycle through all the draggables and hide the ones not in the inventory
    def HideAllNonInventoryItems():
        for x in ItemDictionary:
            if (the_inventory.has_item(ItemDictionary[x]) == False):
                x.set_child(Null())
                x.draggable = False

    #Hide items from the day 1 shop
    def HideDayOneItems():
        for x in DayOneItemList:
            if (the_inventory.has_item(ItemDictionary[x]) == False):
                x.set_child("transparent.png")
                x.draggable = False  

    #Hide items from the day 2 shop
    def HideDayTwoItems():
        for x in DayTwoItemList:
            if (the_inventory.has_item(ItemDictionary[x]) == False):
                x.set_child("transparent.png")
                x.draggable = False  


    def ShowDayOneShopItems():
        DayOneItemList[0].set_child("antidote.png")
        DayOneItemList[0].draggable = True
        DayOneItemList[1].set_child("food.png")
        DayOneItemList[1].draggable = True
        DayOneItemList[2].set_child("flute.png")
        DayOneItemList[2].draggable = True
        DayOneItemList[3].set_child("brand.png")
        DayOneItemList[3].draggable = True
        DayOneItemList[4].set_child("knife.png")
        DayOneItemList[4].draggable = True
        DayOneItemList[5].set_child("health.png")
        DayOneItemList[5].draggable = True
        DayOneItemList[6].set_child("gold.png")
        DayOneItemList[6].draggable = True
        DayOneItemList[7].set_child("water.png")
        DayOneItemList[7].draggable = True

    def ShowDayTwoShopItems():
        DayTwoItemList[0].set_child("antidote.png")
        DayTwoItemList[0].draggable = True
        DayTwoItemList[1].set_child("food.png")
        DayTwoItemList[1].draggable = True
        DayTwoItemList[2].set_child("flute.png")
        DayTwoItemList[2].draggable = True
        DayTwoItemList[3].set_child("brand.png")
        DayTwoItemList[3].draggable = True
        DayTwoItemList[4].set_child("knife.png")
        DayTwoItemList[4].draggable = True
        DayTwoItemList[5].set_child("health.png")
        DayTwoItemList[5].draggable = True
        DayTwoItemList[6].set_child("gold.png")
        DayTwoItemList[6].draggable = True
        DayTwoItemList[7].set_child("water.png")
        DayTwoItemList[7].draggable = True
        


screen Inventory_Screen:
    modal True   

    frame:
        xalign 0.1
        yalign 0.2
        add "gui/inventory bg.png"

    add InventoryGroup

        #image Frame("ninepatch paper", 40, 40, 40, 40, tile=True):
        #   xalign 0.25
        #  size (840, 600)


transform ButtonPos:
    xalign 0.05
    yalign 0.05

#Main button to display inventory
screen inventory_button():
    imagebutton:
        xalign 1.0
        yalign 0.0
        auto "gui/inventory button_%s.png" action [Show("Inventory_Screen"), Hide("inventory_button"), Show("close_inventory_button")]



screen close_inventory_button():
    imagebutton:
        xalign 1.0
        yalign 0.0
        auto "gui/inventory button active_%s.png" action [Hide("Inventory_Screen"), Show("inventory_button"), Hide("close_inventory_button")]






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


