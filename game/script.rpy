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

define sprite_image = "f_iris"



################################################################################
##  ████   ███  █   █ █████   █████ █████  ███  ████  █████ 
##  █     █   █ ██ ██ █       █       █   █   █ █   █   █   
##  █  ██ █████ █ █ █ ████    █████   █   █████ ████    █   
##  █   █ █   █ █   █ █           █   █   █   █ █   █   █   
##   ███  █   █ █   █ █████   █████   █   █   █ █   █   █   
################################################################################
label start:

    stop music fadeout 8

    scene black with Dissolve(2.5)
    show m_iris neutral:
        right
        flip
    show f_iris neutral:
        left
    with Dissolve(2.5)
    label GenderQuestion:
        show m_iris neutral
        show f_iris neutral

    "Select your portrait"
    
    menu:
        "Masculine":
            $ sprite_image = "m_iris"
            jump PronounQuestion
        "Feminine":
            $ sprite_image = "f_iris"
            jump PronounQuestion
   
    label PronounQuestion:
    "Select Pronouns"

    menu: 
        "She/Her":
            $ pronouns = "She/Her"
            jump NameQuestion

        "He/Him":
            $ pronouns = "He/Him"
            jump NameQuestion

        "They/Them":
            $ pronouns = "They/Them"
            jump NameQuestion

    label PronounCheck:
        "Are you Sure?"
        menu:
            "Yes":
                jump NameQuestion
            "No":
                jump PronounQuestion
                
    label NameQuestion:
    # Name characterS
    $ player_name = renpy.input("What would you like to name your character?", default="Iris", length=20).strip()

    if player_name == "":
        $ player_name = "Iris"

    $ p.SetCharacter(Character(player_name))
    

    label FinalCheck:
        if pronouns == "She/Her":
            if sprite_image == "f_iris":
                show f_iris happy
            elif sprite_image == "m_iris":
                show m_iris happy
            Iris "My name is [player_name] and my pronouns are She/Her"
        elif pronouns == "He/Him":
            if sprite_image == "f_iris":
                show f_iris happy
            elif sprite_image == "m_iris":
                show m_iris happy
            Iris "My name is [player_name] and my pronouns are He/Him"
        elif pronouns == "They/Them":
            if sprite_image == "f_iris":
                show f_iris happy
            elif sprite_image == "m_iris":
                show m_iris happy
            Iris "My name is [player_name] and my pronouns are They/Them"

        "Continue with those settings?"
        menu: 
            "Yes":
                jump intro
            "No":
                jump GenderQuestion
 
################################################################################
## ▀█▀ █▄ █ ▀█▀ █▀█ █▀█ 
## ▄█▄ █ ▀█  █  █▀▄ █▄█ 
################################################################################
label intro:

    play amb1 cave_amb fadein 6 volume 0.7

    scene bg cave with Dissolve(1.5)
    camera:
        perspective True
    
    $ renpy.music.play("audio/music/01 Captains Tent Strings.ogg", channel='music1', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/01 Captains Tent Brass.ogg", channel='music2', loop=True, synchro_start=True, tight=True)
    $ renpy.music.set_volume(0, delay=0, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    
    """
    Deep within a vast cave system,{cps=4} {/cps}warmed by the geothermal currents of an underground aquifer,{cps=4} {/cps}lies your camp.
    """

    """
    Humidity and dirt clings to your skin as stalactites loom overhead with mineral-rich condensation.

    You are called urgently to the Captain's Chamber,{cps=4} {/cps}a large tent,{cps=4} {/cps}by a fellow soldier.{cps=4} {/cps}At this hour in the night?{cps=4} {/cps}Strange.{cps=4} {/cps}Nervousness creeps into your quick steps.

    Through winding tunnels,{cps=4} {/cps}you follow the jagged walls with your torchlight.
    
    Heated water hisses from the fissures above.
    
    The air is thickest outside the Captain's Chamber.{cps=4} {/cps}It carries the scent of damp rock.

    You step in.
    """
    achieve start
    stop amb1 fadeout 4
    play amb2 captains_amb fadein 1 volume 0.2

    play sfx1 tent_open volume 0.2
    
    $ renpy.music.set_volume(0.4, delay=8, channel='music1')

    scene bg tent_captain_1 with Dissolve(1.5)


    """
    The Captain's Chamber flaunts its roominess compared to the path it takes to get there. {cps=4} {/cps}Space must be made for the parchments.

    The scent of ink,{cps=4} {/cps}sweat,{cps=4} {/cps}and something vaguely metallic immediately catches your nose. 

    You warm up from the burning oil lamps around,{cps=4} {/cps}and walk forward to the sturdy wooden desk.
    
    Maps and smudged reports scatter in front of the tired man hunched over,{cps=4} {/cps}staring down at them.{cps=4} {/cps}The Captain. 
    """
    
    show iris worried:
        right
        flip
    with Dissolve(1.5)

    """
    On closer inspection,{cps=4} {/cps}you notice the Captain's dark circles under his bloodshot eyes.{cps=4} {/cps}Who knows when he last moved.
    
    He barely reacted to your approach.

    You give him a quick salute and announce your presence.
    """

    show iris neutral
    Iris "Captain."

    Captain "[player_name],{cps=4} {/cps}wait there,{cps=4} {/cps}I have more people on their way."
    
    window auto hide
    play sfx1 tent_close volume 0.2
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

    $ renpy.music.set_volume(0.7, delay=4, channel='music1')
    
    show plo angry at jumpAnim
    Plo "{i}Can't let this old man get his sleep after a hard days work?{/i}"

    """
    His heavy-lidded eyes scan the room as if routine then approaches. 
    
    He straightens his thick frame and gives the Captain a curt salute.
    """

    show plo neutral
    Plo "Captain."

    $ plo_name = "Plo"

    Captain "At ease [plo_name],{cps=4} {/cps}I wouldn't drag you out this late without a good reason." 

    show plo happy

    "Plo gives a sarcastic snort."

    show plo neutral:
        flip
    show plo neutral:
        subpixel True 
        xpos 0.5 
        linear 1.00 xpos 0.18 
    with Pause(1.10)
    show plo neutral:
        xpos 0.18 
        unflip

    Plo "{i}Right{/i}."

    show plo neutral


    "Only a second passes before the tent door flutters open once more."

    window auto hide
    play sfx1 tent_open volume 0.2
    show darcey neutral with Dissolve(1.5) 
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        linear 0.30 pos (1278, 1611) zoom 2.79 
    with Pause(0.40)
    camera:
        pos (1278, 1611) zoom 2.79 
    window auto show
    "A short,{cps=4} {/cps}red-skinned tiefling strides in next.{cps=4} {/cps}You swore you feel the air stop at her presence,{cps=4} {/cps}afraid to move disrespectfully."
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
    "Her dark eyes flick over the assembled group,{cps=4} {/cps}assessing,{cps=4} {/cps}before settling on the Captain with a crisp salute."
    camera:
        subpixel True 
        pos (2061, 386) zoom 2.79 
        linear 0.30 pos (0, 0) zoom 1.0 
    with Pause(0.40)
    camera:
        pos (0, 0) zoom 1.0 

    $ renpy.music.set_volume(1, delay=4, channel='music1')

    Darcey "Captain."

    "The final arrival slips inside quickly after.{cps=4} {/cps}The extra shadow against the torchlight is what made you notice."

    show darcey neutral:
        subpixel True 
        xpos 0.5 
        linear 1.00 xpos 0.23
    with Pause(1.10)
    show darcey neutral:
        xpos 0.23
        flip

    play sfx1 tent_close volume 0.1

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
    "Glancing between the others,{cps=4} {/cps}he only pauses on the tiefling with a nod of acknowledgment{cps=4} {/cps}before facing the Captain."
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

    $ renpy.music.set_volume(1, delay=8, channel='music2')

    show quinn shocked
    Quinn "Captain.{cps=4} {/cps}Something urgent,{cps=4} {/cps}I assume?"

    "The Captain waves the three guests forward."
    Captain "Come in,{cps=4} {/cps}Come in."

    $ darcey_name = "Darcey"
    $ quinn_name = "Quinn"
    show quinn neutral behind darcey at flip:
        subpixel True 
        xpos 0.5 
        linear 1.00 xpos 0.05 
    with Pause(1.10)
    show quinn neutral:
        xpos 0.05 
        unflip



    """
    The Captain relaxes then pushes aside papers and pulls out a white letter sealed by a striking red wax stamp.

    A pause.

    He grins,{cps=4} {/cps}a rare grin.
    """

    Captain "This is a very important message that I need delivered.{cps=4} {/cps}You four will be the ones delivering it."

    show plo happy at jumpAnim
    
    Plo "Hah!{cps=4} {/cps}'bout time I get to hauling something a little less explosive!"

    menu:
        "What kind of message?":
            show iris happy
            Captain "I'm glad you asked{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1

        "Why choose us?":
            Captain "[plo_name],{cps=4} {/cps}the best carriage driver we've got.{cps=4} {/cps}He knows how to handle rough terrain—and rougher company."
            show plo happy
            Captain "[quinn_name],{cps=4} {/cps}a skilled navigator.{cps=4} {/cps}If there's a way through,{cps=4} {/cps}he'll find it."
            show quinn happy
            Captain "[darcey_name],{cps=4} {/cps}a fighter through and through.{cps=4} {/cps}She's deadly for fights you want to pick and intelligent for fights you don't." 
            show darcey happy ##Pronoun Below
            
            if pronouns == "She/Her":
                Captain "And of course,{cps=4} {/cps}[player_name],{cps=4} {/cps}the rising star courier.{cps=4} {/cps}Fast,{cps=4} {/cps}reliable,{cps=4} {/cps}and able to think on her feet."
            elif pronouns == "He/Him":
                Captain "And of course,{cps=4} {/cps}[player_name],{cps=4} {/cps}the rising star courier.{cps=4} {/cps}Fast,{cps=4} {/cps}reliable,{cps=4} {/cps}and able to think on his feet."
            elif pronouns == "They/Them":
                Captain "And of course,{cps=4} {/cps}[player_name],{cps=4} {/cps}the rising star courier.{cps=4} {/cps}Fast,{cps=4} {/cps}reliable,{cps=4} {/cps}and able to think on their feet."

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
    
    $ renpy.music.set_volume(1, delay=4, channel='music2')

    window auto hide
    show bg tent_captain_2 with Dissolve(1.5)
    pause(2.0)

    Captain "The enemy sent us this letter of surrender at sundown."

    show darcey shocked 
    show plo blush at happyAnim
    show quinn shocked 
    show iris shocked
    
    Darcey "{i}Gasp{/i}"
    show darcey happy:
        flipRight
        subpixel True 
        xpos 0.20
        linear 0.30 xpos 0.18
    with Pause(0.40)
    show quinn happy

    Quinn "At long last{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
    

    Captain "There's still work to be done here,{cps=4} {/cps}but what matters now is to send word to the capital.{cps=4} {/cps}Immediately."

    Captain "That is why I'm entrusting this mission to you,{cps=4} {/cps}[player_name]."

    menu:
        "Yes,{cps=4} {/cps}Captain!":
            show iris happy
            Captain "Good.{cps=4} {/cps}You all are dismissed.{cps=4} {/cps}The others will wake up to good news."
            jump continue2
        
        "Stay Quiet":
            show iris worried
            Captain "......{cps=4} {/cps}Well,{cps=4} {/cps}get going then!{cps=4} {/cps}I want you all out of here before morning."
            jump continue2
    
    label continue2:

    Iris "Understood,{cps=4} {/cps}Captain."

    """
    You turn to your new team,{cps=4} {/cps}who stare at you with anticipation.

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
    stop amb2 fadeout 6
    play amb1 cave_amb fadein 3 volume 0.5
    window auto hide
    show iris happy:
        unflip
        subpixel True 
        xpos 1.0 
        linear 0.73 xpos 1.37 
    with Pause(0.93)

    scene black with dissolve

    """
    You make your way back to your home tent.
    
    It's an uncomfortable warmth that you've gotten used to.{cps=4} {/cps}Thick with humidity.{cps=4} {/cps}Exhaustion seems to stick to you in the same way as you walk.
    """ 
    $ renpy.music.set_volume(0, delay=8, channel='music2')
    $ renpy.music.set_volume(0.7, delay=8, channel='music1')
    stop amb1 fadeout 6
    play amb2 soldier_tent_amb fadein 2 volume 0.5

    scene bg tent_1 
    with Dissolve(1.5)

    """
    
    Inside the soldier's tent,{cps=4} {/cps}a thick layer of grime made up of sweat and dirt sticks to the occupants.

    Half a dozen exhausted soldiers lay cramped like sardines in haphazardly built bunk beds.
    
    The canvas walls do little to shield you from the environment outside. 
    
    A single lantern,{cps=4} {/cps}its flame weak and flickering,{cps=4} {/cps}casts shadows along the tent's sagging ceiling.

    This was the life of a conscripted solider.
    
    The few still awake glance up as you return.
    """
    $ renpy.music.set_volume(0.5, delay=8, channel='music1')

    show iris neutral at Close

    Bunkmate "What was that about?{cps=4} {/cps}You get in trouble?"

    "Your bunkmate above you shifts to eye you inquisitively."

    menu:
        "Be honest":
            show iris happy at happyAnim
            Iris "Actually,{cps=4} {/cps}I have great news!"
            "You lean in,{cps=4} {/cps}lowering your voice so as to not wake anyone."
            show iris happy at VeryClose
            Iris "The Captain will announce the end of the war in the morning."
            "They nearly shout before clapping both hands over their mouth."
            Iris "Shh,{cps=4} {/cps}I have to pack.{cps=4} {/cps}I'm leaving before sunrise"
            show iris blush at Close
            Bunkmate "I can't believe it will be over;{cps=4} {/cps}THIS will be over.{cps=4} {/cps}I'm not going to be able to sleep tonight."
            jump continue3

        "Joke around":
            show iris sad
            Iris "3 days night shift duty for me."
            Bunkmate "Man,{cps=4} {/cps}that sucks."
            "You chuckle."
            show iris happy
            Iris "Joking."
            Iris "It was about a mission.{cps=4} {/cps}You will hear about it in the morning~"
            Bunkmate "Hmph{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Guess I'll wait."
            jump continue3
        
        "Be evasive":
            Iris "I got assigned a mission.{cps=4} {/cps} I leave before sunrise."
            Bunkmate "Hmph{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Guess I'll wait."
            jump continue3
    
    label continue3:
    $ _skipping = False

    """
    
    After checking that no one is spying,{cps=4} {/cps}You take a moment to look at the map the Captain entrusted to you.

    """
    window auto hide
    show map with Dissolve(1.5)

    """

    The ideal trip to the capital would be to cut through the mountain path.

    Three days,{cps=4} {/cps}maybe less if you're quick.

    We'd need to pack enough food and supplies for at least twice that.{cps=4} {/cps}For four people.
    """
    hide map with Dissolve(1.5)
    show iris happy


    """
    Quietly you reach under the bunk to pull out your stuff.

    """

    window auto hide
    show screen Inventory_Screen

    show screen close_inventory_button

    window hide

    pause 0.5


    """
    You decide to sleep,{cps=4} {/cps}getting what little rest you still can.
    """

    $ HideAllNonInventoryItems()

    $ ShowingInventoryButton = True

    $ renpy.music.stop(channel='music1', fadeout=8)
    $ renpy.music.stop(channel='music2', fadeout=None)
    stop amb2 fadeout 8
    
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
    $ _skipping = True
   
    """
    Sunrise hasn't hit yet as you make your way to the designated meeting spot.

    Soldiers move about groggily.{cps=4} {/cps}The night shift returns for some much needed sleep as{cps=4} {/cps}the day shift gets ready to work.
    """

    play amb1 cave_rain_amb fadein 3 volume 0.3

    scene bg cave
    show iris happy:
        right
        flip
    show carriage back at left:
        flip
    with Dissolve(1.5)


    """
    You meet your party near the supply tent{cps=4} {/cps}where a wooden carriage{cps=4} {/cps}tied to a sturdy draft horse{cps=4} {/cps}stands ready.


    A cold chill blows into the cave,{cps=4} {/cps}bringing the smell of rain and mud.{cps=4} {/cps}You wish nature was more merciful.


    [plo_name] secures the last of the crates onto the back of the carriage.
    """

    show plo happy:
        subpixel True 
        xpos -0.61 
        linear 1.00 xpos 0.06 
    with Pause(1.10)
    show plo happy:
        xpos 0.06 
   
    Plo "Cart's packed and ready.{cps=4} {/cps}Not much,{cps=4} {/cps}but it'll get us there."

    show quinn neutral at left:
        subpixel True 
        xpos -0.46 
        linear 0.80 xpos -0.04 
    with Pause(0.90)
    show quinn neutral:
        xpos -0.04 

    Quinn "Looks like a rainy day."


    show quinn sad
    show iris neutral


    Quinn "At this rate,{cps=4} {/cps}our journey might be hindered by the mud."


    show plo happy at jumpAnim
    show quinn neutral
    show iris happy


    Plo "A little rain won't bother me."


    Plo "I'll be driving that carriage even if it's blizzardin'."


    window auto hide
    show darcey happy:
        subpixel True 
        xpos 0.99 
        yanchor 1.0
        ypos 1.0
        linear 0.75 xpos 0.58 
        linear 0.25 xpos 0.51 
    with Pause(1.10)
    show darcey happy:
        xpos 0.51 

    "[darcey_name] approaches,{cps=4} {/cps}a bag in hand and a dignified smirk on her face."

    show quinn happy
    show darcey happy

    Darcey "Try not to get us stuck in a ditch,{cps=4} {/cps}alright?"


    show plo angry


    Plo "As if {i}you{/i} would handle it any better."

    show plo happy at happyAnim

    Plo "Maybe a little rain would put out your fire-like temper."


    show darcey angry

    Darcey "Hey,{cps=4} {/cps}I'd have us halfway there already if I was in charge."

    
    show quinn happy

    Quinn "Halfway down a ravine maybe,{cps=4} {/cps}I don't seem to recall you ever driving a carriage before{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

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
            
            $ renpy.music.play("audio/music/02 Journey Harp.ogg", channel='music1', loop=True, synchro_start=True, tight=True)
            $ renpy.music.play("audio/music/02 Journey Accomp.ogg", channel='music2', loop=True, synchro_start=True, tight=True)
            $ renpy.music.play("audio/music/02 Journey Tamb.ogg", channel='music3', loop=True, synchro_start=True, tight=True)
            $ renpy.music.play("audio/music/02 Journey Clar.ogg", channel='music4', loop=True, synchro_start=True, tight=True)
            $ renpy.music.set_volume(0.7, 0.1, channel='music1')
            $ renpy.music.set_volume(0, 0, channel='music2')
            $ renpy.music.set_volume(0.2, 1, channel='music3')
            $ renpy.music.set_volume(0, 0, channel='music4')
            
            "[plo_name] blinks.{cps=4} {/cps}[darcey_name] groans.{cps=4} {/cps}[quinn_name] hides a smirk."
            show darcey worried
            Darcey "That was terrible."
            Iris "You're just jealous you didn't think of it first."
            show plo neutral
            show darcey neutral
            Plo "Guess we better roll out before [player_name] hits us with another one."
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
            "[darcey_name] looks embarrassed of her unknightly behavior."
            show plo worried
            Plo "I'm just going to finish packing then{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
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
            show plo neutral
            Plo "I'm just going to finish packing then{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
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


    [quinn_name]'s eyes narrow slightly at the sight of the road ahead.
    """


    show quinn sad
    Quinn "The weather will only get worse if we wait."

    show quinn neutral
    show iris neutral
    Quinn "I recommend leaving through the rain as is."

    $ renpy.music.play("audio/music/02 Journey Harp.ogg", channel='music1', loop=True, synchro_start=True, tight=True, if_changed=True)
    $ renpy.music.play("audio/music/02 Journey Accomp.ogg", channel='music2', loop=True, synchro_start=True, tight=True, if_changed=True)
    $ renpy.music.play("audio/music/02 Journey Tamb.ogg", channel='music3', loop=True, synchro_start=True, tight=True, if_changed=True)
    $ renpy.music.play("audio/music/02 Journey Clar.ogg", channel='music4', loop=True, synchro_start=True, tight=True, if_changed=True)
    $ renpy.music.set_volume(0.7, 0.1, channel='music1')
    $ renpy.music.set_volume(0, 0, channel='music2')
    $ renpy.music.set_volume(0.2, 1, channel='music3')
    $ renpy.music.set_volume(0, 0, channel='music4')

    

    show iris happy
    Iris "Alright,{cps=4} {/cps}everybody.{cps=4} {/cps}Let's get this letter on the road."

    Iris "Mount up."


    """
    [plo_name] packs the final crate and secures the latch on the carriage.

    [darcey_name] and [quinn_name] enter the carriage.
    """
    window auto hide
    show darcey neutral:
        subpixel True 
        xpos 0.49 
        linear 1.00 xpos -0.29 
    show quinn neutral:
        subpixel True 
        flip
        xpos 0.1 
        linear 1.30 xpos -0.21 
    with Pause(1.40)
    show darcey neutral:
        xpos -0.29 
    show quinn neutral:
        unflip

    """


    [quinn_name] props the door open and faces you with respect.
   
    """
   
    Quinn "After you,{cps=4} {/cps}[player_name]."


    menu:
        "Sit inside":
            Iris "Thank you,{cps=4} {/cps}[quinn_name]."
            window auto hide
            show iris happy:
                subpixel True 
                parallel:
                    'iris happy'
                    0.30
                    'iris happy' with dissolve
                parallel:
                    xpos 1.0 
                    linear 1.20 xpos 0.12 
            with Pause(1.30)
            show iris happy:
                xpos 0.12 
            $ quinn_points += 5
            $ darcey_points += 5
            $ inside_carriage = True
            jump InsideCarriage


        "Guard outside":
            "[player_name] waves their hand at [quinn_name]."
            Iris "No need,{cps=4} {/cps}I'll help guard outside alongside [plo_name]."
            Quinn "As you wish."
            show quinn neutral:
                flip
                subpixel True 
                linear 0.30 xpos -0.47 
            "[quinn_name] shuts the door behind them."
            $ inside_carriage = False
            $ plo_points += 5
            jump OutsideCarriage
     
######################
## inside carriage
######################
    label InsideCarriage:
    
    play amb2 drizzle_carriage_amb fadein 2 volume 0.5
    stop amb1 fadeout 10
    

    scene bg cave 
    show carriage
    with Dissolve(1.5)

    $ renpy.music.set_volume(0.5, 2, channel='music3')  

    """
    You climb into the carriage,{cps=4} {/cps}settling on the slightly worn wooden seat.


    The inside is dim without the presence of an oil lamp.{cps=4} {/cps}You can hear the muffled voice of rain hitting the canvas roof.
    """

    $ renpy.music.set_volume(0.8, 6, 'music2')
    $ renpy.music.set_volume(1, 6, 'music4')
    
    window auto hide
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
            "[darcey_name] laughs,{cps=4} {/cps}while [quinn_name] gives a small,{cps=4} {/cps}knowing smile."
            show darcey blush  
            Darcey "I'll be on my best behavior from here on out."
            Quinn "I bet so."
            $ darcey_points += 5
            $ quinn_points += 3


        "Be serious":
            Iris "Stay focused.{cps=4} {/cps}Stay alert.{cps=4} {/cps}Distractions can't delay us."  
            """
            [darcey_name] smiles,{cps=4} {/cps}appreciating the knowledgeable advice.
           
            [quinn_name] gives a small nod of approval.
            """
            show quinn happy
            Quinn "Understood."  
            show darcey blush
            Darcey "I'll be on my best behavior from here on out."
            $ darcey_points += 2
            $ quinn_points += 5
    
    pause(1.5)
    show darcey neutral
    "Time passes in silence."
    show quinn neutral
    pause(1.5)
    "You feel the carriage jolt around softly as you depart."
    with vpunch
    show bg forest with Dissolve(1.5)

    menu:
        "Ask [quinn_name] about the path ahead":  
            label path:
            $ quinn_points += 5
            show darcey happy
            Iris "What's the terrain like ahead?"
            show quinn neutral
            Quinn "Rough.{cps=4} {/cps}Once we're out of the mud,{cps=4} {/cps}we'll hit gravel.{cps=4} {/cps}It'll even out once we hit the main road."  
            show darcey neutral
            "[darcey_name] sighs."
            Darcey "Let's hope [plo_name] is as skilled as he brags he is."
            jump continue5


        "Ask about [darcey_name] and [plo_name]":
            Iris "What's the deal between you and [plo_name]?"
            show quinn neutral
            show darcey neutral
            "[darcey_name] sighs,{cps=4} {/cps}lowering her voice to a whisper."
            show darcey angry
            Darcey "Let's just say you'd be wrong to expect him to be a model soldier."
            show darcey neutral
            Darcey "[plo_name]'s not the kind of person who thinks of the consequences before he acts."
            show quinn angry
            "[quinn_name] hits her softly with his elbow."
            Quinn "He has a good heart when it matters."
            show darcey blush
            show quinn neutral
            jump continue5


        "Sit Quietly":  
            show quinn neutral
            show darcey neutral
            
            "You settle back,{cps=4} {/cps}listening to the sound of the rain."
            pause(1.5)

            "[quinn_name]'s eyes remain half-lidded as [darcey_name] hums softly under her breath."
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
                        "[darcey_name] studies you for a moment,{cps=4} {/cps}her gaze steady but not probing." 
                        Darcey "You don't talk much,{cps=4} {/cps}do you?"
                        menu:
                            "I'm not much of a talker.":
                                Iris "I'm more of a listener."  
                                show darcey happy
                                Darcey "Listeners are valuable too."
                                show darcey neutral
                                "[darcey_name]'s gaze moves toward the window."
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
                        "[quinn_name] studies you for a moment,{cps=4} {/cps}his gaze steady but not probing."
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
    pause(0.05)
    with hpunch
    pause(0.05)
    with vpunch

    $ renpy.music.stop(channel='music1', fadeout=1)
    $ renpy.music.stop(channel='music2', fadeout=1)
    $ renpy.music.stop(channel='music3', fadeout=1)
    $ renpy.music.stop(channel='music4', fadeout=1)

    """
    The carriage lurches forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.


    You hear a horse's annoyed neigh from outside.
    """

    show darcey angry

    Darcey "Damnit,{cps=4} {/cps}I knew he would."
   
    Iris "That does not sound good{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"


    "You,{cps=4} {/cps}[quinn_name],{cps=4} {/cps}and [darcey_name] make your way out of the carriage."

    play amb1 drizzle_amb fadein 2 volume 0.7
    stop amb2 fadeout 10

    scene bg forest 
    show carriage back:
        right
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

    Iris "[plo_name],{cps=4} {/cps}are you alright?"

    show plo angry

    Plo "I am,{cps=4} {/cps}but I can't say the same for the carriage."

    "You see one of the carriage's wheels was stuck in the mud."

    jump WheelInMud


######################
## outside carriage
######################
    label OutsideCarriage:

    play amb2 drizzle_amb fadein 2 volume 0.8
    stop amb1 fadeout 10
    
    

    scene bg forest with Dissolve(1.5)
    show rain1fast zorder 1
    show rain2fast zorder 0

    $ renpy.music.set_volume(0.5, 5, 'music3')

    """
    The steady patter of rain against the carriage's canopy mingles with the sound of the horse's hooves stomping through the wet mud.


    Moisture from the air sticks to you;{cps=4} {/cps}the rain helps it drip down your collar.
    """

    show plo neutral at left:
        subpixel True pos (-0.04, 1.45) zoom 1.44 
    with Dissolve(1.5)

    "[plo_name] sits at the front,{cps=4} {/cps}reins loose in his hands and{cps=4} {/cps}eyes half-lidded as he watches the road ahead."


    "You sit next to him in peaceful silence as the party makes its way through the thick forest."

    show plo angry

    $ renpy.music.set_volume(0.7, 7, 'music2')
    $ renpy.music.set_volume(1, 6, 'music4')

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
            "[plo_name] grunts in approval."
            Plo "Nothing worse than an itchy shell."  
            show plo happy
            "[plo_name] flashes you a smile before focusing back on the road."  
            Iris "And here I thought you were going to be miserable out here."  
            show plo neutral
            Plo "Eh, only if it were .{cps=4} {/cps}It's the heat that's the problem."  
            "A second of silence passes before Plo's face scrunches."
            show plo angry
            Plo "That{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} and sand."  
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
            show plo_inventory
            window hide
            pause (2.0)
            "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            menu:
                "Praise his packing skills":
                    hide plo_inventory
                    Iris "You{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} really thought of everything."
                    Iris "How did you even get all that to fit in there?"  
                    show plo blush
                    Plo "The amount of supply runs i've gone on you pick up some things."
                    show plo happy
                    Plo "You get to know whats {i}really{/i} essential."
                    $ plo_points += 3
                    jump continue8


                "Question his choices":
                    hide plo_inventory
                    Iris "I'm not sure a lot of that is necessary{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
                    show plo angry
                    Plo "Hmph."
                    show plo neutral
                    Plo "What would a human know about packing anyway."
                    Plo "Of course I gotta bring my childhood basking rock."
                    $ plo_points -= 3
                    jump continue8


    label continue8:


    "[plo_name]'s eyes remain scanning the muddy road ahead."
    pause(1.5)
    with vpunch

    "A comfortable silence dawns on you and your party as the carriage rocks gently beneath you."
    pause(1.5)

    "The road begins to narrow as the mud deepens beneath the horse's hooves."  

    show plo angry


    Plo "The road is getting bad{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} I'm afraid one of the carriage wheels is going to-"
    show plo shocked
    with vpunch
    pause(0.05)
    with hpunch
    pause(0.05)
    with vpunch

    $ renpy.music.stop(channel='music1', fadeout=1)
    $ renpy.music.stop(channel='music2', fadeout=1)
    $ renpy.music.stop(channel='music3', fadeout=1)
    $ renpy.music.stop(channel='music4', fadeout=1)

    """
    The carriage lurches forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.


    The horse strapped to the vehicle lets out an annoyed whine while stomping its feet.
    """


    Plo "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Get stuck in the mud."


    show plo angry


    Plo "Great.{cps=4} {/cps}Just great."  
   
    "You hear a muffled voice from inside the carriage"


    Darcey "Damnit,{cps=4} {/cps}I knew he would."


    
    "[plo_name] groans,{cps=4} {/cps}jumping down and already stepping toward the wheels."
    show plo neutral at jumpAnim

    scene bg forest 
    show carriage back:
        right
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
   
    "[quinn_name] and [darcey_name] quickly emerge from the carriage,{cps=4} {/cps}the former worried and the latter annoyed."

    Quinn "[player_name],{cps=4} {/cps}[plo_name],{cps=4} {/cps}are you alright?"
    show quinn neutral
    show iris sad

    Iris "We are fine,{cps=4} {/cps}its wheels got stuck in the mud."

    jump WheelInMud


######################
## wheel in mud
######################    
    label WheelInMud:

    """

    The rain continues to patter against the leaves as the carriage is stuck on the muddy path.


    The party finds themselves past a winding road,{cps=4} {/cps}precariously close to a steep drop.
    """


    show darcey neutral
    show quinn neutral


    Darcey "Figures."

    show plo angry

    show iris neutral
       
    Iris "[plo_name],{cps=4} {/cps}how long will this take to fix?"

    show plo neutral

    "[plo_name] waves away the concern."

    Plo "Nothing I can't fix,{cps=4} {/cps}just give me a min' I got just the thing."



    if get_serious == False:
        show darcey angry
        Darcey "If you had things under control,{cps=4} {/cps}it wouldn't have gotten stuck!"
        show plo angry
        Plo "I can't control the weather!"
        show darcey neutral
        Darcey "You could have at least planned to keep us on the road!"
        show plo neutral:
            jumpAnim
        Plo "What am I gonna do, fly over it?{cps=4} {/cps}I'm a turtle not a bird!"
        show plo angry
        "[plo_name] points at the cliffs edge without losing [darcey_name]'s eye contact."
        Plo "If you had the reins,{cps=4} {/cps}we'd be down the ravine!"
        show iris shocked:
            jumpAnim
        Iris "Guys,{cps=4} {/cps}enough{cps=4}!"
        show iris happy
        Iris "This situation isn't ideal,{cps=4} {/cps}but arguing and placing blame won't unstick the wheel.{cps=4} {/cps}Besides,{cps=4} {/cps}think of this as a chance to bond."
        show quinn happy
        show plo neutral
        Plo "Bond,{cps=4} {/cps}eh?"
        "[plo_name] looks back at [darcey_name]."
        show plo happy
        Plo "You should go push the stuck wheel out from the mud.{cps=4} {/cps}It'll help our {i}bond{/i}."
        show darcey happy
        Darcey "Sure,{cps=4} {/cps}we wouldn't want the senior to pull something."
        show iris neutral
        Iris "And no fighting!"
        show quinn neutral
        show darcey neutral
        Darcey "As you wish,{cps=4} {/cps}[player_name]."
        show darcey angry
        show plo happy
        "As [darcey_name] turns to go,{cps=4} {/cps}she gives [plo_name] one last dirty look.{cps=4} {/cps}He's too busy grinning."
        show darcey neutral
    else:
        Iris "[darcey_name],{cps=4} {/cps}let's get behind and help push."
        show darcey angry
        "[darcey_name]'s anger,{cps=4} {/cps}though strong,{cps=4} {/cps}only appears for a brief second before being subdued."
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
    Quinn "[player_name],{cps=4} {/cps}a moment please."
    show quinn sad


    menu:
        "Stay and help [plo_name].":
            $ plo_points += 5
            show iris neutral
            Iris "I'm sorry,{cps=4} {/cps}[quinn_name],{cps=4} {/cps}but we have pressing matters here."
            Quinn "I understand."
            "[quinn_name] nods then heads off towards the forest line."
            "[player_name] approaches [plo_name] ready to help in the front.{cps=4} {/cps}[plo_name]'s hand stops her."
            Plo "We are fine,{cps=4} {/cps}[player_name].{cps=4} {/cps}Go see what the kid needs."
            show plo happy
            Plo "[darcey_name] and I have this handled."
            
            show plo neutral:
                subpixel True 
                xpos 1.0 
                linear 0.28 xpos 1.47 
            with Pause(0.40)
            show plo angry:
                xpos 1.47 
            "With [plo_name]'s reassurance,{cps=4} {/cps}you make your way over to the forest where [quinn_name] waits."
            jump continue9


        "Go and see what [quinn_name] wants at the perimeter.":
            $ quinn_points += 3
            "The look on [quinn_name]'s face worries you."
            Iris "[plo_name],{cps=4} {/cps}[darcey_name],{cps=4} {/cps}work on getting this carriage free while [quinn_name] and I check the perimeter."
            show plo happy
            Plo "Roger,{cps=4} {/cps}[player_name]."
            show plo neutral:
                subpixel True 
                xpos 1.0 
                linear 0.28 xpos 1.47 
            with Pause(0.40)
            show plo angry:
                xpos 1.47 
            show iris happy
            Iris "No fighting."
            "[quinn_name] leds you to the forest line."
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
    show carriage back:
        subpixel True 
        xpos 1.0 
        linear 0.24 xpos 1.6 
    with Pause(0.48)
    show iris neutral:
        xpos 0.59 
    show quinn neutral:
        xpos -0.0 

    show quinn neutral
    Quinn "As I was securing the area,{cps=4} {/cps}I found these."
    show quinn sad
    
    "Quinn points at the mud below."
    window auto hide
    show footprints with Dissolve(1.5)
    pause(3.0)
    """
    A series of deep footprints press into the mud.{cps=4} {/cps}They remain distinct despite the rain.
   
    Their unevenness suggests that the owner of the prints was moving quickly.
    """

    Quinn "Fresh.{cps=4} {/cps}I have never seen any footprint pattern like this from our camp."
    hide footprints with Dissolve(1.5)

    "You take a sharp breath.{cps=4} {/cps}[plo_name] and [darcey_name]'s distant bickering muffles in the rain."

    show iris worried
    Iris "This can't be right{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} Nothing should be out here for miles.{cps=4} {/cps}We're still close to the base."

    menu:
        "We should investigate.":
            show iris worried
            Iris "We need to investigate.{cps=4} {/cps}Enemy soldiers have never been this close to base before."
            Iris "Something isn't right."
            $ quinn_points += 10
            jump Investigate


        "We can't stray from our given task.":
            show iris worried
            Iris "It is concerning but{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            show iris neutral
            Iris "We don't know how far the enemy went or what direction.{cps=4} {/cps}Getting the letter to the castle is more important than a wild goose chase."
            Iris "Right now we need to get the carriage back on the road."
            jump DontInvestigate


######################
## investigate
######################  
    label Investigate:


    show quinn sad
    Quinn "Since these footprints are fresh,{cps=4} {/cps}there is a good chance they are still nearby."
   
    menu:
        "They could be hostile.":
            show iris sad
            Iris "We should find them quickly.{cps=4} {/cps}Last thing we need is more trouble."
            show iris neutral
            jump continue11


        "They could be in trouble.":
            show iris sad
            Iris "We should see if they need our help.{cps=4} {/cps}It would be shameful not to consider that."
            show iris neutral
            show quinn worried
            Quinn "Okay,{cps=4} {/cps}be we need to be careful.{cps=4} {/cps}If these tracks belong to an enemy scout,{cps=4} {/cps}we can't afford to be ambushed."
            show quinn neutral
            jump continue11


    label continue11:

    "You and [quinn_name] head back to the carriage.{cps=4} {/cps}To your surprise,{cps=4} {/cps}[plo_name] and [darcey_name] are working together to free the wheels."

    play amb3 rain_amb fadein 8 volume 0.6
    stop amb1 fadeout 20
    stop amb2 fadeout 20

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
    show carriage back:
        subpixel True 
        xpos 1.6 
        linear 0.29 xpos 1.0       
    with Pause(0.40)
    show carriage back:
        xpos 1.0 

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
    show carriage back:
        jumpAnim
    with Pause(0.18)
    with hpunch

    "The carriage lurches forward with the last coordinated thrust,{cps=4} {/cps}freeing it from the mud."

    "The sudden momentum sends [darcey_name] stumbling forward with a muttered curse,{cps=4} {/cps}but she manages to steady herself."

    show iris happy
    Iris "See? Teamwork."

    show darcey angry
    Darcey "You couldn't have been gentler,{cps=4} {/cps}[plo_name]?"

    show plo happy
    Plo "Bah.{cps=4} {/cps}Gentle.{cps=4} {/cps}We're not giving it a massage."

    show quinn sad
    "[quinn_name] is the only one distracted from the small victory.{cps=4} {/cps}His sharp gaze lingers on the treeline,{cps=4} {/cps}where shadows shift amongst the trees."

    show iris neutral
    "[player_name] follows his line of sight."

    show iris worried
    Iris "We found a set of footprints on the forest's edge."

    show darcey worried:
        unflip
        subpixel True 
        xpos 0.98 
        linear 0.30 xpos 0.86 
    with Pause(0.40)
    "[darcey_name]'s expression shifted to stoic seriousness.{cps=4} {/cps}Her eyes follow [quinn_name]'s to the darkened forest."

    Darcey "Footprints?{cps=4} {/cps}Out here?{cps=4} {/cps}We're supposed to be the only ones stupid enough to take this route."

    show plo worried:
        flip
    Plo "They fresh?"

    show quinn neutral
    Quinn "Fresh enough.{cps=4} {/cps}And not from our camp."

    "A quiet moment passes,{cps=4} {/cps}leaving the sound of the rain pattering against leaves.{cps=4} {/cps}They listen.{cps=4} {/cps}Nothing unusual presents itself."

    show plo worried
    Plo "I don't like this."

    show iris worried
    Iris "The sooner we move,{cps=4} {/cps}the sooner we get answers."

    show quinn sad
    Quinn "The rain's picking up.{cps=4} {/cps}If we're going to follow those tracks,{cps=4} {/cps}we need to move now before they are washed away."

    show iris neutral
    Iris "Right.{cps=4} {/cps}Everyone stay alert."

    show plo 
    Plo "I'll stay back.{cps=4} {/cps}Someone has to keep watch of all our stuff."

    Iris "Alright,{cps=4} {/cps}stay safe [plo_name]."

    
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

    play amb1 rain_forest_amb fadein 3 volume 0.6
    stop amb3 fadeout 20

    $ renpy.music.play("audio/music/03 Tension Clar.ogg", channel='music1', loop=True, synchro_start=True, fadein=2, tight=True)
    $ renpy.music.play("audio/music/03 Tension Accomp.ogg", channel='music2', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/03 Tension Trem.ogg", channel='music3', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/03 Tension Cello.ogg", channel='music4', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/03 Tension Low.ogg", channel='music5', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.set_volume(0.8, delay=0.2, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0, delay=0, channel='music3')
    $ renpy.music.set_volume(0, delay=0, channel='music4')
    $ renpy.music.set_volume(0, delay=0, channel='music5')

    scene bg forest_clearing
    show rain1fast zorder 1
    show rain2fast zorder 0
    with Dissolve(1.5)

    "The forest is thick with mist with only the scent of damp wood in the air." 
    "You,{cps=4} {/cps}[darcey_name],{cps=4} {/cps}and [quinn_name] follow the footprints between trees,{cps=4} {/cps}further from the main road."
    "The air gets heavier with every step.{cps=4} {/cps}The group proceeds in silence."

    show darcey neutral at right 
    show quinn neutral at left
    show iris neutral at right:
        subpixel True xpos 0.73 
    with Dissolve(1.5)

    "The footprint tracks gradually turned from ordered to scattered.{cps=4} {/cps}You and your team stop."

    $ renpy.music.set_volume(0.5, delay=8, channel='music2')

    show darcey worried
    Darcey "Something doesn't feel right{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} These tracks have changed."

    show quinn sad
    Quinn "It appears that whoever we're tracking started running without direction."


    show iris worried
    Iris "Injured?{cps=4} {/cps}Or maybe running from something?"

    "Your team continues onward."
    
    "A wind gust traveling through the forest hits them off guard.{cps=4} {/cps}You manage to keep on your feet until it passes,{cps=4} {/cps}arms crossed in front of you as a shield."
    "You turn to check on everyone else.{cps=4} {/cps}[darcey_name] keeps her ground.{cps=4} {/cps}[quinn_name] is knocked over but not hurt."
    "You notice somethig else.{cps=4} {/cps}An underbrush shuddered,{cps=4} {/cps}revealing nothing behind it."
    "The path through opens into a small clearing.{cps=4} {/cps}In the middle is a broken-down carriage."

    $ renpy.music.set_volume(0, delay=20, channel='music1')
    $ renpy.music.set_volume(0.9, delay=4, channel='music2')
    $ renpy.music.set_volume(0.6, delay=6, channel='music3')
    $ renpy.music.set_volume(0.7, delay=6, channel='music4')

    $ renpy.music.set_volume(0.4, delay=20, channel='amb1')
    
    "Its wooden frame is cracked as if it was struck with force.{cps=4} {/cps}Pieces of torn cloth and scattered supplies litter the ground."


    show iris shocked
    show darcey shocked
    Iris "That's not a good sign."


    "[quinn_name] approaches the carriage to search for clues."


    show quinn neutral
    show darcey neutral
    Quinn "Nothing left,{cps=4} {/cps}but someone was here recently."

    #$ renpy.music.set_volume(0, delay=20, channel='music2')
    #$ renpy.music.set_volume(1, delay=4, channel='music3')
    #$ renpy.music.set_volume(1, delay=6, channel='music4')
    #$ renpy.music.set_volume(0.7, delay=4, channel='music5')
    # kept for reference to copy into each menu choice


    "You crouch next to a deep gash made in the carriage's wood,{cps=4} {/cps}running your fingers along it.{cps=4} {/cps}This wasn't made by weather damage;{cps=4} {/cps}this was cut."
    show iris neutral
    menu:
        "Check inside the carriage.":
            "Carefully,{cps=4} {/cps}you step onto the cracked wooden frame to peer inside."

            "You see torn seats and papers and bags left in disarray.{cps=4} {/cps}A faint smear of blood stains the inside of the far door."

            $ renpy.music.set_volume(0, delay=20, channel='music2')
            $ renpy.music.set_volume(1, delay=4, channel='music3')
            $ renpy.music.set_volume(1, delay=6, channel='music4')
            $ renpy.music.set_volume(0.7, delay=4, channel='music5')

            show darcey neutral
            Darcey "How did they manage to get a carriage this far off the path?"

            jump inspect


        "Search the scattered supplies outside.":
            "Carefully,{cps=4} {/cps}you kneel next to the debris,{cps=4} {/cps}sifting through them."
            "You inspect a torn bag that's spilling rations,{cps=4} {/cps}a broken lantern,{cps=4} {/cps}and a necklace with a strange emblem carved into its gem."

            show iris shocked
            Iris "This symbol{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} [quinn_name],{cps=4} {/cps} does this look familiar?"

            $ renpy.music.set_volume(0, delay=20, channel='music2')
            $ renpy.music.set_volume(1, delay=4, channel='music3')
            $ renpy.music.set_volume(1, delay=6, channel='music4')
            $ renpy.music.set_volume(0.7, delay=4, channel='music5')

            show quinn shocked
            Quinn "It does."
            show quinn neutral
            show iris neutral
            Quinn "This carriage belonges to the enemy."

            menu:
                "Pick up the necklace":
                    "You put the necklace into your pocket for now."
                    #TODO: something here to get the item
                "Leave the necklace":
                    "It's best not to steal from them.{cps=4} {/cps}The war is ending."
            jump inspect
   
    label inspect:

    "You expand your inspection of the surrounding area for more clues,{cps=4} {/cps}but keep [darcey_name] and [quinn_name] in sight."

    show quinn worried

    Quinn "That's strange.{cps=4} {/cps}I don't recognize this foliage."

    "[darcey_name] approaches."
    show iris neutral behind darcey:
        flip
    show darcey shocked:
        subpixel True 
        xpos 1.0 
        linear 0.80 xpos 0.52 
    with Pause(0.85)

    show darcey worried

    Darcey "I thought there wasn't a single blade of grass you couldn't identify this side of the mountain."

    show darcey neutral
    "She pokes around it then,{cps=4} {/cps}feeling dread growing inside her,{cps=4} {/cps}stabs through one of its leaves with her spear."

    stop music1 fadeout 1.0
    stop music2 fadeout 1.0
    stop music3 fadeout 1.0
    stop music4 fadeout 1.0
    stop music5 fadeout 1.0

    "Rustling sounds echo but not from the trees.{cps=4} {/cps}In union,{cps=4} {/cps}it grows louder and louder {cps=4} {/cps}followed by a sudden sharp {i}snap{/i}."

    show darcey shocked
    Darcey "What the{cps=4}-{/cps}{cps=4}!{/cps}{cps=4}?{/cps}"

    $ renpy.music.play("audio/music/04 Danger Winds.ogg", channel='music1', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/04 Danger Leads.ogg", channel='music2', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/04 Danger Str.ogg", channel='music3', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/04 Danger Brass.ogg", channel='music4', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/04 Danger Trom.ogg", channel='music5', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/04 Danger Perc.ogg", channel='music6', loop=True, synchro_start=True, fadein=1, tight=True)
    $ renpy.music.play("audio/music/04 Danger Timp.ogg", channel='music7', loop=True, synchro_start=True, fadein=0.05, tight=True)

    $ renpy.music.set_volume(0, delay=0, channel='music1') # Winds 1
    $ renpy.music.set_volume(0, delay=0, channel='music2') # Leads 2
    $ renpy.music.set_volume(0, delay=0, channel='music3') # Str 3
    $ renpy.music.set_volume(1, delay=0, channel='music4') # Brass 4
    $ renpy.music.set_volume(1, delay=0, channel='music5') # Trom 5
    $ renpy.music.set_volume(0.7, delay=0, channel='music6') # Perc 6
    $ renpy.music.set_volume(0.7, delay=0, channel='music7') # Timp 7

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
    
    $ renpy.music.set_volume(0.3, delay=8, channel='music2') # Leads 2
    $ renpy.music.set_volume(0.7, delay=4, channel='music3') # Str 3
    $ renpy.music.set_volume(0, delay=4, channel='music4') # Brass 4
    $ renpy.music.set_volume(0.7, delay=0, channel='music5') # Trom 5
    $ renpy.music.set_volume(0.7, delay=0, channel='music6') # Perc 6
    $ renpy.music.set_volume(0.7, delay=0, channel='music7') # Timp 7


    "Before anyone can react,{cps=4} {/cps}thick,{cps=4} {/cps}gnarled vines burst from the underbrush you entered through and wrapped around [darcey_name]'s leg.{cps=4} {/cps}She is yanked off her feet within seconds."


 
    show darcey angry
    Darcey "Son of a—!"  
    Darcey "Get this thing off me!"

    $ renpy.music.set_volume(0.3, delay=8, channel='music1') # Winds 1
    $ renpy.music.set_volume(0.5, delay=6, channel='music2') # Leads 2
    $ renpy.music.set_volume(0, delay=2, channel='music5') # Trom 5
    $ renpy.music.set_volume(0, delay=2, channel='music7') # Timp 7

    "The vine tightens as she protests,{cps=4} {/cps}dragging her toward the dark mass of writhing roots forming.{cps=4} {/cps}The ground shifts.{cps=4} {/cps}Something huge is moving beneath the mud."


    show quinn sad at jumpAnim
    Quinn "[darcey_name]!{cps=4} {/cps}It's a Hydra Vine!"

    show iris angry
    Iris "Hold on,{cps=4} {/cps}[darcey_name]!"
    show quinn angry

    play sfx1 arrow volume 1

    show arrow1 at CutIn
    with vpunch
    pause(0.5)
    show arrow1 at CutOut
    pause(0.25)
    hide arrow1
    pause(0.25)

    play sfx1 arrow_deflect volume 0.7

    show vine1 at CutIn
    with vpunch
    pause(0.5)
    show vine1 at CutOut
    pause(0.25)
    hide vine1
    "[quinn_name] shoots his bow,{cps=4} {/cps}but the plant flings the arrow away."

    play sfx1 knife_vine_1 volume 0.4

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

    "[darcey_name] struggles to hack the vine with her knife.{cps=4} {/cps}Her blade barely cuts through the thick,{cps=4} {/cps}pulsing roots.{cps=4} {/cps}Its coils tighten."

    $ renpy.music.set_volume(0, delay=10, channel='music1') # Winds 1
    $ renpy.music.set_volume(0, delay=6, channel='music2') # Leads 2
    $ renpy.music.set_volume(0, delay=6, channel='music3') # Str 3
    $ renpy.music.set_volume(0.5, delay=6, channel='music4') # Brass 4
    $ renpy.music.set_volume(0.8, delay=2, channel='music7') # Timp 7


    show iris worried
    Iris "I have to do something!"


    menu:
        "Use the dagger to cut her free.":
            "You lunge forward,{cps=4} {/cps}grabbing the nearest sharp object{cps=4}-{/cps}{cps=4}-{/cps}a dagger made out of a shard of wood--to stab at the vine gripping [darcey_name]'s leg.{cps=4} {/cps}You are desperate."

            play sfx1 knife_vine_2 volume 0.7

            show sword1 at CutIn
            with vpunch
            pause(0.5)
            show sword1 at CutOut
            pause(0.25)
            hide sword1

            "The plant lets out a horrible,{cps=4} {/cps}guttural {i}scream{/i} as sap sprays from the wound.{cps=4} {/cps}But the vine doesn't loosen."

            show vine2 at CutIn
            with vpunch
            pause(0.5)
            show vine2 at CutOut
            pause(0.25)
            hide vine2
            "Where the plant was cut sprouted two more vine-like appendages."

            menu:
                "Keep cutting anyway.":
                    "You grit your teeth and keep hacking as the vines writhe.{cps=4} {/cps}One of them wraps around your wrist."

                    play sfx1 knife_vine_3 volume 0.7

                    show sword2 at CutIn
                    with vpunch
                    pause(0.5)
                    show sword2 at CutOut
                    pause(0.25)
                    hide sword2

                    "Acidic sap oozes onto your skin.{cps=4} {/cps}A scream couldn't encapsulate the pain you jolt in."

                    "[darcey_name] screams as she's yanked deeper,{cps=4} {/cps}halfway inside the plant's writhing mass."

                    show iris shocked
                    "You try to focus on her.{cps=4} {/cps}The mission.{cps=4} {/cps}[quinn_name] and [plo_name].{cps=4} {/cps}Anything.{cps=4} {/cps}Your vision fades."

                    "[quinn_name] is too late rushing in as the vines constrict with a sickening {i}snap{/i}."

                    jump bad_ending

                "Call for help instead.":
                    $ renpy.music.set_volume(0.3, delay=6, channel='music2') # Leads 2
                    $ renpy.music.set_volume(0, delay=10, channel='music4') # Brass 4
                    $ renpy.music.set_volume(0.5, delay=2, channel='music6') # Perc 6
                    $ renpy.music.set_volume(0.5, delay=2, channel='music7') # Timp 7
                    "You back off then shout for [quinn_name]."

                    Iris "It keeps regenerating!"

                    "[quinn_name]'s second arrow is already flying through the air at that shout.{cps=4} {/cps}The vines twist in midair in coordinated response to use [darcey_name] as a shield."

                    play sfx1 arrow volume 0.7

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

                    "[quinn_name] steps back to clear his head.{cps=4} {/cps}He yells toward [player_name]."

                    Quinn "Since we can't pierce the vines,{cps=4} {/cps}our only option is fire!"

                    #if
                    #you have fire starter good 

                    "You remember seeing a fire starter in the remainds of the carriage earlier,{cps=4} {/cps}quickly you sprint over and shuffle through the grass to find it."

                    Iris "[quinn_name]!"

                    "Without a word [quinn_name] catches it masterfully then quickly strikes his ready arrows aflame.{cps=4} {/cps}Each one launches at the vine hydra in succession."

                    play sfx1 arrow volume 0.7
                    play sfx2 ["<silence 0.15>", arrow] volume 0.5
                    play sfx3 ["<silence 0.3>", fireball_vine] volume 0.5
                    
                    show fire at CutIn
                    with vpunch
                    pause(0.5)
                    show fire at CutOut
                    pause(0.25)
                    hide fire
                    pause(0.25)

                    "The plant withers in pain as they hit.{cps=4} {/cps}A horrifying screech echoes throughout the forest.{cps=4} {/cps}[darcey_name] gets dropped in the process."

                    achieve hot

                    $ renpy.music.set_volume(0, delay=4, channel='music2') # Leads 2
                    $ renpy.music.set_volume(0.5, delay=4, channel='music3') # Str 3
                    $ renpy.music.set_volume(0, delay=2, channel='music6') # Perc 6
                    $ renpy.music.set_volume(0, delay=2, channel='music7') # Timp 7

                    
                    window auto hide
                    show darcey angry:
                        subpixel True 
                        pos (1.12, 0.73) rotate -180.0 
                        linear 0.10 pos (1.14, 1.46) rotate -90.0 
                    with Pause(0.20)
                    show darcey angry:
                        pos (1.14, 1.46) rotate -90.0 
                    window auto show


                    "[darcey_name] drops to the ground with a gasp,{cps=4} {/cps}coughing."

                    Darcey "Ouch{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

                    play sfx1 arrow volume 0.4
                    show arrow1 at CutIn
                    with vpunch
                    pause(0.5)
                    show arrow1 at CutOut
                    pause(0.25)
                    hide arrow1
                    pause(0.25)

                    "[quinn_name]'s last shot fells the viny creature,{cps=4} {/cps}dead.{cps=4} {/cps}He runs to Darcey."

                    
                    window auto hide
                    show quinn angry:
                        subpixel True 
                        xpos 0.0 
                        linear 0.10 xpos 0.47 
                    with Pause(0.20)
                    show quinn angry:
                        xpos 0.47 

                    $ darcey_tired = True

                    stop music1 fadeout 10
                    stop music2 fadeout 10
                    stop music3 fadeout 10
                    stop music4 fadeout 10
                    stop music5 fadeout 10
                    stop music6 fadeout 10
                    stop music7 fadeout 10        

                    jump aftermath

                    #Else
                    "[darcey_name] screams as she's yanked deeper,{cps=4} {/cps}halfway inside the plant's writhing mass."

                    show iris shocked
                    Iris "No,{cps=4} {/cps}no,{cps=4} {/cps}no!"

                    "[quinn_name] is too late rushing in as the vines constrict with a sickening {i}snap{/i}."

                    jump bad_ending
        #TODO: locked choice ONLY IF U HAVE FLUTE!
        "Try to use magic.":
            
            stop music1 fadeout 5
            stop music2 fadeout 5
            stop music3 fadeout 5
            stop music4 fadeout 5
            stop music5 fadeout 5
            stop music6 fadeout 5

            $ renpy.music.set_volume(0.5, delay=6, channel='music7') # Timp 7

            $ magic_score += 1
            
            "You reach into your pack,{cps=4} {/cps}hands trembling,{cps=4} {/cps}and pull out your carved flute."

            show iris worried

            $ renpy.music.play("audio/music/05 Magic Shaky.ogg", channel='music1', loop=True, synchro_start=True, fadein=1, tight=True)
            $ renpy.music.play("audio/music/05 Magic Flute.ogg", channel='music2', loop=True, synchro_start=True, fadein=1, tight=True)
            $ renpy.music.play("audio/music/05 Magic Winds.ogg", channel='music3', loop=True, synchro_start=True, fadein=1, tight=True)
            $ renpy.music.play("audio/music/05 Magic High.ogg", channel='music4', loop=True, synchro_start=True, fadein=1, tight=True)
            $ renpy.music.play("audio/music/05 Magic Cello.ogg", channel='music5', loop=True, synchro_start=True, fadein=1, tight=True)
            $ renpy.music.play("audio/music/05 Magic Str.ogg", channel='music5', loop=True, synchro_start=True, fadein=1, tight=True)

            $ renpy.music.set_volume(0.6, delay=0, channel='music1') # Shaky 1
            $ renpy.music.set_volume(0, delay=0, channel='music2') # Flute 2
            $ renpy.music.set_volume(0, delay=0, channel='music3') # Winds 3
            $ renpy.music.set_volume(0, delay=0, channel='music4') # High 4
            $ renpy.music.set_volume(0, delay=0, channel='music5') # Cello 5
            $ renpy.music.set_volume(0, delay=0, channel='music6') # Str 6
            stop music7 fadeout 20
            

            "The melody trembles at first in shaky adrenaline.{cps=4} {/cps}But it swiftly finds its tune,{cps=4} {/cps}notes cutting through the fog like silver thread."

            play sfx1 fireball volume 0.5

            show magic1 at CutIn
            with hpunch
            pause(0.5)
            show magic1 at CutOut
            pause(0.25)
            hide magic1

            $ renpy.music.set_volume(0.3, delay=3, channel='music4') # High 4

            "Magic stirs around you,{cps=4} {/cps}drawn to the song."
            "The plant coils tighter at the sight."

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

            $ renpy.music.set_volume(0, delay=4, channel='music1') # Shaky 1
            $ renpy.music.set_volume(0.8, delay=3, channel='music2') # Flute 2

            menu:
                "Aim carefully and cast what you have.":

                    $ renpy.music.set_volume(0.5, delay=4, channel='music4') # High 4
                    $ renpy.music.set_volume(0.3, delay=6, channel='music5') # Cello 5
                    $ renpy.music.set_volume(0.3, delay=6, channel='music6') # Str 6

                    "With your flute in hand,{cps=4} {/cps}you steady your breath to focus."

                    play sfx1 fireball_vine volume 0.6
                    
                    show magic2 at CutIn
                    with hpunch
                    pause(0.5)
                    show magic2 at CutOut
                    pause(0.25)
                    hide magic2

                    "The magic surges ferociously,{cps=4} {/cps}but,{cps=4} {/cps}this time,{cps=4} {/cps}it finds its mark."

                    "The vines shriek and shrivel when struck.{cps=4} {/cps}The burning parts turn to ash right before your eyes."

                    $ renpy.music.set_volume(0.5, delay=8, channel='music2') # Flute 2
                    $ renpy.music.set_volume(0.4, delay=4, channel='music3') # Winds 3
                    $ renpy.music.set_volume(1, delay=4, channel='music6') # Str 6

                    window auto hide
                    show darcey angry:
                        subpixel True 
                        pos (1.12, 0.73) rotate -180.0 
                        linear 0.10 pos (1.14, 1.46) rotate -90.0 
                    with Pause(0.20)
                    show darcey angry:
                        pos (1.14, 1.46) rotate -90.0 
                    window auto show

                    "[darcey_name] drops to the ground with a gasp,{cps=4} {/cps}coughing."

                    Darcey "Ouch{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

                    play sfx1 arrow volume 0.4

                    show arrow1 at CutIn
                    with vpunch
                    pause(0.5)
                    show arrow1 at CutOut
                    pause(0.25)
                    hide arrow1
                    pause(0.25)

                    "[quinn_name] takes one last shot before running to Darcey."

                    
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

                    $ renpy.music.set_volume(1, delay=2, channel='music1') # Shaky 1
                    $ renpy.music.set_volume(0, delay=4, channel='music2') # Flute 2
                    

                    show iris 
                    "You shut your eyes.{cps=4} {/cps}All your fear and desperation swell into the spell.{cps=4} {/cps}It's unmanageable."

                    "It explodes from you."
                    show iris shocked
                    show quinn shocked
                    show darcey shocked

                    stop music1 fadeout 1
                    stop music2 fadeout 1
                    stop music3 fadeout 1
                    stop music4 fadeout 1
                    stop music5 fadeout 1
                    stop music6 fadeout 1

                    play sfx1 fireball volume 0.7

                    show magic3 at CutIn
                    with hpunch
                    pause(0.5)
                    show magic3 at CutOut
                    pause(0.25)
                    hide magic3
                    with vpunch
                    with hpunch

                    "It isn't just the vines that disintegrates.{cps=4} {/cps}The trees,{cps=4} {/cps}nature,{cps=4} {/cps}enemy's carriage.{cps=4} {/cps}It's all gone to soot."

                    "[quinn_name] and [darcey_name] are displaced.{cps=4} {/cps}They lay unconscious meters from where they once were."

                    "Your last surge of raw mana detonates at your feet,{cps=4} {/cps}hurling you hard to the ground.{cps=4} {/cps}Everything starts to go black."

                    achieve boom

                    "The last thing you hear is rain."

                    jump bad_ending

    label aftermath:
    
    $ renpy.music.set_volume(0, delay=2, channel='music2') # Flute 2
    #$ renpy.music.set_volume(0, delay=0, channel='music3') # Winds 3
    $ renpy.music.set_volume(0.1, delay=6, channel='music4') # High 4
    $ renpy.music.set_volume(0.5, delay=6, channel='music5') # Cello 5
    #$ renpy.music.set_volume(0, delay=0, channel='music6') # Str 6
    
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



    "[darcey_name] carefully dusts herself off.{cps=4} {/cps}She winces when she rolls her red and sore ankle.{cps=4} {/cps}It still had the imprint of the vines."

    show darcey sad
    Darcey "Next time,{cps=4} {/cps}let's not follow the creepy footprints {i}directly into a monster's trap{/i}."

    "[quinn_name] sighs in relief and ignores [darcey_name]'s quip."

    show quinn sad
    show iris neutral
    Quinn "What matters right now is that you're okay."

    "The adrenaline still shivers down your spine as you glance back at the abandoned enemy carriage.{cps=4} {/cps}You shack your head."

    show iris angry
    Iris "We need to get back to our carriage now,{cps=4} {/cps}back on our mission."

    "No one says anything after that.{cps=4} {/cps}You notice that the forest feels heavier{cps=4} {/cps}like something is still watching."
    show iris neutral
    show darcey neutral

    "[darcey_name] leans on you for support as she limps forward.{cps=4} {/cps}You carefully help her navigate the drenched ground." 


    "[quinn_name] trails close behind with bow ready."

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

    $ renpy.music.set_volume(0, delay=2, channel='music3') # Winds 3
    $ renpy.music.set_volume(0.3, delay=6, channel='music4') # High 4
    $ renpy.music.set_volume(0.3, delay=6, channel='music5') # Cello 5
    $ renpy.music.set_volume(0.3, delay=6, channel='music6') # Str 6

    stop amb1 fadeout 8
    play amb2 rain_amb fadein 4 volume 0.5

    scene bg forest
    show rain1slow zorder 1
    show rain2slow zorder 0
    show plo happy:
        right   
        flip
    with Dissolve(1.5)

    "The carriage comes back into view,{cps=4} {/cps}comforting your team after the chaos."
    
    "[plo_name] got it back on the road.{cps=4} {/cps}The sound of freefall rain combines with the sound of it pattering on the carriage's canvas roof."

    
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
    "[plo_name]'s easygoing expression falters the moment he sees [darcey_name] limping beside you."

    Plo "What happened out there?"

    show darcey sad
    Darcey "Just encountered a clingy plant{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

    "The exhaustion in [darcey_name]'s voice is clear as it trails off."

    show plo sad
    Plo "You alright?"

    show darcey neutral
    Darcey "I'll live."

    $ renpy.music.set_volume(0, delay=10, channel='music4') # High 4

    "[plo_name] nods; his grin becoming forced.{cps=4} {/cps}He steps forward and guides her toward the carriage with an unspoken gentleness."

    show plo neutral
    Plo "Up you go then.{cps=4} {/cps}No arguments."

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
        Plo "Come on,{cps=4} {/cps}everyone in.{cps=4} {/cps}Storytime will have to wait until we're free from this place's surprise."
    else:
        Plo "[player_name],{cps=4} {/cps}appreciate the company,{cps=4} {/cps}but you should ride inside this time."
        Plo "Humans and rain don't mix too well,{cps=4} {/cps}last I checked."
        "With a softer voice,{cps=4} {/cps}he leans down."
        show plo neutral:
            subpixel True 
            pos (1.0, 1.18) xrotate 0.0 rotate 0.0 
            linear 0.60 pos (0.99, 1.16) xrotate 0.0 rotate -9.0 
        with Pause(0.70)
        show plo neutral:
            pos (0.99, 1.16) xrotate 0.0 rotate -9.0 


        Plo "Keep an eye on [darcey_name],{cps=4} {/cps}will ya?{cps=4} {/cps}She looks shaken up."

    $ renpy.music.set_volume(0, delay=10, channel='music5') # Cello 5
    $ renpy.music.set_volume(0, delay=10, channel='music6') # Str 6

    Iris "Let's get out of here."

    stop amb2 fadeout 6
    play amb3 rain_carriage_amb fadein 3 volume 0.8

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

    Iris "[darcey_name]{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} Are you sure you're okay?"

    show darcey sad
    Darcey "Yeah,{cps=4} {/cps}just sore.{cps=4} {/cps}I've had worse.{cps=4} {/cps}Probably."

    menu:
        "Crack a joke to lighten the mood.":
            Iris "Personally,{cps=4} {/cps}I don't think man-eating vines were the best welcome from the local flora."
            show darcey happy
            Darcey "Who knows,{cps=4} {/cps}this could be top service from enchanted forests.{cps=4} {/cps}I'm flattered."
            show quinn happy
            Quinn "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}I'll write a strongly-worded letter."
            $ quinn_points += 10
            $ darcey_points += 5

        "Offer to keep an eye on [darcey_name].":
            Iris "Rest.{cps=4} {/cps}I'll keep watch until you're recovered.{cps=4} {/cps}You've done enough today."
            $ quinn_points += 10
            $ darcey_points += 5
            show darcey happy
            show quinn neutral
            Darcey "Thanks.{cps=4} {/cps}I'll try not to fall asleep on your shoulder."

        "Stay quiet, but keep close.":
            "You keep quiet,{cps=4} {/cps}only offering [darcey_name] your arm as she climbs in."
            show darcey neutral
            "She gives you a brief but grateful glance."
            $ quiet += 1
            $ quinn_points += 5
            $ darcey_points += 5
            show quinn neutral
            show darcey happy
            Darcey "I guess the forest thought a bush was too obvious of an ambush."
            show quinn happy 
            Quinn "Hmph."
    
    stop amb3 fadeout 10
    jump Uphill

######################
## don't investigate
######################  
    label DontInvestigate:
    
    play amb3 rain_amb fadein 5 volume 0.5
    stop amb1 fadeout 20
    stop amb2 fadeout 20
    
    Quinn "Of course,{cps=4} {/cps}apologies [player_name]."

    "You and [quinn_name] head back to the carriage.{cps=4} {/cps}To your surprise,{cps=4} {/cps}[plo_name] and [darcey_name] are working together to free the wheels."
    
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

    $ renpy.music.play("audio/music/02 Journey Harp.ogg", channel='music1', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/02 Journey Clar.ogg", channel='music2', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/02 Journey Accomp.ogg", channel='music3', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/02 Journey Celli.ogg", channel='music4', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/02 Journey Tamb.ogg", channel='music5', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/02 Journey Bodhran.ogg", channel='music6', loop=True, synchro_start=True, tight=True)
    $ renpy.music.play("audio/music/02 Journey Vln.ogg", channel='music7', loop=True, synchro_start=True, tight=True)
    $ renpy.music.set_volume(0, 0, channel='music1')
    $ renpy.music.set_volume(0, 0, channel='music2')
    $ renpy.music.set_volume(0, 0, channel='music3')
    $ renpy.music.set_volume(0, 0, channel='music4')
    $ renpy.music.set_volume(0.5, 0.1, 'music5')
    $ renpy.music.set_volume(0.2, 0.1, 'music6')
    $ renpy.music.set_volume(0, 0, channel='music7')
    
    "The carriage lurches forward with the last coordinated thrust,{cps=4} {/cps}freeing it from the mud."

    "The sudden momentum sends [darcey_name] stumbling forward with a muttered curse,{cps=4} {/cps}but she manages to steady herself."

    show darcey angry
    Darcey "You couldn't have been gentler,{cps=4} {/cps}[plo_name]?"

    show plo happy
    Plo "Bah.{cps=4} {/cps}Gentle.{cps=4} {/cps}We're not giving it a massage."

    show darcey neutral
    Darcey "Whatever.{cps=4} {/cps}Let me back on this thing so I can fufill the mission."
    show darcey angry:
        subpixel True 
        xpos 0.98 
        linear 0.30 xpos 1.3 
    with Pause(0.40)

    show quinn sad
    "[quinn_name] is the only one distracted from the small victory.{cps=4} {/cps}His sharp gaze lingers on the treeline,{cps=4} {/cps}where shadows shift amongst the trees."
    
    "Nevertheless,{cps=4} {/cps}he gets in the carriage."
    
    show iris neutral
    show quinn sad:
        subpixel True 
        xpos 0.03 
        linear 0.60 xpos 1.03 
    with Pause(0.70)

    $ renpy.music.set_volume(1, 3, 'music2')
    $ renpy.music.set_volume(0.8, 3, 'music3')
    $ renpy.music.set_volume(0, 6, 'music6')

    if inside_carriage == True:
        show plo neutral:
            flip
        Plo "Alright,{cps=4} {/cps}everyone in?{cps=4} {/cps}Let's get movin' before the road throws us another surprise."
    else:
        show plo neutral:
            flip
        Plo "[player_name],{cps=4} {/cps}appreciated the company,{cps=4} {/cps}but you should ride inside this time."
        Plo "Humans and rain don't mix too well,{cps=4} {/cps}last I checked."
        Plo "Makes them all sick."
    show iris happy
    Iris "Will do."

    stop amb3 fadeout 10
    play amb1 rain_carriage_amb fadein 2 volume 0.8

    scene bg forest
    show carriage 
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

    $ renpy.music.set_volume(0.6, 4, 'music5')
    $ renpy.music.set_volume(0.7, 0.2, 'music1')

    "You settle into the carriage.{cps=4} {/cps}Rain drips from all three of you.{cps=4} {/cps}It's nice to be inside."

    if get_serious == False:
        Iris "Remind me to thank the horse later.{cps=4} {/cps}If we survive this,{cps=4} {/cps}it gets half my rations and a name."

        show darcey happy
        show quinn happy
        Darcey "Better guarantee a title and pension with how bumpy [plo_name] is driving."

        show quinn neutral
        Quinn "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}Their pace is impressive."

        "You laugh faintly. "

        "Tension creeps in as the wheels begin to grind harder,{cps=4} {/cps}the incline steeper."
    else:
        """
        Time passes.
        The weight of what's ahead gets to you.{cps=4} {/cps}Time slows.
        [quinn_name] and [darcey_name]'s voices blend into the background.{cps=4} {/cps}Their words get muffle by your thoughts.{cps=4} {/cps}You stare out the window,{cps=4} {/cps}lost in the passing landscape.
        Uncertainty of what's to come makes the world outside feel distant and cold.
        """
    "The forest outside morphs into rocky outcrops and mud slick ridges."

    "The carriage jolts."

    $ renpy.music.set_volume(0, 1, 'music1')
    $ renpy.music.set_volume(0, 1, 'music2')
    $ renpy.music.set_volume(0, 1, 'music3')
    $ renpy.music.set_volume(0.8, 0.2, 'music4')
    $ renpy.music.set_volume(0.5, 4, 'music5')
    $ renpy.music.set_volume(0.8, 0.2, 'music6')

    with hpunch
    show quinn shocked
    show darcey shocked

    "A loud {i}crack{/i} rings out as one of the rear wheels twists to the left.{cps=4} {/cps}The carriage heads toward a narrow ravine."

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

    Iris "Whoa!"
    
    show darcey angry
    Darcey "[plo_name]?!"
    show quinn sad
    Quinn "We're sliding!"

    "[plo_name] yells from outside."

    $ renpy.music.set_volume(1, 1, 'music2')

    Plo "I KNOW!"

    Plo "Everyone {i}lean right!{/i}{cps=4} {/cps}NOW!"
    with hpunch

    $ renpy.music.set_volume(1, 1, 'music7')
    $ renpy.music.set_volume(1, 1, 'music3')

    "You,{cps=4} {/cps}[darcey_name],{cps=4} {/cps}and [quinn_name] throw your weight to the right side of the carriage as [plo_name] wrestles with the reins.{cps=4} {/cps}The horses whine in panic."

    "The carriage shudders{cps=4}.{/cps}{cps=4}.{/cps}{cps=4} {/cps} then steadies.{cps=4} {/cps}Right on the edge of a cliff."
    
    "A few pebbles tumble off the edge below you into the fog."

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

    $ renpy.music.set_volume(0.5, 4, 'music4')
    $ renpy.music.set_volume(0.2, 4, 'music6')
    $ renpy.music.set_volume(0.7, 4, 'music7')
    
    "A long silence follows."

    show darcey neutral
    Darcey "{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} That counts as our one 'slip down a hill',{cps=4} {/cps}right?"

    show quinn neutral
    Quinn "Technically,{cps=4} {/cps}we didn't {cps=4}fall{/cps}."
    
    Iris "Let's count it to avoid another one."

    $ renpy.music.set_volume(0.2, 4, 'music4')

    show quinn happy
    show darcey happy

    stop amb1 fadeout 20
    play amb2 drizzle_carriage_amb fadein 5 volume 0.6

    "Laughter breaks the tension.{cps=4} {/cps}For a moment,{cps=4} {/cps}the cabin feels warmer."

    "The rain begins to ease outside.{cps=4} {/cps}Trees lessen until disappearing altogether.{cps=4} {/cps}The road evens out and trades mud for coarse,{cps=4} {/cps}sandy ground."

    $ renpy.music.set_volume(0.8, 0.2, 'music1')
    $ renpy.music.set_volume(0.7, 4, 'music3')
    $ renpy.music.set_volume(0, 8, 'music4')
    $ renpy.music.set_volume(0, 8, 'music6')

    menu:
        "Ask [darcey_name] about her worst travel day.":
            $ darcey_points += 5
            Iris "[darcey_name],{cps=4} {/cps}what's the worst travel day you've ever had?"

            $ renpy.music.set_volume(0.7, 1, 'music2')
            $ renpy.music.set_volume(0, 4, 'music3')
            $ renpy.music.set_volume(0, 8, 'music7')
            $ renpy.music.set_volume(0.3, 4, 'music5')

            show darcey happy
            Darcey "Good question!{cps=4} {/cps}I assume today doesn't count."
            show darcey neutral
            Darcey "One time,{cps=4} {/cps}I was escorting a food delivery load.{cps=4} {/cps}The {i}entire{/i} cartload was raw fish and goat milk in glass jars{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            Darcey "...during the blistering summer."

            show quinn worried
            Quinn "I can almost imagine the smell."

            show darcey happy
            show quinn neutral
            Darcey "By the end of the second day,{cps=4} {/cps}even vultures wouldn't come near.{cps=4} {/cps}Took one sniff and ran for the hills."

        "Ask [quinn_name] about his bow reflexes.":
            $ quinn_points += 5
            Iris "[quinn_name],{cps=4} {/cps}how did you get so skilled with your bow?"

            $ renpy.music.set_volume(0.7, 1, 'music2')
            $ renpy.music.set_volume(0, 4, 'music3')
            $ renpy.music.set_volume(0, 8, 'music7')
            $ renpy.music.set_volume(0.3, 4, 'music5')

            show quinn neutral
            Quinn "Being half-elf has its advantages,{cps=4} {/cps}But that doesn't mean your naturally talented.{cps=4} {/cps}Precision comes from years of practice."
            
            Quinn "I've spent countless hours training until it became second nature."

        "Stay quiet and listen to the rain.":
            $ quiet += 1

            $ renpy.music.set_volume(0.7, 1, 'music2')
            $ renpy.music.set_volume(0.4, 8, 'music3')
            $ renpy.music.set_volume(0, 10, 'music5')
            
            "You settle into the quiet moment,{cps=4} {/cps}letting the sound of soft rainfall and creaking wood lull your nerves."

            "[darcey_name] rests her head back."
            show darcey neutral
            Darcey "Almost feels peaceful.{cps=4} {/cps}Almost."

            show quinn neutral
            "[quinn_name] closes his eyes briefly,{cps=4} {/cps}arms crossed,{cps=4} {/cps}hand always near his bow."

            "Silence is broken only by the occasional sound of [darcey_name] or [quinn_name] shifting and the faint hum of the carriage over uneven ground."

            $ renpy.music.set_volume(0, 8, 'music2')
            $ renpy.music.set_volume(0, 8, 'music3')
            $ renpy.music.set_volume(0, 8, 'music7')

            "A memory rises in your mind{cps=4}-{/cps}{cps=4}-{/cps}one you haven't thought of in years{cps=4}-{/cps}{cps=4}-{/cps}as you listen to the rain."

            show black with Dissolve(1.5)
            """
            Ever since you were a child something about magic has always fascinated you,{cps=4} {/cps}but it always alluded you.

            Your father was a mage,{cps=4} {/cps}he left his tomes open at night and you'd always sneak in when he slept to study the sigils.

            He always described to you the wonder of magic,{cps=4} {/cps}how he could feel it as he casted each spell. 
            
            Each one was like a spark of his own soul,{cps=4} {/cps}something so connected and dear to him. 

            It was a wonderful thought to you.

            Just a thought. 

            No matter how hard you tried there was nothing that could stir up a feeling so wholly pure as that. 

            It's a miracle you learned the basics.

            You never minded being drafted in the end if it meant sparing your parents.
            """

            hide black with Dissolve(1.5)

    $ renpy.music.set_volume(0.7, 1, 'music2')

    "A small bump in the road reminds you you're still on the rough road."
    with hpunch

    show darcey happy
    Darcey "Bets on how long until we hit the next 'harmless little bump' in the road?"

    show quinn happy
    Quinn "Do you count the time in minutes or seconds?"

    Iris "I'm starting to think we're jinxed with all these bumps.{cps=4} {/cps}Who cursed our trip?"

    show darcey angry
    Darcey "Probably [plo_name].{cps=4} {/cps}He keeps cursing under his breath at the carriage's every movement."

    stop amb2 fadeout 20

    "[plo_name]'s voice bellows through the canvas."

    Plo "I HEARD THAT!" 
    #TODO: a text effect would be nice here

    show darcey happy

    Darcey "Good!"

    "The air grows drier.{cps=4} {/cps}The smell of the soggy forest floor gives way to the firmer,{cps=4} {/cps}bristly smell of sandy terrain."

    "The sun comes out without plants to cover it.{cps=4} {/cps}Cold is being replaced by the hotness of a desert."

    jump Uphill

######################
## uphill
######################  
    label Uphill:
    #enviroment turns more hot and mixed with sand

    stop music1 fadeout 10
    stop music2 fadeout 10
    stop music3 fadeout 10
    stop music4 fadeout 10
    stop music5 fadeout 10
    stop music6 fadeout 10
    stop music7 fadeout 10
    
    Plo "We'll reach the main merchant path in not too long."

    show quinn neutral

    Quinn "The sun will soon set.{cps=4} {/cps}What would you like to do,{cps=4} {/cps}[player_name]?"

    Iris "Let's camp here for now."
    show darcey happy

    Plo "About time.{cps=4} {/cps}I was starting to think we'd need to start carrying everythin'."

    Plo "It's faster."

    #rain stops
    scene sand
    with Dissolve(1.5)

    pause(1.5)
    
    show plo neutral at left:
        subpixel True xpos 0.11
    show iris happy:
        right
        flip
    show quinn neutral at left:
        subpixel True xpos 0.04 
    show darcey neutral at left:
        flip
        subpixel True xpos 0.01
    with Dissolve(1.5)

    with Pause(0.40)

    "You exit the carriage to find a good spot to rest."

    "You spot a small outcropping of rock offers a natural break from the wind.{cps=4} {/cps}A great place to set up camp."
    
    "Your team gets there as night passes over the sunset."

    #TODO: add the tintshader
    show quinn happy
    Quinn "Well,{cps=4} {/cps}this is as good a place as any for the night."

    play sfx1 tent_place volume 0.3
    queue sfx1 campfire_start volume 0.3

    "The party sets up camp beneath the outcropping.{cps=4} {/cps}[plo_name] unloads gear from the carriage,{cps=4} {/cps}while [quinn_name] works on building a fire with careful,{cps=4} {/cps}practiced hands."

    "The fire crackles softly as night settles.{cps=4} {/cps}The clouds part just enough for the faintest glow of moonlight to break through."

    scene black with Dissolve (2.0)
    #"You have reached the end of the Day 1.{cps=4} {/cps}Look forward to new chapters soon!"
    #jump end

    "After finishing their meals, everyone settles into their evening routine."

    scene sand

    "The desert wind has cooled with hints of the day's warmth beneath your feet."

    Quinn "The temperature is dropping fast. It will be cold by midnight."
    Plo "Finally, a break from the heat."

    "You join the team around the fire. There's an occasional crack of embers and soft rustle of someone's shifting cloak."

    Iris "We'll take turns on watch tonight. I'll go first."

    Darcey "You sure? [plo_name] could do it. He hasn't done much but sit around all day."

    Plo "Bah!"

    Iris "I'm sure. I've got enough energy left in me."

    "The others, after deciding not to argue, settle in their ready-made tents beneath the natural stone overhang." 
    "You adjust your posture by the fire. The flickers of flame dance against the dark horizon."

    "You watch the stars blink to life, one by one."

######################
## night 1
######################  
    label night_1:

    #TODO: how to make this feel like a long time in between? idk
    "Your eyes start to droop."
    "Eventually, it's time to wake someone for the second shift."

    menu:
        "Wake Darcey":
            $ second_watch = "darcey"

            if darcey_tired == True:
                $ darcey_points -= 5
                "You gently nudge [darcey_name] awake."
                Iris "Second shift. You're next."
                Darcey "Fine, but I'm going to hold this against you forever. Or until breakfast."
                "[darcey_name] sighs."
                Darcey "The only thing worse than being attacked by a living plant... night shift."
                jump watch_tired
            elif darcey_tired == False:
                $ darcey_points += 5
                "You gently nudge [darcey_name] awake."
                Iris "Second shift. You're next."
                Darcey "Yeah, yeah, I'm up." 
                Darcey "Leave it to me. Get some rest, [player_name]."
                jump catch_thief

        "Wake Plo":
            $ second_watch = "plo"

            if plo_tired == True:
                $ plo_points -= 5
                "You gently nudge [plo_name] awake."
                Plo "{i}ZzzZZzz{/i}"
                "You nudge [plo_name] again."
                Plo "Mmm, it's in the carriage."
                "You nudge [plo_name]... again."
                Plo "...[player_name]?"
                "He rubs his eyes."
                Iris "Second shift. You're next."
                Plo "Mmm, can do. Can do."
                jump watch_tired
            elif plo_tired == False:
                "You gently nudge [plo_name] awake."
                Plo "...Nope. I'm asleep. This is a dream."
                "You nudge [plo_name] again."
                Plo "Fine, fine! I'm up [player_name]! I'm getting up."
                Iris "Second shift. You're next."
                Plo "Yeah, yeah. Get some shut eye for me."
                jump catch_thief
                
        "Wake Quinn":
            $ second_watch = "quinn"

            if quinn_tired == True:
                "You gently nudge [quinn_name]. He rubs his eyes and sits up."
                Quinn "[player_name]?"
                Iris "Second shift. You're next."
                Quinn "I can manage that. Sleep well."
                jump watch_tired
            elif quinn_tired == False:
                $ quinn_points += 5
                "You gently nudge [quinn_name]. He sits up and immediately understands."
                Quinn "I'll keep watch. Sleep well, [player_name]."
                jump catch_thief

################################################################################
## █▀▄ ▄▀▄ ▀▄▀   ▀█▀ █ █ █ █▀█ 
## █▄▀ █▀█  █     █  ▀▄▀▄▀ █▄█ 
################################################################################

######################
## catch thief
######################  
    label catch_thief:

    scene black with Dissolve(1.5)
    pause 1.0

    "You drift off to sleep. The sounds of the night slip away..."

    centered "Day 2"

    "Frantic footsteps and the startled voices of your companions wake you up."

    "You run out to see what happened."

    Iris "What is going on?"

    if second_watch == "quinn":
        "While you were asleep, I found a thief going through our carriage!"
    elif second_watch == "plo":
        "Perfect timing, [player_name]. Found this little sucker helping themself to our things!"
    elif second_watch == "darcey":
        "I caught this thief red handed!"

    Kobold "P-please, don't hurt me! I only meant-"

    "A small, trembling kobold clutches a carriage wheel, your carriage's wheel, eyes flicking between the angry faces surrounding him."

    "[darcey_name] is pointing her spear at him, pinning him against a tree."

    Darcey "Save it! Who would trust a thief?"

    Iris "Explain yourself. Why do you have our wheel?"

    Kobold "I—I'm sorry! My clan- we're starving!" 
    
    Kobold "I thought... I thought, if I took just one wheel, I could trade it for food."

    Quinn "There are other ways besides stealing. Asking for example."

    Plo "In the middle of the desert at midnight? Hah, you'd be lucky if we handed you a loaf of stale bread."

    Darcey "Save your excuses. You're lucky I didn't spear you where you stood."

    Kobold "No spear, please! I'm truly sorry! I'll make it right—"

    "The kobold bows his head and trembles. For a moment, it seems the tension might ease."

    menu:
        "Trade food for the wheel back":
            $ quinn_points += 3
            Iris "We can give you some rations, just hand the wheel over."
            Kobold "Rations? Really? Thank you! Thank you—"
            Darcey "What? Why would we do that?"
            Iris "[darcey_name]."
            "[darcey_name] steps forward towards the kobold, fishing a few pieces of jerky from her pack."
            Darcey "Here. Take this. But promise you won't come near us again."
            kobold "I promise! Thank you!"
            "[darcey_name] hands over the food and reaches for the wheel. 
            "The kobold has other plans. He quickly scoops up the wheel once he has the food secured and bolts without a word."
            Darcey "HEY!"
            "You shout after him, but he's already halfway down a sandy slope."
            #TODO: animation here, make it feel engaging
            "The kobold trips over a rock. The wheel tumbles from his arms."
            "You hear the sickening snap as the wheel splinters against a nearby stone."
            Kobold "Gah!"
            Plo "OUR WHEEL!"
            "[quinn_name] aims his bow at the fleeing kobold, hesitates, then lowers it."
            "The kobold disappears into the darkness."
            Quinn "No use. Capturing him won't un-break the wheel."
            Darcey "That little liar! I knew we couldn't trust a thief!"

        "Intimidate him into giving it back":
            $ darcey_points += 3
            $ plo_points += 3
            Iris "Drop it and speak quickly, or you'll regret being caught."
            Kobold "Y-yes! Yes, I'll drop it! Please!"
            "He steps back as if to find a suitable distance to lay down the wheel."
            #TODO: animation, him backing away
            "The kobold has other plans. As he turns to flee, the weight of the wheel sends him tumbling and escapes his grip."
            "You hear the wheel splintering as it lands on a stone."
            Kobold "No! My wheel—"
            Plo "{i}OUR{/i} wheel!"
            Darcey "Get back here!"
            "[quinn_name] aims his bow at the fleeing kobold, hesitates, then lowers it."
            Quinn "No use. Capturing him won't un-break the wheel."
            "The kobold disappears into the darkness."
            

    "Dawn breaks over the sand as the party gathers around the shattered wheel."

    #TODO: Show the wheel cg

    Quinn "The wheel... it's completely shattered."

    Plo "Is there a way to fix? No way am I walking all the way in that {i}sand{/i}."

    Darcey "We'll make it work. We've faced worse."

    "The group packs up camp as the sun climbs higher, ready to face the long day ahead."
    "The kobold's fate is unknown, but their own journey must continue."

        

######################
## slept in
######################  
    #label watch_tired:






################################################################################
## █▀▄ ▄▀▄ ▀▄▀ ▀█▀ █▄█ █▀█ █▀▀ █▀▀ 
## █▄▀ █▀█  █   █  █ █ █▀▄ ██▄ ██▄ 
################################################################################




################################################################################
## Endings
################################################################################

######################
## Rolling Credits
###################### 
    label finalcredits:
        scene black
        show screen creditscreen
        pause 100 # or however long it takes to scroll through in a reasonable speed
        pause
        jump end
    screen creditscreen:
        vbox:
            xsize 1000 # horizontal size of the credits
            ysize 2500 # how much vertical space your rolling credits take.
            xalign 0.5
            yalign 0.0
            at transform:
                subpixel True
                easein 50: # or however long it takes to scroll through in a reasonable speed
                    yalign 1.0
            vbox:
                ysize 1000 # enter vertical resolution, so that it starts with an empty screen
            add "images/logo w.png": # adding a picture in-between the text
                zoom 0.75
                xalign 0.5
            text "Don't Shoot the Messenger":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 25
                xalign 0.5
            text "version [config.version]":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 25
                xalign 0.5
            vbox:
                ysize 250 # some empty space in between
            text "Sound Design":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 55
                xalign 0.5
            text "a_sett":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            text "Andrew Shirey":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            vbox:
                ysize 150 # some empty space in between
            text "Music":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 45
                xalign 0.5
            text "a_sett":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            vbox:
                ysize 150 # some empty space in between
            text "Programming":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 55
                xalign 0.5
            text "William Rockwell":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            text "indecisiv":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            vbox:
                ysize 150 # some empty space in between
            text "Art":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 55
                xalign 0.5
            text "Revierr":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            vbox:
                ysize 150 # some empty space in between
            text "Writing":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 55
                xalign 0.5
            text "indecisiv":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            text "KhaosPhoenix":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            vbox:
                ysize 150 # some empty space in between
            text "Special Thanks":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 55
                xalign 0.5
            text "Arimia":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            text "bobcgames":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 35
                xalign 0.5
            vbox:
                ysize 350 # some empty space in between
            add "images/rp logo bw.png": # adding a picture in-between the text
                zoom 0.55
                xalign 0.5
            text "Made with Ren'Py":
                font "Bellefair-Regular.ttf"
                #bold True
                size 35
                xalign 0.5
            text "Version [renpy.version_only]":
                font "Bellefair-Regular.ttf"
                #bold True
                size 25
                xalign 0.5
            vbox:
                ysize 650 # some empty space in between
            add "images/letter.png": # adding a picture in-between the text
                zoom 2.0
                xalign 0.5
            text "The End":
                font "Bellefair-Regular.ttf"
                color "#7c3131"
                bold True
                size 100
                xalign 0.5
            vbox:
                ysize 300 # some empty space in between

######################
## Bad Ending
###################### 
    label bad_ending:

        stop amb1 fadeout 6
        stop amb2 fadeout 6
        stop amb3 fadeout 6

        stop music1 fadeout 10
        stop music2 fadeout 10
        stop music3 fadeout 10
        stop music4 fadeout 10
        stop music5 fadeout 10
        stop music6 fadeout 10
        stop music7 fadeout 10

        scene black with Dissolve(1.5)
        if sprite_image == "f_iris":
            show game_over_f
            with Dissolve(1.5)
        elif sprite_image == "m_iris":
            show game_over_m
            with Dissolve(1.5)

        show text "{size=110}Game Over{/size}":
            subpixel True ypos 0.12 
        with Dissolve(1.5)
        " "
        window auto hide
        achieve badend
        jump end

#keep this the very last line of code##############################################
label end:
