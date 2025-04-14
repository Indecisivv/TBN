#likability values
default max_points = 100
default plo_points = 50
default darcey_points = 30
default quinn_points = 50

#state values
default plo_hungry = False
default darcey_hungry = False
default quinn_hungry = False
default iris_hungry = False

default plo_tired = False
default darcey_tired = False
default quinn_tired = False
default iris_tired = False

default get_serious = False
default quiet = 0
default inside_carriage = False
default magic_score = 0

#character name values
default plo_name = "???"
default darcey_name = "???"
default quinn_name = "???"
define player_name =  ""

#ending values


################################################################################
##  ████  █   █  ███  ████   ███   ████ █████ █████ ████  █████ 
##  █     █   █ █   █ █   █ █   █ █       █   █     █   █ █     
##  █     █████ █████ ████  █████ █       █   ████  ████  █████ 
##  █     █   █ █   █ █   █ █   █ █       █   █     █   █     █ 
##   ████ █   █ █   █ █   █ █   █  ████   █   █████ █   █ █████ 
##  https://lingojam.com/GiantTextGenerator
################################################################################
#main characters
define Iris = Character("[player_name]", who_color="#ffc23e")
define Plo = Character("[plo_name]", who_color="#6cff3b")
define Darcey = Character("[darcey_name]", who_color="#f95959")
define Quinn = Character("[quinn_name]", who_color="#bca6eb")
#side characters
define Officer = Character("Officer", color="#ffffff")
define Captain = Character("Captain", color="#ffffff")
define Bunkmate = Character("Bunkmate", color="#ffffff")

#temp
################################################################################
#Weather
image rain1fast = Fixed(SnowBlossom("gui/rain1.png", 10, xspeed=(-1000, -900), yspeed=(2000, 1900), start=50, fast=True, horizontal=False))
image rain2fast = Fixed(SnowBlossom("gui/rain2.png", 25, xspeed=(-1000, -900), yspeed=(2000, 1900), start=50, fast=True, horizontal=False))

image rain1slow = Fixed(SnowBlossom("gui/rain1.png", 5, xspeed=(-1000, -900), yspeed=(2000, 1900), start=50, fast=True, horizontal=False))
image rain2slow = Fixed(SnowBlossom("gui/rain2.png", 15, xspeed=(-1000, -900), yspeed=(2000, 1900), start=50, fast=True, horizontal=False))
#endregion


#for spawning flipped
transform flip:
    xzoom -1.0
transform unflip:
    xzoom 1.0


################################################################################
##  ████   ███  █   █ █████   █████ █████  ███  ████  █████ 
##  █     █   █ ██ ██ █       █       █   █   █ █   █   █   
##  █  ██ █████ █ █ █ ████    █████   █   █████ ████    █   
##  █   █ █   █ █   █ █           █   █   █   █ █   █   █   
##   ███  █   █ █   █ █████   █████   █   █   █ █   █   █   
################################################################################
label start:
    
    # Name characterS
    $ player_name = renpy.input("What would you like to name your character?", default="Iris", length=20).strip()

    if player_name == "":
        $ player_name = "Iris"

    # jump DebugIntro

    camera:
        perspective True

################################################################################
## ▀█▀ █▄ █ ▀█▀ █▀█ █▀█ 
## ▄█▄ █ ▀█  █  █▀▄ █▄█ 
################################################################################
    label intro:
    
    
    """
    Deep within a vast cave system,{cps=4} {/cps}warmed by the geothermal currents of an underground aquifer,{cps=4} {/cps}lies your camp.
    """
    scene cave with Dissolve(1.5)
    """
    Humidity and dirt clings to your skin as stalactites loom overhead{cps=4} {/cps}with mineral-rich condensation.

    You are called urgently to the Captain's Chamber.{cps=2} {/cps}At this hour in the night? Strange.{cps=2} {/cps}Nervousness creeps into your steps.

    Through winding tunnels,{cps=4} {/cps}you follow the jagged walls with your torchlight.
    
    Heated water hisses from the fissures above.
    
    Outside the Captain's Chamber,{cps=4} {/cps}the air is thick with the scent of damp rock.

    You step in.
    """
    #TODO: maybe like a step sfx here

    scene tent with Dissolve(1.5)

    #TODO: pan around captains chambers

    """
    The Captain's Chamber flaunts its roominess compared to the path it takes to get there.{cps=4} {/cps}Space must be made for the parchments.

    The scent of ink,{cps=4} {/cps}sweat,{cps=4} {/cps}and something vaguely metallic catch your nose immediately. 

    You warm up from the burning oil lamps around,{cps=4} {/cps}and walk forward to the sturdy wooden desk.
    
    Maps and smudged reports scatter in front of the tired man hunched over, staring down at them.{cps=4} {/cps}The Captain. 
    """

    show iris worried at right
    show iris at flip
    show captain
    with Dissolve(1.5)

    """
    On closer inspection, you notice the Captain's dark circles under his bloodshot eyes.{cps=4} {/cps}Who knows when he last moved.
    
    He barely reacted to your approach.

    You give him a quick salute and announce your presence.
    """

    show iris neutral
    Iris "Captain."

    Captain "[player_name],{cps=4} {/cps}wait there,{cps=4} {/cps}I have more people on their way."

    

    window auto hide
    show plo neutral with Dissolve(0.5)
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        linear 0.30 pos (1116, 828) zoom 2.24 
    with Pause(0.40)
    camera:
        pos (1116, 828) zoom 2.24 
    window auto show
    "You barely notice a torchlight reach the tent flap when a massive figure ducks beneath it."
    camera:
        subpixel True 
        pos (1116, 828) 
        linear 0.30 pos (747, 378) 
    with Pause(0.40)
    camera:
        pos (747, 378) 
    "His broad shell scraps the fabric on entrance."
    camera:
        subpixel True 
        pos (747, 378) 
        linear 0.30 pos (1404, 63) 
    with Pause(0.40)
    camera:
        pos (1404, 63) 
    "The figure's weathered brown skin was hardened by time.{cps=4} {/cps}The oil lamps revealed its deep grooves and ridges."
    camera:
        subpixel True 
        pos (1404, 63) zoom 2.24 
        linear 0.30 pos (0, 0) zoom 1.0 
    with Pause(0.40)
    camera:
        pos (0, 0) zoom 1.0 

    show plo angry at jumpAnim
    Plo "{i}Can't let this old man get his sleep after a hard days work?{/i}"

    """
    His heavy-lidded eyes scan the room as if routine then approaches. 
    
    He straightens his thick frame and gives the captain a curt salute.
    """

    show plo neutral
    Plo "Captain."

    Captain "At ease Plo,{cps=4} {/cps}I wouldn't drag you out this late without a good reason."

    $ plo_name = "Plo"

    show plo happy

    "Plo gives a sarcastic snort."

    Plo "{i}Right{/i}."

    show plo neutral

    "Only a second passes before the tent door flutters open once more."

    show plo neutral at Position (xpos = 0.25)

    window auto hide
    show darcey neutral with Dissolve(1.5) 
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        linear 0.30 pos (1278, 1611) zoom 2.79 
    with Pause(0.40)
    camera:
        pos (1278, 1611) zoom 2.79 
    window auto show
    "A short,{cps=4} {/cps}red-skinned tiefling strides in next.{cps=4} {/cps}You swore you feel the air stop at her presence, afraid to move disrespectfully."
    camera:
        subpixel True 
        pos (1278, 1611) 
        linear 0.30 pos (2268, 1070) 
    with Pause(0.40)
    camera:
        pos (2268, 1070) 
    "She approached the desk poised and unwavering.{cps=4} {/cps}She stands at attention."
    camera:
        subpixel True 
        pos (2268, 1070) 
        linear 0.30 pos (2061, 386) 
    with Pause(0.40)
    camera:
        pos (2061, 386) 
    "Her dark eyes flick over the assembled group,{cps=4} {/cps}assessing,{cps=4} {/cps}before settling on the captain with a crisp salute."
    camera:
        subpixel True 
        pos (2061, 386) zoom 2.79 
        linear 0.30 pos (0, 0) zoom 1.0 
    with Pause(0.40)
    camera:
        pos (0, 0) zoom 1.0 



    Darcey "Captain."

    "The final arrival slips inside quickly after.{cps=4} {/cps}The extra shadow against the torchlight is what made you notice."

    show darcey at flip
    show darcey neutral at Position (xpos = 0.31)

    window auto hide
    show quinn happy with Dissolve(1.5) 
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        linear 0.30 pos (1494, 1665) zoom 2.9 
    with Pause(0.40)
    camera:
        pos (1494, 1665) zoom 2.9 
    window auto show
    "He's a lean dark skinned elf whose dark cloak is still dusted from the cave's passage."
    camera:
        subpixel True 
        pos (1494, 1665) 
        linear 0.30 pos (2205, 1026) 
    with Pause(0.40)
    camera:
        pos (2205, 1026) 
    "Glancing between the others,{cps=4} {/cps}he only pauses on the tiefling with a nod of acknowledgment{cps=4} {/cps}before facing the captain."
    camera:
        subpixel True 
        pos (2205, 1026) 
        linear 0.30 pos (1926, 414) 
    with Pause(0.40)
    camera:
        pos (1926, 414) 
    "He offers a salute before speaking."
    camera:
        subpixel True 
        pos (1926, 414) zoom 2.9 
        linear 0.30 pos (0, 0) zoom 1.0 
    with Pause(0.40)
    camera:
        pos (0, 0) zoom 1.0 

    show quinn shocked
    Quinn "Captain. Something urgent,{cps=4} {/cps}I assume?"

    Captain "Darcey,{cps=4} {/cps}Quinn,{cps=4} {/cps}Plo.{cps=4} {/cps}Come in,{cps=4} {/cps}Come in."

    $ darcey_name = "Darcey"
    $ quinn_name = "Quinn"
    show quinn neutral behind darcey at Position (xpos = 0.12) 


    """
    The Captain relaxes then pushes aside papers and pulls out a white letter sealed by a striking red wax stamp.

    A pause.

    He grins,{cps=4} {/cps}a rare grin.
    """

    Captain "This is a very important message that I need delivered.{cps=2} {/cps}You four will be the ones delivering it."

    show plo happy at jumpAnim
    
    Plo "Hah!{cps=4} {/cps}'bout time I get to hauling something a little less explosive!"

    menu:
        "What kind of message?":
            show iris happy
            Captain "I'm glad you asked{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1

        "Why choose us?":
            #TODO: character image changes
            Captain "Plo,{cps=4} {/cps}the best carriage driver we've got.{cps=2} {/cps}He knows how to handle rough terrain—and rougher company."
            show plo happy
            Captain "Quinn,{cps=4} {/cps}a skilled navigator.{cps=2} {/cps}If there's a way through,{cps=4} {/cps}he'll find it."
            show quinn happy
            Captain "Darcey,{cps=4} {/cps}a fighter through and through.{cps=2} {/cps}Deadly for fights you want to pick and intelligent for fights you don't." 
            show darcey happy
            Captain "And of course,{cps=4} {/cps}[player_name],{cps=4} {/cps}the rising star messenger.{cps=2} {/cps}Fast,{cps=4} {/cps}reliable,{cps=4} {/cps}and able to think on their feet."
            show iris happy
            Captain "All excellent in your own rights."
            Captain "You four are the perfect team for this mission because{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1
        
        "Stay Quiet":
            show iris worried
            Captain "I summoned you all here today because{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            $ quiet += 1
            jump continue1
    
    label continue1:
    
    "He displays the letter to the group." 
    
    Captain "The enemy sent us this letter of surrender at sundown."

    show darcey shocked 
    show plo blush at happyAnim
    show quinn shocked 
    show iris shocked
    
    #TODO: character image changes
    Darcey "{i}Gasp{/i}"
    show darcey happy:
        flipRight
        subpixel True 
        xpos 0.31 
        linear 0.30 xpos 0.26 
    with Pause(0.40)
    show quinn happy

    Quinn "At long last{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
    

    Captain "There's still work to be done here,{cps=4} {/cps}but what matters now is to send word to the capital.{cps=4} {/cps}Immediately."

    Captain "That is why i'm entrusting this mission to you,{cps=4} {/cps}[player_name]."

    menu:
        "Yes,{cps=4} {/cps}Captain!":
            show iris happy
            Captain "Good.{cps=2} {/cps}You all are dismissed.{cps=2} {/cps}The others will wake up to good news."
            jump continue2
        
        "Stay Quiet":
            show iris worried
            Captain "......{cps=4} {/cps}Well, get going then!{cps=4} {/cps}I want you all out of here before morning."
            jump continue2
    
    label continue2:

    Iris "Understood,{cps=4} {/cps}captain."

    """
    You turn to your new team, who stare at you with anticipation.

    """
    show darcey happy:
        flipLeft
        subpixel True 
        xpos 0.31 
        linear 0.30 xpos 0.26 
    Iris "Alright!"
    show plo happy
    show iris happy
    Iris "Let's meet at the camp entrance in 5 hours."
    show iris:
        flipRight 
        exitRight with Pause(0.40)

    scene black with dissolve

    """
    You make your way back to your home tent.
    
    It's an uncomfortable warmth that you've gotten used to. Thick with humidity. Exhaustion seems to stick to you in the same way as you walk.
    """ 

    scene tent with Dissolve(1.5)

    #TODO: pan around the tent bg
    """
    
    Inside the soldier's tent, a thick layer of grime made up of sweat and dirt sticks to the occupants.

    Half a dozen exhausted soldiers lay cramped like sardines in haphazardly built bunk beds.
    
    The canvas walls do little to shield you from the environment outside. 
    
    A single lantern,{cps=4} {/cps}its flame weak and flickering,{cps=4} {/cps}casts shadows along the tent's sagging ceiling.

    This was the life of a conscripted solider.
    
    The few still awake glance up as you return.
    """

    show iris neutral at Close

    Bunkmate "What was that about? You get in trouble?"

    "Your bunkmate above you shifts to eye you inquisitively."

    menu:
        "Be honest":
            show iris happy at happyAnim
            Iris "Actually,{cps=4} {/cps}I have great news!"
            "You lean in,{cps=4} {/cps}lowering your voice so as not to wake anyone."
            show iris happy at VeryClose
            Iris "The Captain will announce the end of the war in the morning."
            "They nearly shout before clapping both hands over their mouth."
            Iris "Shh,{cps=4} {/cps}I have to pack{cps=4}—{/cps}I'm leaving before sunrise"
            show iris blush at Close
            Bunkmate "I can't believe it will be over; THIS will be over.{cps=4} {/cps}I'm not going to be able to sleep tonight."
            jump continue3

        "Joke around":
            show iris sad
            Iris "3 days night shift duty for me."
            Bunkmate "Man, that sucks."
            "You chuckle."
            show iris happy
            Iris "Joking."
            Iris "It was about a mission.{cps=4} {/cps}You will hear about it in the morning~"
            Bunkmate "Hmph{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Guess I'll wait."
            jump continue3
        
        "Be evasive":
            Iris "I got assigned a mission.{cps=2} {/cps} I leave before sunrise."
            Bunkmate "Hmph{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Guess I'll wait."
            jump continue3
    
    label continue3:

    """
    
    After checking that no one is spying, You take a moment to look at the map the Captain entrusted to you.

    """
    show map

    """

    The ideal trip to the capital would be to cut through the mountain path.

    Three days,{cps=4} {/cps}maybe less if you're quick.

    We'd need to pack enough food and supplies for at least twice that. For four people.
    """
    hide map
    show iris happy
    """

    Quietly you reach under the bunk to pull out your stuff.

    """

    ##TODO: show inventory packing here!!! ##

    

    """
    You decide to sleep, getting what little rest you still can.
    """
    
