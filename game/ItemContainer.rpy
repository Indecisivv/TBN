#Add Items Here

#When creating a new item, create a correspoding Draggable object that represents said item
#Then, add the draggable and it's item to the dictionary below
#Also, Add the draggable to the InventoryGroup at the bottom



default Guitar = item("Guitar", "A Stringed Instrument", 3, 1, 20, "R")
default Biscuit = item("Biscuit", "A Hearty Pastry", 1, 1, 3, "R")
default Pizza = item("Pizza", "A Savory, Foreign Cuisine", 2, 2, 5, "R")
default Cake = item("Cake", "A Hearty Pastry", 1, 1, 5, "R")



#Use Default to define items, not Define, since items can change
#Should probably move all this to its own file
default Item_Antidote = item("Antidote", "Cures Poison", 1, 1, 3, "R")
default Item_Food = item("Food", "It's Food", 1, 1, 3, "R")
default Item_Flute = item("Flute", "A Wind Instrument", 1, 1, 10, "R")
default Item_Brand = item("Brand", "DEFAULT_DESCRIPTION", 1, 1, 10, "R")
default Item_Knife = item("Knife", "Good for cutting things", 1, 1, 10, "R")
default Item_Health = item("Health Potion", "Heals People", 1, 1, 10, "R")
default Item_Gold = item("Brand", "Money can used to purchase goods and services", 1, 1, 10, "R")
default Item_Water = item("Water", "Hydrating", 1, 1, 10, "R")


#Drag objects with names that correspond to a specific item
default Drag_Antidote = Drag(d = "antidote.png", drag_name = "Antidote", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.75, 0.1))
default Drag_Food = Drag(d = "food.png", drag_name = "Food", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.8, 0.2))
default Drag_Flute = Drag(d = "flute.png", drag_name = "Antidote", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.9, 0.3))
default Drag_Brand = Drag(d = "brand.png", drag_name = "Brand", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.8, 0.4))
default Drag_Knife = Drag(d = "knife.png", drag_name = "Knife", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.75, 0.5))
default Drag_Health = Drag(d = "health.png", drag_name = "Health Potion", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.9, 0.45))
default Drag_Gold = Drag(d = "gold.png", drag_name = "Knife", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.9, 0.1))
default Drag_Water = Drag(d = "water.png", drag_name = "Knife", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.8, 0.5))



default biscuit = Drag(d = Solid("#10f609", xysize=(200, 200)), drag_name = "Biscuit", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.7, 0.2))
default pizza = Drag(d = Solid("#ff9811", xysize = (400, 400)), drag_name = "Pizza", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.6, 0.5))
default guitar = Drag(d = Solid("#522801", xysize = (600, 200)), drag_name = "Guitar", draggable = True, droppable = False, dragged = drag_placed, drag_raise = True, drag_offscreen = True, activated = OnActivate, alternate = OnRightClick, anchor = (0.0, 0.0), pos = (0.7, 0.8))
default testList = [biscuit, pizza, guitar, Drag_Flute]

default DayOneItemList = [Drag_Antidote, Drag_Food, Drag_Flute, Drag_Brand, Drag_Knife, Drag_Health, Drag_Gold, Drag_Water]


default DayTwoItemList = [Drag_Antidote, Drag_Food, Drag_Flute, Drag_Brand, Drag_Knife, Drag_Health, Drag_Gold]

default ItemDictionary = {
    biscuit: Biscuit,
    pizza: Pizza,
    guitar: Guitar,
    Drag_Antidote: Item_Antidote,
    Drag_Food: Item_Food,
    Drag_Flute: Item_Flute,
    Drag_Brand: Item_Brand,
    Drag_Knife: Item_Knife,
    Drag_Health: Item_Health,
    Drag_Gold: Item_Gold,
    Drag_Water: Item_Water
    }



#All these numbers are subject to change
#Distance between columns
default ColumnParity = 0.15

#At what vertical alignment does the inventory start?
default ColumnStartPoint = 0.125

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
default Space1 = Drag(d = "gui/inventory slot.png", drag_name = "0.0", draggable = False, anchor = SpaceAnchor, pos = (Column1Pos, Row1Pos))
default Space2 = Drag(d = "gui/inventory slot.png", drag_name = "0.1", draggable = False, anchor = SpaceAnchor, pos = (Column2Pos, Row1Pos))
default Space3 = Drag(d = "gui/inventory slot.png", drag_name = "0.2", draggable = False, anchor = SpaceAnchor, pos = (Column3Pos, Row1Pos))
default Space4 = Drag(d = "gui/inventory slot.png", drag_name = "0.3", draggable = False, anchor = SpaceAnchor, pos = (Column4Pos, Row1Pos))

default Space5 = Drag(d = "gui/inventory slot.png", drag_name = "1.0", draggable = False, anchor = SpaceAnchor, pos = (Column1Pos, Row2Pos))
default Space6 = Drag(d = "gui/inventory slot.png", drag_name = "1.1", draggable = False, anchor = SpaceAnchor, pos = (Column2Pos, Row2Pos))
default Space7 = Drag(d = "gui/inventory slot.png", drag_name = "1.2", draggable = False, anchor = SpaceAnchor, pos = (Column3Pos, Row2Pos))
default Space8 = Drag(d = "gui/inventory slot.png", drag_name = "1.3", draggable = False, anchor = SpaceAnchor, pos = (Column4Pos, Row2Pos))

default Space9 = Drag(d = "gui/inventory slot.png", drag_name = "2.0", draggable = False, anchor = SpaceAnchor, pos = (Column1Pos, Row3Pos))
default Space10 = Drag(d = "gui/inventory slot.png", drag_name = "2.1", draggable = False, anchor = SpaceAnchor, pos = (Column2Pos, Row3Pos))
default Space11 = Drag(d = "gui/inventory slot.png", drag_name = "2.2", draggable = False, anchor = SpaceAnchor, pos = (Column3Pos, Row3Pos))
default Space12 = Drag(d = "gui/inventory slot.png", drag_name = "2.3", draggable = False, anchor = SpaceAnchor, pos = (Column4Pos, Row3Pos))



#Add All spaces and drag objects
#drag objects must be in this list as well, 
#otherwise they won't interact with the empty spaces in the way we want


#Create a loop that starts from index 12, if not in the inventory, hide it
default InventoryGroup = DragGroup(Space1, Space2, Space3, Space4,
Space5, Space6, Space7, Space8,
Space9, Space10, Space11, Space12,
#biscuit, guitar, pizza, 
Drag_Antidote, Drag_Food, Drag_Flute, Drag_Brand, Drag_Knife, Drag_Health, Drag_Gold, Drag_Water)
