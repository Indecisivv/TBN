
define e = Character("Eileen")

define e_shout = Character("Eileen", who_color="#c8ffc8", what_size=34)
define e_whisper = Character("Eileen", who_color="#c8ffc8", what_size=18)
define e1 = Character("Eileen", window_background="gui/startextbox.png")

#"The who_color and what_color properties set the color of the character's name and dialogue text, respectively."
#"The colors are strings containing rgb hex codes, the same sort of colors understood by a web browser."
define e2 = Character("Eileen", who_color="#c8ffc8", what_color="#ffc8c8")

#"Similarly, the who_font and what_font properties set the font used by the different kinds of text."
define e3 = Character("Eileen", who_font="Roboto-Regular.ttf", what_font="Roboto-Light.ttf")



define e8 = Character(
    None,
    window_background = None,

    what_size=28,
    what_outlines=[( 1, "#008000", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')
 

#By using kind, you can copy properties from one character to another
define l8 = Character(kind=e8, what_outlines=[( 1, "#c00000", 0, 0 )] )
 
#Special character that speaks with narration
define narrator = Character(what_italic=True)
 


define s = Character("Sylvie")
define l = Character("Lucy")

#define g = Character("[name]")
 
image logo base = "logo base.png"
image logo alias = "logo base"
image logo rotated = Transform("logo base", rotate=45)

image ninepatch paper tiled = Frame("ninepatch paper", 40, 40, 40, 40, tile=True)
 
image lucy animated:
    "lucy happy"
    pause 0.5
    "lucy mad"
    pause 0.5
    repeat

image eileen animated:
    "eileen vhappy"
    pause 0.5
    "eileen happy"
    pause 0.5
    repeat
 
image speen:
    "spin_1.png"
    pause 0.1
    "spin_2.png"
    pause 0.1
    "spin_3.png"
    pause 0.1
    "spin_4.png"
    pause 0.1
    "spin_5.png"
    pause 0.1
    "spin_6.png"
    pause 0.1
    "spin_7.png"
    pause 0.1
    "spin_8.png"
    pause 0.1
    repeat
        



define slowdissolve = Dissolve(1.0)
 






label DebugIntro:
    $ menu_flag = False
    $ menu_what = False
    $ name = "Default"



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg meadow
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    with dissolve
    show eileen happy
    with dissolve

    e "Where would you like to go?"


    menu:
        "Generic Debug":
            jump DebugTest
        "Item Test":
            jump DebugItemCheck
        "Gender Test":
            jump GenderQuestion


    



default TestBool = True


 






label DebugItemCheck:
    #Index 1 represents row, index 2 represents column
    #$ the_inventory.add_item(Biscuit, 0, 0)
    #$ the_inventory.add_item(Pizza, 0, 0)

    #Test to ensure objects of size greater than 1x1 take up their proper places
    
    #if the_inventory.add_item(Flute, 0, 0):
    #    "Added a Flute at 0-0"
    #else:
    #    "Failed To Add a Flute! That Space is already Occuppied"
    
    #if the_inventory.add_item(Guitar, 0, 0):
    #    "Added a Guitar at 0-0"
    #else:
    #    "Failed To Add a Guitar! That Space is already Occuppied"

    #if the_inventory.add_item(Biscuit, 0, 1):
    #    "Added a Biscuit!"
    #else:
    #    "Failed To Add a Biscuit! That Space is already Occuppied"

    #$ the_inventory.remove_item(Guitar)

    #"Removed the Guitar!"

    #if the_inventory.add_item(Biscuit, 0, 1):
    #    "Added a Biscuit!"
    #else:
    #    "Failed To Add a Biscuit! That Space is already Occuppied"

    #show screen inventory_button

    if TestBool:
        "This is true"
    else:
        "This is False"




    "Here's the button"

    

    #call screen Inventory_Screen
 

    "Here's the inventory"



    """
    Quietly you reach under the bunk to pull out your stuff.

    """

    show screen Inventory_Screen

    show screen close_inventory_button

    pause 0.5

    $ HideAllNonInventoryItems()

    "1"

    "2"

    "3"

    "4"

    "5"


    show ninepatch paper tiled at Quarter:
        size (840, 600)

    "Here's a Paper"







    menu:
        "You have a Guitar" if the_inventory.has_item(Guitar) == True:
            "You do indeed have a Guitar"

        "You have a Biscuit" if the_inventory.has_item(Biscuit) == True:
            "You do indeed have a Biscuit"


        "You DON'T have a Guitar" if the_inventory.has_item(Guitar) == False:
            "I don't have a Guitar, sorry"   

        "You DON'T have a Pizza" if the_inventory.has_item(Pizza) == False:
            "I don't have a Pizza, sorry"   

        "IDK What to Do":
            "Gosh if only you had a Guitar"





    

 


label DebugTest:
        
    e "Hello."
    #show sylvie blue giggle at right
    with dissolve


    show lucy happy at AnchorHalfBottom
    show lucy happy at zoomInLeft behind eileen

    l "Here I am!!!!!"

    show eileen behind lucy

    show sylvie blue normal at CutIn

    s "Cutting In"

    
    show sylvie blue normal at CutOut

    s "Cutting Out"

    show lucy at TintShader

    l "Here's the tinttest"

    show lucy at NormalTint

    l "Normalizign tint"

    show lucy at HueShader

    l "Here's the huetest"

    show lucy at BrightnessShader

    l "Here's the brighttest"

    show lucy at NormalBrightness

    l "Normalizign brightness"

    show speen at AnchorHalfBottom
    show speen at center

    show lucy at confuseFacingRight
    show speen at confuseFacingRight
    l "wtf are u talking about?"
    show speen at confuseFacingLeft
    show lucy at Straighten
    l "straightening"
    show lucy at flipLeft
        
    l "fleep"

    show lucy at confuseFacingLeft
    l "NOW wtf are u talking about?"
    show speen at Straighten
    show lucy at Straighten
    l "Ok I get it now"
    show lucy at MoveToRight
    l "To the right"
    show lucy at flipRight
        
    l "fleep 2"
    
    show lucy at MoveToRight

    l "I added {i}this{i}  \"line\" myself."
    
    show lucy at MoveToLeft
    l "To the left Now!"
    show lucy at MoveToHalfRight
    l "To the right Now!"
    show lucy at proudAnim
    l "I'm proud"
    show lucy at scaredAnim
    l "I'm scared!"
    
    show lucy at happyAnim
    l "I'm Happy."
    show lucy at spookedAnim
    l "I'm spooked. "
    show lucy mad at sadAnim
    l "I'm sad. "
    show lucy happy at jumpAnim
    l "I'm bouncing."
    show eileen behind lucy
    show lucy at Close
    l "Am I close enough for you? "
    show lucy at VeryClose
    l "How about now? "
    show lucy at Normalize
    pause 0.1
    show lucy at ResetOffset
    show lucy at MiddleRight behind eileen
    with move
    l "Over here!"
    show lucy mad at left behind eileen
    with move
    l "To the left now!"
    l "I'm outta here!"
        
    show lucy at exitRight
    pause
    show logo base:
        xalign .3 yalign .7
        easein 1.0 xalign .7 yalign .3
        easeout 1.0 xalign .3 yalign .7
        repeat

    show lucy animated at left behind eileen
    show eileen animated
    show speen at topmiddle
    l "Animating now!"
    with hpunch

    e "Once you add a story, pictures, and music, you can release it to the world!"
    with vpunch
    show logo base at MiddleRight behind eileen

    scene bg whitehouse
    with slowdissolve
    pause .5
    scene bg washington
    show logo base at MiddleRight behind eileen
    show eileen happy
    with slowdissolve

    e "That was a transition!"
    menu:
        "Yes, I do.":
            jump choice1_yes
        "No, I don't.":
            jump choice1_no
        "What are you talking about":
            jump choice1_what
    label choice1_yes:
        $ menu_flag = True
        e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."
        jump choice1_done
    label choice1_no:
        $ menu_flag = False
        e "Games without menus are called kinetic novels, and there are dozens of them available to play."
        jump choice1_done
    label choice1_what:
        $ menu_what = True
        show lucy happy:
            xalign 1.0
            yalign 1.0
        l "What do you mean?"
        jump choice1_done
    label choice1_done:
        # ... the game continues here.

    if menu_flag:
        e "For example, I remember that you plan to use menus in your game."
    else:
        e "For example, I remember that you're planning to make a kinetic novel, without menus."

    if menu_what:
        e "You were confused about the menu."
    else:
        e "You were NOT confused about the menu."
    python:
        name = renpy.input("What's your name?")
        #.strip removes whitespace
        name = name.strip() or "Guy Shy"

        
    e  "To interpolate a variable, write it in square brackets. Isn't that right, [name]?"
    e "The cps text tag {cps=25}makes text type itself out slowly{/cps}, even if slow text is off."
    e "The cps tag can also be relative to the default speed, {cps=*2}doubling{/cps} or {cps=*0.5}halving{/cps} it."

    e "The k tag changes kerning. It can space the letters of a word {k=-.5}closer together{/k} or {k=.5}farther apart{/k}."

    e "The size tag changes the size of text. It can make text {size=+10}bigger{/size} or {size=-10}smaller{/size}, or set it to a {size=30}fixed size{/size}."

    e "The p tag breaks a paragraph,{p}and waits for the player to click."
    e "If it is given a number as an argument,{p=1.5}it waits that many seconds."

    e "The w tag also waits for a click,{w} except it doesn't break lines,{w=.5} the way p does."

    # This ends the game.