################################################################################
## █▀▄ ▄▀▄ ▀▄▀   █▀█ █▄ █ █▀▀
## █▄▀ █▀█  █    █▄█ █ ▀█ ██▄
################################################################################

######################
## in cave
######################
    label DayOne:
   
    scene black with Dissolve(1.5)
   
    centered "Day 1"
   
    """
    Sunrise hasn't hit yet as you make your way to the designated meeting spot.


    Soldiers move about groggily. The night shift returns for some needed sleep as{cps=4} {/cps}the day shift gets ready to work.


    """
    scene cave with Dissolve(1.5)

    show iris happy:
        right
        flip


    """
    You meet your party near the supply tent{cps=4} {/cps}where a wooden carriage{cps=4} {/cps}tied to a sturdy draft horse{cps=4} {/cps}stands ready.


    A cold chill blows into the cave,{cps=4} {/cps}bringing the smell of rain and mud. You wish nature was more merciful.


    Plo secures the last of the crates onto the back of the carriage.
    """


    show plo happy at MoveToLeft
   
    Plo "Cart's packed and ready.{cps=2} {/cps}Not much,{cps=4} {/cps}but it'll get us there."


    show quinn neutral at left


    Quinn "The rain looks intense."


    show quinn sad
    show iris neutral


    Quinn "At this rate, our journey might be hindered by the mud."


    show plo happy at jumpAnim
    show quinn neutral
    show iris happy


    Plo "A little rain won't bother me."


    Plo "I'll be driving that carriage even if it's blizzardin'."

    show darcey happy:
        yanchor 1.0
        ypos 1.0
        xpos 2.0
        linear 1.50 xpos 0.49

    "Darcey approaches,{cps=4} {/cps}a bag in hand and a dignified smirk on her face."

    show quinn happy
    show darcey happy

    Darcey "Try not to get us stuck in a ditch,{cps=4} {/cps}alright?"


    show plo angry


    Plo "As if {i}you{/i} would handle it any better."

    show plo happy at happyAnim

    Plo "Maybe a little rain would put out your fire-like temper."


    show darcey angry

    Darcey "Hey,{cps=4} {/cps}I'd have us halfway there already if I was in charge."

    
    show quinn happy at happyAnim

    Quinn "Halfway down a ravine maybe,{cps=4} {/cps}I don't seem to recall you ever driving a carriage before..."

    show darcey neutral
    show quinn neutral
    Darcey "You're supposed to have {i}my{/i} back here."


    menu:
        "Joke around":
            show darcey neutral behind iris
            Iris "You are all acting like we're headed into a storm of drama."
            Iris "Let's just {i}wheel{/i} ourselves together and {i}carriage{/i} on."
            show plo shocked
            show darcey worried
            show quinn happy
            "Plo blinks. Darcey groans. Quinn hides a smirk."
            show darcey worried
            Darcey "That was terrible."
            Iris "You're just jealous you didn't think of it first."
            show plo neutral
            show darcey neutral
            Plo "Guess we better roll out before Iris hits us with another one."
            show plo neutral:
                flip
                subpixel True 
                xpos 0.1 
                linear 0.30 xpos -0.47 
            with Pause(0.40)
            show plo neutral:
                xpos -0.47 
            $ quinn_points += 5
            $ darcey_points += 5
            $ plo_points += 5
            jump continue4


        "It's time to get serious":
            show darcey angry behind iris
            show iris neutral
            Iris "We don't have time for this,{cps=4} {/cps}guys."
            show darcey angry
            show plo neutral
            show quinn neutral
            Iris "The lives of many people rely on this letter being delivered."
            show darcey sad
            Darcey "Apologies,{cps=4} {/cps}[player_name]."
            "Darcey looks embarrassed of her unknightly behavior."
            show plo worried
            Plo "I'm just going to finish packing then..."
            show plo worried at flip
            $ quinn_points += 3
            show plo neutral:
                subpixel True 
                xpos 0.1 
                linear 0.30 xpos -0.47 
            with Pause(0.40)
            show plo neutral:
                xpos -0.47 
            $ plo_points -= 3
            $ get_serious = True
            show darcey neutral
            jump continue4


        "Say nothing":
            show iris neutral
            $ quiet += 1
            Plo "I'm just going to finish packing then..."
            show plo worried at flip
            $ quinn_points += 3
            show plo neutral:
                subpixel True 
                xpos 0.1 
                linear 0.30 xpos -0.47 
            with Pause(0.40)
            show plo neutral:
                xpos -0.47 
            jump continue4
   
    label continue4:


    """
    The conversation dies off as the sound of rain tapping against the heavy stone of the cave grows louder.


    Quinn's eyes narrow slightly at the sight of the road ahead.
    """


    show quinn sad
    Quinn "The weather will only get worse if we wait."

    show quinn neutral
    show iris neutral
    Quinn "We shouldn't waste any more time."

    show iris happy
    Iris "Alright,{cps=4} {/cps}everybody.{cps=2} {/cps}Let's get this letter on the road."

    Iris "Mount up."


    """
    Plo packs the final crate and secures the latch on the carriage.

    Darcey and Quinn enter the carriage.
    """

    show darcey neutral:
            subpixel True 
            xpos 0.1 
            linear 0.30 xpos -0.47 
    show quinn neutral:
            subpixel True 
            xpos 0.1 
            linear 0.30 xpos -0.21 



    """


    Quinn props the door open and faces you with respect.
   
    """
   
    Quinn "After you,{cps=4} {/cps}[player_name]."


    menu:
        "Sit inside":
            Iris "Thank you, Quinn."
            window auto hide
            show iris happy:
                subpixel True 
                parallel:
                    'iris happy'
                    0.30
                    'iris happy' with dissolve
                parallel:
                    xpos 1.0 
                    linear 0.30 xpos 0.12 
            with Pause(0.90)
            show iris happy:
                xpos 0.12 
            $ quinn_points += 5
            $ darcey_points += 5
            $ inside_carriage = True
            jump InsideCarriage


        "Guard outside":
            "[player_name] waves their hand at Quinn."
            Iris "No need,{cps=4} {/cps}I'll help guard outside alongside Plo."
            Quinn "As you wish."
            show quinn neutral:
                flip
                subpixel True 
                linear 0.30 xpos -0.47 
            "Quinn shuts the door behind them."
            $ inside_carriage = False
            $ plo_points += 5
            jump OutsideCarriage
     
######################
## inside carriage
######################
    label InsideCarriage:


    scene carriage with Dissolve(1.5)


    """
    You climb into the carriage,{cps=4} {/cps}settling on the slightly worn wooden seat.


    The inside is dim without the presence of an oil lamp.{cps=4} {/cps}You can hear the muffled voice of rain hitting the canvas roof.
    """


    show quinn neutral:
        left
        Close
        subpixel True pos (-0.2, 1.54) 
    show darcey neutral:
        right
        Close
        subpixel True pos (1.0, 1.58) 
    with Dissolve(1.5)

    Darcey "So,{cps=4} {/cps}[player_name]{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} Got any words of wisdom before we roll out?"
    menu:
        "Keep it lighthearted":
            Iris "Try not to kill each other before we get there."  
            show darcey happy
            show quinn happy
            "Darcey laughs,{cps=4} {/cps}while Quinn gives a small,{cps=4} {/cps}knowing smile."
            show darcey blush  
            Darcey "I'll be on my best behavior from here on out."
            Quinn "I bet so."
            $ darcey_points += 5
            $ quinn_points += 3


        "Be serious":
            Iris "Stay focused.{cps=4} {/cps}Stay alert.{cps=4} {/cps}Distractions can't delay us."  
            """
            Darcey smiles,{cps=4} {/cps}appreciating the knowledgeable advice.
           
            Quinn gives a small nod of approval.
            """
            show quinn happy
            Quinn "Understood."  
            show darcey blush
            Darcey "I'll be on my best behavior from here on out."
            $ darcey_points += 2
            $ quinn_points += 5

    pause(1.5)
    "Time passes in silence."
    pause(1.5)
    "You feel the carriage jolt around softly as you depart."



    menu:
        "Ask Quinn about the path ahead":  
            label path:
            $ quinn_points += 5
            show darcey happy
            Iris "What's the terrain like ahead?"
            show quinn neutral
            Quinn "Rough.{cps=4} {/cps}Once we're out of the mud,{cps=4} {/cps}we'll hit gravel.{cps=4} {/cps}It'll even out once we hit the main road."  
            show darcey neutral
            "Darcey sighs."
            Darcey "Let's hope Plo is as skilled as he brags he is."
            jump continue5


        "Ask about Darcey and Plo":
            Iris "What's the deal between you and Plo?"
            show quinn neutral
            show darcey neutral
            "Darcey sighs,{cps=4} {/cps}lowering her voice to a whisper."
            show darcey angry
            Darcey "Let's just say you'd be wrong to expect him to be a model soldier."
            show darcey neutral
            Darcey "Plo's not the kind of person who thinks of the consequences before he acts."
            show quinn angry
            "Quinn hits her softly with his elbow."
            Quinn "He has a good heart when it matters."
            show darcey blush
            show quinn neutral
            jump continue5


        "Sit Quietly":  
            show quinn neutral
            show darcey neutral
            
            "You settle back,{cps=4} {/cps}listening to the sound of the rain."
            pause(1.5)

            "Quinn's eyes remain half-lidded as Darcey hums softly under her breath."
            pause(1.5)

            "The rhythmic sway of the carriage mixes with the patter of rain to create a drowsy sort of calm."
            pause(1.5)
            show quinn happy
            Quinn "Something on your mind,{cps=4} {/cps}[player_name]?"
            menu:
                "Ask about path ahead.":
                    jump path

                "Nothing.":
                    Iris "Nothing much..."
                    show quinn neutral


                    if quiet >= 2:
                        show darcey neutral
                        "Darcey studies you for a moment,{cps=4} {/cps}her gaze steady but not probing." 
                        Darcey "You don't talk much,{cps=4} {/cps}do you?"
                        menu:
                            "I'm not much of a talker.":
                                Iris "I'm more of a listener."  
                                show darcey happy
                                Darcey "Listeners are valuable too."
                                show darcey neutral
                                "Darcey's gaze moves toward the window."
                                $ darcey_points += 5
                                jump continue5


                            "Say nothing.":
                                show darcey happy
                                Darcey "Pfft."
                                $ quinn_points += 5  
                                $ darcey_points += 5
                                jump continue5  
                    else:
                        show quinn neutral
                        Quinn "Alright."
                        "Quinn studies you for a moment,{cps=4} {/cps}his gaze steady but not probing."
                        jump continue5
                    jump continue5
    label continue5:


    "A comfortable silence dawns on you and your party as the carriage rocks gently beneath you."

    show darcey happy
    Darcey "So,{cps=4} {/cps}what do you think about-"
    show darcey shocked:
        jumpAnim
        subpixel True pos (1.0, 1.58)
    show quinn shocked:
        jumpAnim
        subpixel True pos (-0.2, 1.54) 
    with vpunch


    """
    The carriage lurches forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.


    You hear a horse's annoyed neigh from outside.
    """

    show darcey angry

    Darcey "Damnit,{cps=4} {/cps}I knew he would."
   
    Iris "That does not sound good..."


    "You,{cps=4} {/cps}Quinn,{cps=4} {/cps}and Darcey make your way out of the carriage."


    scene forest 
    show rain1fast zorder 1
    show rain2fast zorder 0

    show plo neutral:
        right
        flip
    show iris worried:
        right
        flip
    with Dissolve(1.5)
    pause(1.0)
    
    window auto hide
    show quinn shocked at left:
        subpixel True 
        xpos -0.47 
        linear 0.49 xpos -0.02 
    show darcey angry at left:
        flip
        subpixel True 
        xpos -0.3 
        linear 0.52 xpos -0.03 
    with Pause(0.52)
    show quinn shocked:
        xpos -0.02 
    show darcey angry:
        xpos -0.03 
    window auto show


    Iris "Plo,{cps=4} {/cps}are you alright?"

    show plo angry


    Plo "I am,{cps=4} {/cps}but I can't say the same for the carriage."


    "You see one of the carriage's wheels was stuck in the mud."

    jump WheelInMud


######################
## outside carriage
######################
    label OutsideCarriage:

    scene forest with Dissolve(1.5)
    
    show rain1fast zorder 1
    show rain2fast zorder 0

    """
    The steady patter of rain against the carriage's canopy mingles with the sound of the horse's hooves stomping through the wet mud.


    Moisture from the air sticks to you; the rain helps it drip down your collar.
    """

    show plo neutral at left:
        subpixel True pos (0.0, 1.6) xzoom 1.0 zoom 1.56 



    "Plo sits at the front,{cps=4} {/cps}reins loose in his hands and{cps=4} {/cps}eyes half-lidded as he watches the road ahead."


    "You sit next to him in peaceful silence as the party makes its way through the thick forest."

    show plo angry

    Plo "Rain's picking up."

    menu:
        "Make small talk.":
            $ plo_points += 5
            Iris "The weather only gets better for us."
            show plo happy
            Plo "Haha!"
            show plo neutral
            Plo "It is actually quite nice for tortle folk like myself."
            show plo blush
            Plo "Keeps the shell from drying out."
            Iris "Is that so?"  
            show plo neutral
            "Plo grunts in approval."
            Plo "Nothing worse than an itchy shell."  
            show plo happy
            "Plo flashes you a smile before focusing back on the road."  
            Iris "And here I thought you were going to be miserable out here."  
            show plo neutral
            Plo "Eh, only if it were sunny. It's the heat that's the problem."  
            "A second of silence passes before Plo's face scrunches."
            show plo angry
            Plo "That... and sand."  
            Iris "Sand?"  
            show plo neutral
            Plo "It gets {i}everywhere{/i}."  
            jump continue8


        "Talk about the mission.":
            Iris "Did you pack everything you needed for the mission last night?"
            show plo angry
            Plo "Barely had any time,{cps=4} {/cps}so I just packed the essentials."
            show plo neutral
            Plo "Here,{cps=4} {/cps}take a look if you are so curious."
            "He takes his bag and tosses it onto your lap."
            ##the joke is that his inventory is filled with junk, ill make a graphic for this
            show jokeinventory
            "..."
            hide jokeinventory
            menu:
                "Praise his packing skills":
                    Iris "You... really thought of everything."
                    Iris "How did you even get all that to fit in there?"  
                    show plo blush
                    Plo "The amount of supply runs i've gone on you pick up some things."
                    show plo happy
                    Plo "You get to know whats {i}really{/i} essential."
                    $ plo_points += 3
                    jump continue8


                "Question his choices":
                    Iris "I'm not sure a lot of that is necessary..."
                    show plo angry
                    Plo "Hmph."
                    show plo neutral
                    Plo "What would a human know about packing anyway."
                    $ plo_points -= 3
                    jump continue8


    label continue8:


    "Plo's eyes remain scanning the muddy road ahead."
    pause(1.5)

    "A comfortable silence dawns on you and your party as the carriage rocks gently beneath you."
    pause(1.5)

    "The road begins to narrow as the mud deepens beneath the horse's hooves."  

    show plo angry


    Plo "The road is getting bad{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} I'm afraid one of the carriage wheels is going to-"
    show plo shocked
    with vpunch


    """
    The carriage lurches forward, almost knocking you out of the seat before stopping just as quickly.


    The horse strapped to the vehicle lets out an annoyed whine while stomping its feet.
    """


    Plo "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Get stuck in the mud."


    show plo angry


    Plo "Great. Just great."  
   
    "You hear a muffled voice from inside the carriage"


    Darcey "Damnit,{cps=4} {/cps}I knew he would."


    
    "Plo groans,{cps=4} {/cps}jumping down and already stepping toward the wheel."
    show plo neutral at jumpAnim

    scene forest 
    show rain1fast zorder 1
    show rain2fast zorder 0
    
    show plo neutral:
        right
        flip
    show iris worried:
        right
        flip
    with Dissolve(1.5)
    pause(1.0)
    
    window auto hide
    show quinn shocked at left:
        subpixel True 
        xpos -0.47 
        linear 0.49 xpos -0.02 
    show darcey angry at left:
        flip
        subpixel True 
        xpos -0.3 
        linear 0.52 xpos -0.03 
    with Pause(0.52)
    show quinn shocked:
        xpos -0.02 
    show darcey angry:
        xpos -0.03 
    window auto show
   
    "Quinn and Darcey quickly emerge from the carriage,{cps=4} {/cps}the former worried and the latter annoyed."

    Quinn "[player_name],{cps=4} {/cps}Plo,{cps=4} {/cps}are you alright?"
    show quinn neutral
    show iris sad

    Iris "We are fine,{cps=4} {/cps}a wheel got stuck in the mud."

    jump WheelInMud


######################
## wheel in mud
######################    
    label WheelInMud:


    """

    The rain continues to patter against the leaves as the carriage is stuck on the muddy path.


    The party finds themselves past a winding road, precariously close to a steep drop.
    """


    show darcey neutral
    show quinn neutral


    Darcey "Figures."

    show plo angry

    show iris neutral
       
    Iris "Plo,{cps=4} {/cps}how long will this take to fix?"

    show plo neutral

    "Plo waves away the concern."

    Plo "Nothing I can't fix,{cps=4} {/cps}just give me a min' I got just the thing."



    if get_serious == False:
        show darcey angry
        Darcey "If you had things under control, it wouldn't have gotten stuck!"
        show plo angry
        Plo "I didn't magick us to leave in the deludge!"
        show darcey neutral
        Darcey "You could have planned to keep us on the road!"
        show plo neutral:
            jumpAnim
        Plo "Excuse me if the storm makes it hard for comfort. I'm a turtle not a rain bug!"
        show plo angry
        "Plo points at the cliffs edge without losing Darcey's eye contact."
        Plo "If you had the reins, we'd be down the ravine!"
        show iris shocked:
            jumpAnim
        Iris "Guys,{cps=4} {/cps}enough{cps=4}!"
        show iris happy
        Iris "This situation isn't ideal, but arguing and placing blame won't unstick the wheel. Besides, think of this as a chance to bond."
        show quinn happy
        show plo neutral
        Plo "Bond, eh?"
        "Plo looks back at Darcey."
        show plo happy
        "You should go push the stuck wheel out from the mud. It'll help our bond."
        show darcey happy
        Darcey "Sure, we wouldn't want the senior to pull something."
        show iris neutral
        "Iris calls for Darcey from behind the carriage."
        show quinn neutral
        show darcey neutral
        Darcey "As you wish,{cps=4} {/cps}[player_name]."
        show darcey angry
        "As Darcey turns to go, she gives Plo one last dirty look. He's too busy grinning."
        show darcey neutral
    else:
        Iris "Darcey, let's get behind and help push."
        show darcey angry
        "Darcey's anger, though strong, only appears for a brief second before being subdued."
        show darcey neutral
        Darcey "As you wish,{cps=4} {/cps}[player_name]."
        show darcey neutral



    show plo neutral:
        unflip
    Plo "Let's get this carriage back on the road then."
    window auto hide
    show quinn neutral:
        subpixel True 
        xpos -0.02 
        linear 0.70 xpos 0.41 
    show darcey angry:
        subpixel True 
        xpos -0.03 
        linear 0.60 xpos 1.08 
    with Pause(0.80)
    show quinn neutral:
        xpos 0.41 
    show darcey angry:
        xpos 1.08 
    window auto show
    Quinn "Iris,{cps=4} {/cps}a moment please."
    show quinn sad


    menu:
        "Stay and help Plo.":
            $ plo_points += 5
            show iris neutral
            Iris "I'm sorry, Quinn, but we have pressing matters here."
            Quinn "I understand."
            "Quinn nods then heads off towards the forest line."
            "Iris approaches Plo ready to help in the front. Plo's hand stops her."
            Plo "We are fine,{cps=4} {/cps}[player_name]. Go see what the kid needs."
            show plo happy
            Plo "Darcey and I have this handled."
            
            show plo neutral:
                subpixel True 
                xpos 1.0 
                linear 0.28 xpos 1.47 
            with Pause(0.40)
            show plo angry:
                xpos 1.47 
            "With Plo's reassurance, you make your way over to the forest where Quinn waits."
            jump continue9


        "Go and see what Quinn wants at the perimeter.":
            $ quinn_points += 3
            "Concern distorted Quinn's face to your worry."
            Iris "Plo, Darcey, work on getting this carriage free while Quinn and I check the perimeter."
            show plo happy
            Plo "Roger, Sergeant."
            show plo neutral:
                subpixel True 
                xpos 1.0 
                linear 0.28 xpos 1.47 
            with Pause(0.40)
            show plo angry:
                xpos 1.47 
            show iris happy
            Iris "No fighting."
            "Quinn leds you to the forest line."
            show iris neutral
            Iris "What's the matter?"
            jump continue9
           
           


    label continue9:    
    window auto hide
    show iris neutral:
        flip
        subpixel True 
        xpos 1.0 
        linear 0.38 xpos 0.59 
    show quinn neutral:
        flip
        subpixel True 
        xpos 0.41 
        linear 0.30 xpos -0.0 
    with Pause(0.48)
    show iris neutral:
        xpos 0.59 
    show quinn neutral:
        xpos -0.0 
    window auto show

    show quinn neutral
    Quinn "As I was securing the area, I found these."
    show quinn sad
    
    "Quinn points at the mud below."
    #i will make this graphic too :D -perry
    show footprints
    """
    A series of deep footprints press into the mud. They remain distinct despite the rain.
   
    They're unevenness suggests that the owner of the prints was moving quickly.
    """

    Quinn "Fresh. I have never seen any footprint pattern like this from our camp."
    hide footprints


    "You take a sharp breath. Plo and Darcey's distant bickering muffles in the rain."


    show iris worried
    Iris "This can't be right... Nothing should be out here for miles. We're still close to the base."


    menu:
        "We should investigate.":
            show iris worried
            Iris "We need to investigate. Enemy soldiers have never been this close to base before."
            Iris "Something isn't right."
            $ quinn_points += 10
            jump Investigate


        "We can't stray from our given task.":
            show iris worried
            Iris "It is concerning but..."
            show iris neutral
            Iris "We don't know how far the enemy went or what direction. Getting the letter to the castle is more important than a wild goose chase."
            Iris "Right now, we need to get the carriage back on the road."
            jump DontInvestigate


######################
## investigate
######################  
    label Investigate:


    show quinn sad
    Quinn "If someone passed through here recently,{cps=4} {/cps}they might still be nearby."
   
    menu:
        "They could be up to no good.":
            show iris sad
            Iris "We should find them quickly, no good comes from them sneaking around the camp."
            show iris neutral
            jump continue11


        "They could be in trouble.":
            show iris sad
            Iris "The war has ended, what if they need our help?"
            show iris neutral
            show quinn worried
            Quinn "Either way, we need to be careful.{cps=4} {/cps}If these tracks belong to an enemy scout we can't afford to ignore them."
            show quinn neutral
            jump continue11


    label continue11:

    "You head back over to the carriage,{cps=4} {/cps}seeing darcey and plo working together to free the wheels."

    
    window auto hide
    show plo angry at right:
        subpixel True 
        xpos 1.46 
        linear 0.28 xpos 0.98 
    show iris neutral:
        unflip
        subpixel True 
        xpos 0.59 
        linear 0.30 xpos 0.59 
    show quinn neutral behind iris:
        unflip
        subpixel True 
        xpos 0.0 
        linear 0.22 xpos 0.03 
    show darcey angry at right:
        subpixel True 
        xpos 1.3 
        linear 0.28 xpos 0.93 
    with Pause(0.40)
    window auto show

    Plo "That's it!"

    Plo "Push!"

    
    show iris happy
    show plo neutral:
        jumpAnim
    show darcey angry:
        subpixel True 
        xpos 0.93 
        linear 0.08 xpos 0.98 
        jumpAnim
    with Pause(0.18)
    with hpunch

    "The carriage jolts forward,{cps=4} {/cps}freeing it from the mud."

    

    "The sudden momentum nearly sends Darcey stumbling forward,{cps=4} {/cps}but she steadies herself with a muttered curse."


    show darcey angry
    Darcey "Finally.{cps=4} {/cps}Couldn't have been {i}any{/i} gentler?"

    show plo happy
    Plo "We were getting it unstuck, not giving it a massage."

    show quinn sad
    "Despite the small victory,{cps=4} {/cps}Quinn remains still,{cps=4} {/cps}his sharp gaze lingering on the treeline.{cps=4} {/cps}He doesn't look at the freed carriage—only at the shadows shifting between the trees."


    show iris neutral
    "Iris follows his line of sight, frowning."


    show iris worried
    Iris "We found a set of footprints I want us to go inspect."

    show darcey worried:
        unflip
        subpixel True 
        xpos 0.98 
        linear 0.30 xpos 0.86 
    with Pause(0.40)
    "Darcey glances at Quinn,{cps=4} {/cps}then at the darkened forest,{cps=4} {/cps}her expression shifting from irritation to something more serious."

    Darcey "Footprints?{cps=4} {/cps}Out here?{cps=4} {/cps}Thought we were the only ones stupid enough to take this route."

    show plo worried:
        flip
    Plo "They fresh?"

    show quinn neutral
    Quinn "Fresh enough.{cps=4} {/cps}And not from our camp."

    "A quiet moment passes as the rain patters against the leaves,{cps=4} {/cps}the wind making them sway.{cps=4} {/cps}The weight of the unknown settles over the group."

    show plo worried
    Plo "I don't like this."

    show iris worried
    Iris "The sooner we move, the sooner we get answers."

    show quinn sad
    Quinn "The rain's picking up.{cps=4} {/cps}If we're going to follow those tracks,{cps=4} {/cps}we need to move now before they are washed away."

    show iris neutral
    Iris "Right.{cps=4} {/cps}Everyone stay alert."

    show plo 
    Plo "I'll stay back then, someone has to keep watch of all the supplies."

    Iris "Alright, stay safe [plo_name]."

    
    window auto hide
    show quinn worried:
        flip
        subpixel True 
        xpos 0.03 
        linear 0.18 xpos -0.46 
    show iris worried:
        flip
        subpixel True 
        xpos 0.59 
        linear 0.23 xpos -0.03 
    show darcey worried:
        subpixel True 
        xpos 0.86 
        linear 0.30 xpos 0.0 
    with Pause(0.90)

######################
## vine monster attack
######################  
    scene forest 
    show rain1fast zorder 1
    show rain2fast zorder 0
    with Dissolve(1.5)

    "The forest is thick with mist,{cps=4} {/cps}the scent of damp wood clinging to the air." 
    "The footprints weave between the trees,{cps=4} {/cps}leading deeper off the main road."
    "The air feels heavier and the silence is broken only by distant rustlings of rain drops."

    show darcey neutral at right 
    show quinn neutral at left
    show iris neutral at right:
        subpixel True xpos 0.73 
    with Dissolve(1.5)

    show darcey worried
    Darcey "Something doesn't feel right{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} These tracks are too scattered."

    show quinn sad
    Quinn "It appears that whoever the tracks belong to was running."


    show iris worried
    Iris "Injured,{cps=4} {/cps}maybe?{cps=4} {/cps}Or running from something."

    "You continue onward."
    
    "A sudden gust of wind sends raindrops falling from the leaves above,{cps=4} {/cps}making the underbrush shudder.{cps=4} {/cps}Up ahead,{cps=4} {/cps}the path opens into a small clearing."

    "A broken-down carriage sits in the middle."

    "The wooden frame is cracked,{cps=4} {/cps}as if something struck it with force."

    "Pieces of torn cloth and scattered supplies litter the ground."


    show iris shocked
    show darcey shocked
    Iris "Well,{cps=4} {/cps}that's not a good sign."


    "Quinn approaches the carriage."


    show quinn neutral
    show darcey neutral
    Quinn "Nothing left. Someone was here recently."


    "You crouch near the carriage,{cps=4} {/cps}running your fingers along a deep gash in the wood.{cps=4} {/cps}Not just weather damage—this was cut."
    show iris neutral
    menu:
        "Check inside the carriage.":
            "Carefully,{cps=4} {/cps}you step onto the cracked wooden frame,{cps=4} {/cps}peering inside."

            "The seats are torn,{cps=4} {/cps}papers and bags left in disarray.{cps=4} {/cps}A faint smear of blood stains the side of the door."

            show darcey neutral
            Darcey "How did they manage to get a carriage this far off the path anyway?"

            jump inspect


        "Search the scattered supplies.":
            "You kneel,{cps=4} {/cps}sifting through the debris."
            "A torn bag reveals rations,{cps=4} {/cps}a broken lantern,{cps=4} {/cps}and a necklace with a strange emblem carved into its gem."


            show iris shocked
            Iris "This symbol{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} Quinn, does this look familiar?"


            show quinn shocked
            Quinn "It does.{cps=4} {/cps}It confirms our suspicions."
            show quinn neutral
            show iris neutral
            Quinn "This carriage belonged to the enemy soldiers."

            menu:
                "Pick up the necklace":
                    "Maybe this could be of use if I have room in my bag."
                    #TODO: something here to get the item
                "Leave the necklace":
                    "What use is an enemy necklace anyway."
            jump inspect
   
    label inspect:

    "You go off to inspect the surrounding area for more clues."

    show quinn worried

    Quinn "Something is off.{cps=4} {/cps}I don't recognize this foliage."

    "Darcey approaches,{cps=4} {/cps}poking around with her spear."
    show iris neutral behind darcey:
        flip
    show darcey shocked:
        subpixel True 
        xpos 1.0 
        linear 0.13 xpos 0.52 
    with Pause(0.23)

    show darcey worried

    Darcey "Strange,{cps=4} {/cps}thought there wasn't a single blade of grass you couldn't identify this side of the mountain."

    show darcey neutral
    "She stabs through the leaf with her spear."


    "A rustling sound echoes through the trees,{cps=4} {/cps}followed by a sudden sharp {i}snap{/i}."

    show darcey shocked
    Darcey "What the—?!"
    show vine2 at CutIn
    pause(1.0)
    show vine2 at CutOut
    pause(0.5)
    hide vine2
    
    window auto hide
    show darcey shocked:
        subpixel True 
        parallel:
            xpos 0.65 
            linear 0.10 xpos 0.64 
            linear 0.13 xpos 0.72 
            linear 0.01 xpos 0.74 
            linear 0.10 xpos 1.02 
            linear 0.13 xpos 1.14 
            linear 0.08 xpos 1.2 
            linear 0.05 xpos 1.12 
        parallel:
            ypos 1.07 rotate 0.0 
            linear 0.10 ypos 1.11 rotate -9.0 
            linear 0.14 ypos 1.23 rotate -27.0 
            linear 0.10 ypos 1.32 rotate -45.0 
            linear 0.13 ypos 1.21 rotate -108.0 
            linear 0.08 ypos 0.83 rotate -153.0 
            linear 0.05 ypos 0.73 rotate -180.0 
    with Pause(0.70)
    with vpunch
    with vpunch
    with vpunch
    show darcey shocked:
        pos (1.12, 0.73) rotate -180.0 
    window auto show
    show iris shocked:
        unflip
    show quinn shocked
    



    "Before anyone can react,{cps=4} {/cps}thick,{cps=4} {/cps}gnarled vines burst from the underbrush,{cps=4} {/cps}wrapping around Darcey's leg and yanking her off her feet."


 
    show darcey angry
    Darcey "Son of a—!"  
    Darcey "Get this thing off me!"


    "The vine tightens,{cps=4} {/cps}dragging her toward the dark mass of writhing roots deeper in the clearing.{cps=4} {/cps}The ground shifts—something huge is moving beneath the mud."


    show quinn sad at jumpAnim
    Quinn "Damnit!{cps=4} {/cps}It's a hydra vine!"

    show iris angry
    Iris "Hold on,{cps=4} {/cps}Darcey!"
    show quinn angry
    show arrow1 at CutIn
    with vpunch
    pause(0.5)
    show arrow1 at CutOut
    pause(0.25)
    hide arrow1
    pause(0.25)
    show vine1 at CutIn
    with vpunch
    pause(0.5)
    show vine1 at CutOut
    pause(0.25)
    hide vine1
    "Quinn shoots his bow,{cps=4} {/cps}the plant flings the arrow away."

    show sword1 at CutIn
    with vpunch
    pause(0.5)
    show sword1 at CutOut
    pause(0.25)
    hide sword1

    show darcey angry:
        subpixel True 
        parallel:
            xpos 1.12 
            linear 0.14 xpos 1.13 
            linear 0.08 xpos 1.14 
        parallel:
            ypos 0.73 
            linear 0.18 ypos 0.74 
        parallel:
            rotate -180.0 
            linear 0.12 rotate -180.0 
            linear 0.06 rotate -193.5 
            linear 0.02 rotate -198.0 
            linear 0.10 rotate -180.0 
    with Pause(0.40)

    "Darcey struggles,{cps=4} {/cps}hacking at the vine with her knife,{cps=4} {/cps}but the blade barely cuts through the thick pulsing roots.{cps=4} {/cps}The more she fights,{cps=4} {/cps}the tighter it coils."

    show iris worried
    Iris "I have to do something!"


    menu:
        "Use the dagger to cut her free.":
            "You lunge forward,{cps=4} {/cps}grabbing the nearest sharp object—a dagger, a shard of wood, anything—and hack at the vine gripping her leg."

            show sword1 at CutIn
            with vpunch
            pause(0.5)
            show sword1 at CutOut
            pause(0.25)
            hide sword1

            "The plant lets out a horrible,{cps=4} {/cps}guttural {i}groan{/i} as sap sprays from the wound,{cps=4} {/cps}but the vine doesn't loosen."

            show vine2 at CutIn
            with vpunch
            pause(0.5)
            show vine2 at CutOut
            pause(0.25)
            hide vine2
            "Instead where the plant was cut two more vine-like appendages emerge."

            menu:
                "Keep cutting anyway.":
                    "You grit your teeth and keep hacking as the vines writhe,{cps=4} {/cps}one of them wrapping around your wrist."

                    show sword2 at CutIn
                    with vpunch
                    pause(0.5)
                    show sword2 at CutOut
                    pause(0.25)
                    hide sword2

                    "It burns where it touches—acidic sap touches your skin."

                    "Darcey screams as she's yanked deeper,{cps=4} {/cps}halfway inside the plant's writhing mass."

                    show iris shocked
                    Iris "No—no no no!"

                    "Quinn rushes in,{cps=4} {/cps}but it's too late.{cps=4} {/cps}The vines constrict with a sickening {i}snap{/i}."

                    jump bad_ending

                "Call for help instead.":
                    "You back off,{cps=4} {/cps}shouting for Quinn."

                    Iris "It keeps regenerating!"

                    "Quinn fires another arrow,{cps=4} {/cps}but the creature adapts its vines twist midair,{cps=4} {/cps}using Darcey as a shield."

                    show arrow1 at CutIn
                    with vpunch
                    pause(0.5)
                    show arrow1 at CutOut
                    pause(0.25)
                    hide arrow1
                    pause(0.25)

                    show darcey angry:
                        subpixel True 
                        parallel:
                            xpos 1.12 
                            linear 0.14 xpos 1.13 
                            linear 0.08 xpos 1.14 
                        parallel:
                            ypos 0.73 
                            linear 0.18 ypos 0.74 
                        parallel:
                            rotate -180.0 
                            linear 0.12 rotate -180.0 
                            linear 0.06 rotate -193.5 
                            linear 0.02 rotate -198.0 
                            linear 0.10 rotate -180.0 
                    with Pause(0.40)

                    Quinn "I can't get a good angle on it."

                    Quinn "Fire!{cps=4} {/cps}It's weak to fire!"

                    #if
                    #you have fire starter good 

                    "You remember packing a fire starter in your bag earlier,{cps=4} {/cps}you take it out and toss it to Quinn."

                    Iris "Quinn,{cps=4} {/cps}use this!"

                    "Quinn quickly strikes the fire starter and lights on of his arrows aflame."

                    show fire at CutIn
                    with vpunch
                    pause(0.5)
                    show fire at CutOut
                    pause(0.25)
                    hide fire
                    pause(0.25)

                    "The plant withers in pain,{cps=4} {/cps}dropping Darcey in the process."

                    
                    window auto hide
                    show darcey angry:
                        subpixel True 
                        pos (1.12, 0.73) rotate -180.0 
                        linear 0.10 pos (1.14, 1.46) rotate -90.0 
                    with Pause(0.20)
                    show darcey angry:
                        pos (1.14, 1.46) rotate -90.0 
                    window auto show


                    "Darcey drops to the ground with a gasp,{cps=4} {/cps}coughing."

                    Darcey "Ouch{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

                    show arrow1 at CutIn
                    with vpunch
                    pause(0.5)
                    show arrow1 at CutOut
                    pause(0.25)
                    hide arrow1
                    pause(0.25)

                    "Quinn shoots one last shot at the dead plant before running to Darcey."

                    
                    window auto hide
                    show quinn angry:
                        subpixel True 
                        xpos 0.0 
                        linear 0.10 xpos 0.47 
                    with Pause(0.20)
                    show quinn angry:
                        xpos 0.47 

                    $ darcey_tired = True

                    jump aftermath

                    #Else
                    "Darcey screams as she's yanked deeper,{cps=4} {/cps}halfway inside the plant's writhing mass."

                    show iris shocked
                    Iris "No no no no!"

                    "Quinn rushes in,{cps=4} {/cps}but it's too late.{cps=4} {/cps}The vines constrict with a sickening {i}snap{/i}."

                    jump bad_ending
        #TODO: locked choice ONLY IF U HAVE FLUTE!
        "Try to use magic.": 
            $ magic_score += 1
            
            "You reach into your pack,{cps=4} {/cps}hands trembling,{cps=4} {/cps}and pull out the carved flute."

            show iris worried

            "The melody trembles at first,{cps=4} {/cps}shaky with adrenaline.{cps=4} {/cps}But soon it steadies,{cps=4} {/cps}notes cutting through the fog like silver thread."

            show magic1 at CutIn
            with hpunch
            pause(0.5)
            show magic1 at CutOut
            pause(0.25)
            hide magic1

            "Magic stirs around you,{cps=4} {/cps}drawn to the song."
            "The plant senses the energy and coils tighter."

            show darcey angry:
                subpixel True 
                parallel:
                    xpos 1.12 
                    linear 0.14 xpos 1.13 
                    linear 0.08 xpos 1.14 
                parallel:
                    ypos 0.73 
                    linear 0.18 ypos 0.74 
                parallel:
                    rotate -180.0 
                    linear 0.12 rotate -180.0 
                    linear 0.06 rotate -193.5 
                    linear 0.02 rotate -198.0 
                    linear 0.10 rotate -180.0 
            with Pause(0.40)

            Darcey "Gah!"
            show iris sad
            show quinn sad

            menu:
                "Aim carefully and cast what you have.":
                    "With your flute in hand you steady your breath and focus—"

                    #TODO: music quick tune here

                    show magic2 at CutIn
                    with hpunch
                    pause(0.5)
                    show magic2 at CutOut
                    pause(0.25)
                    hide magic2

                    "The magic surges,{cps=4} {/cps}wild and hot,{cps=4} {/cps}but this time it finds its mark."

                    "The vines shrivel up and shriek where struck,{cps=4} {/cps}burning to ash."

                    window auto hide
                    show darcey angry:
                        subpixel True 
                        pos (1.12, 0.73) rotate -180.0 
                        linear 0.10 pos (1.14, 1.46) rotate -90.0 
                    with Pause(0.20)
                    show darcey angry:
                        pos (1.14, 1.46) rotate -90.0 
                    window auto show

                    "Darcey drops to the ground with a gasp,{cps=4} {/cps}coughing."

                    Darcey "Ouch{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

                    show arrow1 at CutIn
                    with vpunch
                    pause(0.5)
                    show arrow1 at CutOut
                    pause(0.25)
                    hide arrow1
                    pause(0.25)

                    "Quinn shoots one last shot at the dead plant before running to Darcey."

                    
                    window auto hide
                    show quinn angry:
                        subpixel True 
                        xpos 0.0 
                        linear 0.10 xpos 0.47 
                    with Pause(0.20)
                    show quinn angry:
                        xpos 0.47 

                    $ darcey_tired = True

                    jump aftermath

                "Push more power into the spell.":
                    show iris 
                    "You shove all your fear and desperation into the spell,{cps=4} {/cps}eyes shut."

                    "It explodes outward."
                    show iris shocked
                    show quinn shocked
                    show darcey shocked

                    #TODO: harsh flute sound here

                    show magic3 at CutIn
                    with hpunch
                    pause(0.5)
                    show magic3 at CutOut
                    pause(0.25)
                    hide magic3
                    with vpunch
                    with hpunch

                    "The vines disintegrate,{cps=4} {/cps}but so does the surrounding trees."

                    "A surge of raw mana detonates at your feet,{cps=4} {/cps}throwing you and Darcey back."

                    "You hear nothing but rain."

                    jump bad_ending

    label aftermath:

    
    window auto hide
    show iris worried:
        subpixel True 
        xpos 0.73 
        linear 0.20 xpos 1.1 
        flip
    show darcey angry:
        subpixel True 
        parallel:
            xpos 1.14 
            linear 0.20 xpos 1.07 
        parallel:
            ypos 1.46 rotate -90.0 
            linear 0.10 ypos 1.1 rotate -9.0 
    with Pause(0.30)
    show iris worried:
        xpos 1.1 
    show darcey angry:
        pos (1.07, 1.1) rotate -9.0 
    window auto show



    "Darcey dusts herself off,{cps=4} {/cps}wincing as she rolls her ankle that was red and sore from the vines."

    show darcey sad
    Darcey "Okay.{cps=4} {/cps}Next time,{cps=4} {/cps}let's not follow the creepy footprints {i}directly into a monster's mouth{/i},{cps=4} {/cps}yeah?"

    "Quinn sighs,{cps=4} {/cps}not entertained by Darcey's attempt to lighten the mood."

    show quinn sad
    show iris neutral
    Quinn "As long as you are okay thats all that matters right now."

    "A shiver runs down your spine as you glance back at the abandoned carriage."

    show iris angry
    Iris "No matter what happened here before,{cps=4} {/cps}it's not as important as getting back to the carriage now."

    "No one says much after that.{cps=4} {/cps}The forest feels heavier somehow,{cps=4} {/cps}like something is still watching."
    show iris neutral
    show darcey neutral

    "You help Darcey limp through the underbrush,{cps=4} {/cps}careful not to slip on the slick ground." 


    "Quinn trails close behind,{cps=4} {/cps}his bow still in hand,{cps=4} {/cps}just in case."

    window auto hide
    show iris neutral:
        subpixel True 
        xpos 1.1 
        linear 0.49 xpos 0.02 
        linear 0.01 xpos -0.02 
    show darcey neutral:
        subpixel True 
        parallel:
            xpos 1.07 
            linear 0.49 xpos -0.04 
            linear 0.01 xpos 0.13 
        parallel:
            ypos 1.1 
            linear 0.30 ypos 1.1 
    show quinn sad:
        subpixel True 
        xpos 0.47 
        linear 0.07 xpos 0.46 
        flip
        linear 0.91 xpos -0.43 
    with Pause(0.98)
    show iris neutral:
        xpos -0.02 
    show darcey neutral:
        pos (0.13, 1.1) 
    show quinn sad:
        xpos -0.43 
    scene black 
    with Dissolve(1.5)
    pause(1.5)

    scene forest
    show rain1slow zorder 1
    show rain2slow zorder 0
    show plo happy:
        right   
        flip
    with Dissolve(1.5)

    "The carriage comes back into view,{cps=4} {/cps}its form comforting after the chaos.{cps=4} {/cps}Rain continues to patter softly against the canvas roof."

    
    window auto hide
    show darcey sad at left:
        subpixel True 
        xpos -0.37 
        linear 0.60 xpos 0.23 
    show iris neutral at left:
        subpixel True 
        xpos -0.37 
        linear 0.60 xpos 0.1 
    show quinn sad at left:
        subpixel True 
        xpos -0.49 
        linear 0.60 xpos -0.12 
    with Pause(0.70)
    show darcey sad:
        xpos 0.23 
    show iris neutral:
        xpos 0.1 
    show quinn sad:
        xpos -0.12 
    show plo shocked 
    "Plo's easygoing expression falters the moment he sees Darcey limping beside you."

    Plo "What happened out there?"

    show darcey sad
    Darcey "Got into a tangle with something that really didn't want to let go."

    "She tries to play it off,{cps=4} {/cps}but the exhaustion in her voice is clear."

    show plo sad
    Plo "You alright?"

    show darcey neutral
    Darcey "I'll live.{cps=4} {/cps}Just want to get out of here now"

    "Plo nods,{cps=4} {/cps}his usual grin replaced by something more serious.{cps=4} {/cps}He steps forward and steadies her by the arm, {cps=4} {/cps}uiding her toward the carriage with an unspoken gentleness."

    show plo neutral
    Plo "Up you go,{cps=4} {/cps}then.{cps=4} {/cps}No arguments."

    show darcey neutral:
        subpixel True 
        xpos 0.23 
        linear 0.21 xpos 1.06 
    show quinn sad:
        subpixel True 
        xpos -0.12 
        linear 0.30 xpos 1.07 
    with Pause(0.40)
    show darcey neutral:
        xpos 1.06 
    show quinn sad:
        xpos 1.07 

    if inside_carriage == True:
        Plo "Alright,{cps=4} {/cps}everyone in.{cps=4} {/cps}You can tell me about it later,{cps=4} {/cps}let's get moving before the road throws us another surprise."
    else:
        Plo "[player_name],{cps=4} {/cps}appreciate the company but you should ride inside this time."
        Plo "Humans and rain don't mix too well,{cps=4} {/cps}last I checked."
        "With a softer voice he leans down."
        show plo neutral:
            subpixel True 
            pos (1.0, 1.18) xrotate 0.0 rotate 0.0 
            linear 0.60 pos (0.99, 1.16) xrotate 0.0 rotate -9.0 
        with Pause(0.70)
        show plo neutral:
            pos (0.99, 1.16) xrotate 0.0 rotate -9.0 


        Plo "{i}And to keep a eye on Darcey,{cps=4} {/cps}she looks shaken up.{/i}"

    Iris "Let's get a move on."

    scene carriage 
    show quinn sad:
        left
        Close
        subpixel True pos (-0.2, 1.54) 
    show darcey neutral:
        right
        Close
        subpixel True pos (1.0, 1.58) 
    with Dissolve(1.5)
    pause(2.0)

    Iris "Darcey{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} are you sure you're okay?"

    show darcey sad
    Darcey "Yeah.{cps=4} {/cps}Just sore.{cps=4} {/cps}I've had worse.{cps=4} {/cps}Probably."

    menu:
        "Crack a joke to lighten the mood.":
            Iris "So{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} man-eating vines.{cps=4} {/cps}Real warm welcome from the local flora."
            show darcey happy
            Darcey "Do all enchanted forests offer complimentary strangling,{cps=4} {/cps}or did we just get lucky?"
            show quinn happy
            Quinn "Remind me to write a strongly worded letter to the forest when we are done."
            $ quinn_points += 10
            $ darcey_points += 5

        "Offer to keep an eye on Darcey.":
            Iris "Let me help keep watch while you rest.{cps=4} {/cps}You've done enough today."
            $ quinn_points += 10
            $ darcey_points += 5
            show darcey happy
            show quinn neutral
            Darcey "Thanks.{cps=4} {/cps}I'll try not to fall asleep on your shoulder."

        "Stay quiet, but keep close.":
            "You don't say anything,{cps=4} {/cps}just offer Darcey your arm again as she climbs in."
            show darcey neutral
            "She gives you a brief and grateful glance."
            $ quiet += 1
            $ quinn_points += 5
            $ darcey_points += 5
            show quinn neutral
            show darcey happy
            Darcey "Well that was a interesting side quest."
            show quinn happy 
            Quinn "Just wait.{cps=4} {/cps}Next we'll be ambushed by a bush."
    jump Uphill

######################
## don't investigate
######################  
    label DontInvestigate:
    Quinn "Of course, apologies Iris."

    "You head back over to the carriage,{cps=4} {/cps}seeing darcey and plo working together to free the wheels."
    
    window auto hide
    show plo angry at right:
        subpixel True 
        xpos 1.46 
        linear 0.28 xpos 0.98 
    show iris neutral:
        unflip
        subpixel True 
        xpos 0.59 
        linear 0.30 xpos 0.59 
    show quinn neutral behind iris:
        unflip
        subpixel True 
        xpos 0.0 
        linear 0.22 xpos 0.03 
    show darcey angry at right:
        subpixel True 
        xpos 1.3 
        linear 0.28 xpos 0.93 
    with Pause(0.40)
    window auto show

    Plo "That's it!"

    Plo "Push!"

    show iris happy
    show plo neutral:
        jumpAnim
    show darcey angry:
        subpixel True 
        xpos 0.93 
        linear 0.08 xpos 0.98 
        jumpAnim
    with Pause(0.18)
    with hpunch

    "The carriage jolts forward,{cps=4} {/cps}freeing it from the mud."

    "The sudden momentum nearly sends Darcey stumbling forward,{cps=4} {/cps}but she steadies herself with a muttered curse."

    show darcey angry
    Darcey "Finally.{cps=4} {/cps}Couldn't have been {i}any{/i} gentler?"

    show plo happy
    Plo "We were getting it unstuck, not giving it a massage."

    show darcey neutral
    Darcey "Whatever, get me back on this thing so I can fufill my duty."
    show darcey angry:
        subpixel True 
        xpos 0.98 
        linear 0.30 xpos 1.3 
    with Pause(0.40)

    show quinn sad
    "Despite the small victory,{cps=4} {/cps}Quinn remains still,{cps=4} {/cps}his sharp gaze lingering on the treeline before getting on the carriage."
    show iris neutral
    show quinn sad:
        subpixel True 
        xpos 0.03 
        linear 0.60 xpos 1.03 
    with Pause(0.70)

    if inside_carriage == True:
        show plo neutral:
            flip
        Plo "Alright,{cps=4} {/cps}everyone in?{cps=4} {/cps}Let's get moving before the road throws us another surprise."
    else:
        show plo neutral:
            flip
        Plo "[player_name],{cps=4} {/cps}appreciated the company,{cps=4} {/cps}but you should ride inside this time."
        Plo "Humans and rain don't mix too well,{cps=4} {/cps}last I checked."
        Plo "Makes them all sick."
    show iris happy
    Iris "Alright!{cps=4} {/cps}Then let's head out."

    scene carriage 
    show quinn neutral:
        left
        Close
        subpixel True pos (-0.2, 1.54) 
    show darcey neutral:
        right
        Close
        subpixel True pos (1.0, 1.58) 
    with Dissolve(1.5)
    pause(2.0)



    "You settle into the carriage,{cps=4} {/cps}rain drips from your wet sleeve."

    if get_serious == False:
        Iris "Remind me to thank the horse later.{cps=4} {/cps}If we survive this, it gets half my rations and a name."

        show darcey happy
        show quinn happy
        Darcey "Better make it a title and a pension if it gets us all the way there with how bumpy Plo is driving."

        show quinn neutral
        Quinn "It has maintained a consistent pace despite the mud and incline.{cps=4} {/cps}That's valuable."

        "You laugh faintly,{cps=4} {/cps}but the tension creeps in as the wheels begin to grind harder,{cps=4} {/cps}the incline steeper now."
    else:
        """
        Time passes.
        The journey feels longer now, the weight of what's ahead pressing down on you.
        Quinn and Darcey's voices blend into the background, their words muffled by your thoughts as you stare out the window, lost in the passing landscape.
        The uncertainty of what's to come lingers in the air, making the world outside feel distant and cold.
        """
    "The forest outside thins somewhat,{cps=4} {/cps}replaced by rocky outcrops and mud slick ridges."

    "Suddenly,{cps=4} {/cps}the carriage jolts."
    with hpunch
    show quinn shocked
    show darcey shocked

    "A loud {i}crack{/i} rings out as one of the rear wheels slips,{cps=4} {/cps}dragging the carriage a foot to the left toward a narrow ravine."

    window auto hide
    show quinn shocked:
        subpixel True 
        xpos -0.2 
        linear 0.14 xpos -0.41 
        linear 0.09 xpos -0.18 
        linear 0.09 xpos -0.41
    show darcey shocked:
        flip
        subpixel True 
        xpos 1.0 
        linear 0.29 xpos 0.66 
        linear 0.01 xpos 0.62 
        linear 0.01 xpos 0.59 
        linear 0.01 xpos 0.59 
    with Pause(0.42)
    show quinn shocked:
        xpos -0.4 
    show darcey shocked:
        xpos 0.59 
    with hpunch

    Iris "Whoa—!"
    
    show darcey angry
    Darcey "Plo?!"
    show quinn sad
    Quinn "We're sliding—"

    "From outside,{cps=4} {/cps}Plo yells."

    Plo "I KNOW!"

    Plo "Everyone {i}lean right!{/i}{cps=4} {/cps}NOW!"
    with hpunch

    "You and the others throw your weight to the right side of the carriage.{cps=4} {/cps}The horses whinny in panic as Plo wrestles with the reins."

    "The carriage shudders{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} then steadies.{cps=4} {/cps}A few pebbles tumble off the edge below you,{cps=4} {/cps}disappearing into the fog."

    show quinn sad:
        subpixel True 
        xpos -0.4 
        linear 0.28 pos (-0.2, 1.54) 
    show darcey neutral:
        unflip
        subpixel True 
        xpos 0.59 
        linear 0.79 pos (1.0, 1.58) 
    with Pause(0.89)

    "A long silence follows."

    show darcey neutral
    Darcey "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}So, that counts as our one 'slip down a hill',{cps=4} {/cps}right?{cps=4} {/cps}Told you I wouldn't be the one to do it."

    show quinn neutral
    Quinn "Technically, we didn't {cps=4}fall{/cps}."

    Iris "Let's not test the odds on a second try."

    show quinn happy
    show darcey happy

    "Laughter breaks the tension,{cps=4} {/cps}and for a moment,{cps=4} {/cps}the cabin feels warmer despite the damp."

    "Outside,{cps=4} {/cps}the rain begins to ease.{cps=4} {/cps}The trees thin further as the road evens out,{cps=4} {/cps}trading mud for coarse,{cps=4} {/cps}sandy ground."

    menu:
        "Ask Darcey about her worst travel day.":
            $ darcey_points += 5
            Iris "Darcey.{cps=4} {/cps}What's the worst travel day you've ever had?"

            show darcey happy
            Darcey "Oooh, good question. Not including today{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            show darcey neutral
            Darcey "One time I was escorting a food delivery load. The {cps=4}entire{/cps} cartload is raw fish, the sun was blazing down, and someone thought putting goat milk in glass jars was smart."

            show quinn worried
            Quinn "I can almost remember the smell."

            show darcey happy
            show quinn neutral
            Darcey "By the end of the second day even the vultures gave up.{cps=4} {/cps}Took one sniff and ran for the hills."

        "Ask Quinn about his bow reflexes.":
            $ quinn_points += 5
            Iris "Quinn,{cps=4} {/cps}you're incredibly precise with that bow.{cps=4} {/cps}How did you get so skilled?"

            show quinn neutral
            Quinn "Being half-elf has its advantages.{cps=4} {/cps} But precision with a bow comes from years of practice."
            
            Quinn "I've spent countless hours training,{cps=4} {/cps}honing my focus until it became second nature."

        "Stay quiet and listen to the rain.":
            $ quiet += 1

            "You settle into the quiet moment,{cps=4} {/cps}letting the sound of soft rainfall and creaking wood lull your nerves."

            "Darcey rests her head back,{cps=4} {/cps}staring up at the ceiling of the carriage."
            show darcey neutral
            Darcey "Almost feels peaceful.{cps=4} {/cps}Almost."

            show quinn neutral
            "Quinn closes his eyes briefly,{cps=4} {/cps}arms crossed,{cps=4} {/cps}but his hand never strays far from his bow."

            "The silence is broken only by the occasional sound of Darcey or Quinn shifting, and the faint hum of the carriage over uneven ground."

            "As you listen to the rain,{cps=4} {/cps}a memory rises in your mind—one you haven't thought of in years."

            show black with Dissolve(1.5)
            #this could be a lot cooler and more lore dropping if expanded
            "The day you were drafted into the war.{cps=4} {/cps}You were barely an adult, yet it was you or your elderly parents."

            "It was a choice you would make again."

            hide black with Dissolve(1.5)


    "A small jolt reminds you you're still on a rough road."
    with hpunch

    show darcey happy
    Darcey "Alright,{cps=4} {/cps}bets on how long until we hit the next 'harmless little bump' in the road?"

    show quinn happy
    Quinn "Do you count the time in minutes?"

    Iris "I'm starting to think we're cursed.{cps=4} {/cps}Who angered a forest spirit recently?"

    show darcey angry
    Darcey "Probably Plo.{cps=4} {/cps}He keeps cursing under his breath every time the carriage tilts."

    "Right on cue,{cps=4} {/cps}Plo's voice bellows through the canvas."

    Plo "I HEARD THAT!" 
    #TODO: a text effect would be nice here

    show darcey happy

    Darcey "{cps=4}You were meant to.{/cps}"

    "Laughter spreads again as the trees begin to thin,{cps=4} {/cps}and the wheels finally stop groaning in the muck."

    "The air grows drier.{cps=4} {/cps}The soggy forest floor gives way to firmer,{cps=4} {/cps}sandy terrain,{cps=4} {/cps}and the clouds begin to part."

    jump Uphill

######################
## uphill
######################  
    label Uphill:
    #TODO: rain stops
    #enviroment turns more hot and mixed with sand
    
    Plo "Not too long and we will be on the main merchant path."

    show quinn neutral

    Quinn "The sun is setting soon,{cps=4} {/cps}what would you like to do, [player_name]?"

    Iris "Let's camp here for now."
    show darcey happy

    Plo "About time.{cps=4} {/cps}I was starting to think we'd need a paddle instead of wheels."

    Plo "With the luck we have,{cps=4} {/cps}would be faster to just carry everything."

    scene sand
    with Dissolve(1.5)

    pause(1.5)

    
    show plo neutral at left:
        subpixel True xpos 0.11
    show iris happy at right:
        flip
    show quinn neutral at left:
        subpixel True xpos 0.04 
    show darcey neutral at left:
        flip
        subpixel True xpos 0.01
    with Dissolve(1.5)

    with Pause(0.40)

    "You exit the carriage to find a good spot to rest."

    "As the sun dips lower behind the clouds,{cps=4} {/cps}a small outcropping of rock offers a natural break from the wind."

    #TODO: add the tintshader
    show quinn happy
    Quinn "This is as good a place as any to rest for the night."

    "The party sets up camp beneath the outcropping.{cps=4} {/cps}Plo unloads gear from the back while Quinn begins building a fire,{cps=4} {/cps}coaxing life from damp kindling with careful,{cps=4} {/cps}practiced hands."

    "The fire crackles softly as evening settles in.{cps=4} {/cps}The clouds begin to part just enough for the faintest glow of moonlight to break through."

######################
## night
######################  
    label night:

################################################################################
## █▀▄ ▄▀▄ ▀▄▀   ▀█▀ █ █ █ █▀█ 
## █▄▀ █▀█  █     █  ▀▄▀▄▀ █▄█ 
################################################################################





################################################################################
## █▀▄ ▄▀▄ ▀▄▀ ▀█▀ █▄█ █▀█ █▀▀ █▀▀ 
## █▄▀ █▀█  █   █  █ █ █▀▄ ██▄ ██▄ 
################################################################################




################################################################################
## Endings
################################################################################
label bad_ending:
    scene black with Dissolve(1.5)
    centered "Game Over"
    achieve badend
    jump end


#keep this the very last line of code
label end:
