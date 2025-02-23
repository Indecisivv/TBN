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
define Iris = Character("[player_name]", color="#ffffff")
define Plo = Character("[plo_name]", color="#ffffff")
define Darcey = Character("[darcey_name]", color="#ffffff")
define Quinn = Character("[quinn_name]", color="#ffffff")
#side characters
define Officer = Character("Officer", color="#ffffff")
define Captain = Character("Captain", color="#ffffff")
define Bunkmate = Character("Bunkmate", color="#ffffff")



################################################################################
##  ████   ███  █   █ █████   █████ █████  ███  ████  █████ 
##  █     █   █ ██ ██ █       █       █   █   █ █   █   █   
##  █  ██ █████ █ █ █ ████    █████   █   █████ ████    █   
##  █   █ █   █ █   █ █           █   █   █   █ █   █   █   
##   ███  █   █ █   █ █████   █████   █   █   █ █   █   █   
################################################################################
label start:
    
    # object initialization 
    #define test_object = item("Coin","This is a description", 1, 2, 5, "R")
    #define test_object4 = item("Iron","This is a description", 2, 3, 1, "L")

    #jump DebugIntro

    # Name characterS
    $ player_name = renpy.input("What would you like to name your character?", default="Iris", length=20).strip()

    if player_name == "":
        $ player_name = "Iris"

################################################################################
## ▀█▀ █▄ █ ▀█▀ █▀█ █▀█ 
## ▄█▄ █ ▀█  █  █▀▄ █▄█ 
################################################################################
    
    """
    Deep within a vast cave system,{cps=4} {/cps}warmed by the geothermal currents of an underground aquifer,{cps=4} {/cps}lies your camp.

    The ever-present humidity and dust clings to your skin. 
    
    Stalactites loom overhead,{cps=4} {/cps}glistening with mineral-rich condensation.

    You are called urgently to the captain's chamber.{cps=2} {/cps}An unusual call this late.{cps=2} {/cps}It sets a nervous edge to your steps.

    You make your way through the winding tunnels,{cps=4} {/cps}the flickering torchlight casting restless shadows against the jagged walls. 
    
    When you finally reach the chamber,{cps=4} {/cps}the air is thick with the scent of damp rock and the distant hiss of heated water through the fissures.

    You step in.
    """
    #TODO: maybe like a step sfx here

    scene bg bg2 with Dissolve(1.5)

    #TODO: pan around captains chambers

    """
    The captain's chamber is spacious compared to the cramped alcove you just left.

    The warm air moves slightly here,{cps=4} {/cps}carrying with it the scent of burning oil lamps and damp parchment.
    
    A sturdy wooden desk dominates the space,{cps=4} {/cps}littered with maps and smudged reports. 
    
    The scent of ink,{cps=4} {/cps}sweat,{cps=4} {/cps}and something vaguely metallic lingers in the air. 
    """

    show iris happy at left
    show captain at right 
    with Dissolve(1.5)

    """
    The captain himself looks worn,{cps=4} {/cps}dark circles under his eyes betraying the long hours spent hunched over paperwork. 
    
    He barely glances up as you enter.

    You give him a quick salute and announce your presence.
    """

    Iris "Captain."

    Captain "[player_name],{cps=4} {/cps}wait there for a moment,{cps=4} {/cps}I have more people on their way."

    
    "It doesn't take long before they show."

    show plo happy with Dissolve(1.5)
    #TODO: pan around character image

    """

    The flickering torchlight barely reaches the tent flap as a massive figure ducks beneath it,{cps=4} {/cps}his broad shell scraping the fabric's edge. 
    
    Plo steps inside,{cps=4} {/cps}his weathered green skin illuminated by the dim glow,{cps=4} {/cps}deep grooves and ridges marking the passage of time across his form.
    """
    Plo "{i}Can't let this old man get his sleep after a hard days work?{/i}"

    """
    His heavy-lidded eyes scan the room with the slow deliberation of a veteran who's seen more than his fair share of orders. 
    
    With a sigh that echoes like shifting rock,{cps=4} {/cps}he straightens his thick frame,{cps=4} {/cps}rolling his shoulders with an audible pop before giving the captain a curt salute.
    """

    Plo "Captain."

    Captain "At ease Plo,{cps=4} {/cps}I wouldn't drag a grumpy old tortle like you this late without good reason."

    $ plo_name = "Plo"

    Plo "{i}Suuure{/i} you wouldn't."


    "Only a second passes before the tent door flutters open once more."

    show plo happy at MoveToLeft
    
    show darcey happy with Dissolve(1.5) 
    #TODO: pan around character image

    """
    A short,{cps=4} {/cps}red-skinned tiefling strides in next,{cps=4} {/cps}her presence like a blade—sharp,{cps=4} {/cps}poised,{cps=4} {/cps}and unwavering.

    She stands with military discipline,{cps=4} {/cps}eyes sharp,{cps=4} {/cps}the polished metal of her spear glints against her back.
    
    Her dark eyes flick over the assembled group,{cps=4} {/cps}assessing,{cps=4} {/cps}calculating,{cps=4} {/cps}before settling on the captain with a crisp salute.

    """

    Darcey "Captain."

    #TODO: pan around character image
    #TODO: more screen positions to make everyone fit
    show darcey happy at MoveToLeft 
    show quinn happy with Dissolve(1.5) 
 
    """
    A moment later,{cps=4} {/cps}the final arrival slips inside with quiet efficiency,{cps=4} {/cps}moving like a shadow against the flickering torchlight.

    A lean dark skinned elf,{cps=4} {/cps}his dark cloak still dusted from the cave's passage.

    His sharp eyes flickering between the others,{cps=4} {/cps}pausing briefly on the tiefling with a nod of acknowledgment,{cps=4} {/cps}before locking onto the captain.

    He straightens and offers a salute,{cps=4} {/cps}his voice calm but edged with curiosity.
    """

    Quinn "Captain. Something urgent,{cps=4} {/cps}I assume?"

    Captain "Darcey, Quinn."

    $ quinn_name = "Quinn"
    $ darcey_name = "Darcey"

    """
    The captain straightens in his seat,{cps=4} {/cps}pushing aside a pile of papers and pulling out a letter.

    A pause.

    Then,{cps=4} {/cps}a rare grin.
    """

    Captain "I have a very important message that needs delivered.{cps=2} {/cps}You four will be the ones delivering it."

    show plo happy at jumpAnim
    
    Plo "Hah,{cps=4} {/cps}'bout time I get to be hauling something a little less explosive!"

    menu:
        "What kind of message?":
            Captain "I'm glad you asked{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1

        "Why choose us?":
            #TODO: character image changes
            Captain "Plo,{cps=4} {/cps}the best carriage driver we've got.{cps=2} {/cps}He knows how to handle rough terrain—and rougher company."
            Captain "Quinn,{cps=4} {/cps}a skilled navigator.{cps=2} {/cps}If there's a way through,{cps=4} {/cps}he'll find it."
            Captain "Darcey,{cps=4} {/cps}a fighter through and through.{cps=2} {/cps}Intelligent and deadly." 
            Captain "And of course,{cps=4} {/cps}[player_name],{cps=4} {/cps}the rising star messenger.{cps=2} {/cps}Fast,{cps=4} {/cps}reliable,{cps=4} {/cps}and able to think on their feet."
            Captain "All excellent soldiers in your own rights."
            Captain "You four are the perfect team for this mission because{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1
        
        "Stay Quiet":
            Captain "I summoned you all here today because{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1
    
    label continue1:
    
    "He turns the letter,{cps=4} {/cps}letting the group view it." 
    
    Captain "The enemy sent us this letter of surrender at sundown."

    show darcey happy at happyAnim
    show plo happy at spookedAnim
    
    #TODO: character image changes
    Darcey "{i}Gasp{/i}"

    Quinn "At long last{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

    Captain "There's still work to be done here,{cps=4} {/cps}but we need to send word to the capital immediately"

    Captain "That is why im entrusting this mission to you,{cps=4} {/cps}Major [player_name]."

    menu:
        "Yes,{cps=4} {/cps}Captain!":
            Captain "Good.{cps=2} {/cps}You all are dismissed.{cps=2} {/cps}The others will wake up to good news."
            jump continue2
        
        "Stay Quiet":
            Captain "Alright?{cps=2} {/cps}Alright!{cps=2} {/cps}Get going then,{cps=4} {/cps}I want you guys out of here before morning."
            jump continue2
    
    label continue2:

    Iris "Understood,{cps=4} {/cps}captain."

    """
    Before leaving,{cps=4} {/cps}you glance at your new team.

    They are watching you,{cps=4} {/cps}waiting with eyes filled with anticipation.
    """
    Iris "Let's meet at the camp entrance in 5 hours."

    scene black with dissolve

    """
    You make your way back to your assigned tent.
    
    The tent is no more comfortable than when you left. 
    
    The air here is warmer,{cps=4} {/cps}the proximity to the aquifer making it thick with humidity and body heat.

    Despite the subterranean shelter,{cps=4} {/cps}exhaustion clings to your bones like the damp air itself.
    """ 

    scene bg bg3 with Dissolve(1.5)

    #TODO: pan around the tent bg
    """
    
    The stifling air inside the soldier's tent is thick with sweat and dust,{cps=4} {/cps}clinging to your skin like a second layer of grime. 
    
    The canvas walls do little to shield you from the humid night,{cps=4} {/cps}the smell of damp straw body odor pressing in from all sides of the tent. 
    
    Half a dozen exhausted soldiers lay cramped like sardines in haphazardly built bunk beds.
    
    A single lantern,{cps=4} {/cps}its flame weak and flickering,{cps=4} {/cps}casts shifting shadows along the tent's sagging ceiling.

    This was the life on a conscripted solider.
    
    The few still awake glance up as you return.
    """

    Bunkmate "What was that about? You get in trouble?"

    "Your bunkmate above you shifts, eyes filled with concern."

    menu:
        "Be honest":
            Iris "Actually, I have great news!"
            "You lean in,{cps=4} {/cps}lowering your voice so as not to wake anyone."
            Iris "The Captain will announce the end of the war in the morning."
            Bunkmate "NO WAY!!"
            "They nearly shout before clapping both hands over their mouth."
            Iris "Shh,{cps=4} {/cps}I have to pack{cps=4}—{/cps}I'm leaving on a mission this morning"
            Bunkmate "This is so huger{cps=4} {/cps}I'm not going to be able to sleep tonight!{cps=2} {/cps}Good luck [player_name]!"
            jump continue3

        "Joke around":
            Iris "Yep,{cps=4} {/cps}3 days laundry duty for me."
            Bunkmate "Really?!"
            "You chuckle."
            Iris "No,{cps=4} {/cps}not really."
            Iris "I got assigned a mission,{cps=4} {/cps}you will hear about it in the morning~"
            Bunkmate "Dang{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} that sucks."
            jump continue3
        
        "Be evasive":
            Iris "No,{cps=4} {/cps}I got assigned a mission.{cps=2} {/cps} I leave before sunrise."
            Bunkmate "Dang{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps} that sucks."
            jump continue3
    
    label continue3:

    """
    Quietly you reach under the bunk to pull out your stuff.
    
    You take a moment to look at the map the Captain entrusted to you.

    The camp sits just nestled in enemy territory,{cps=4} {/cps}supporting the front line fighters from a distance.

    A trip to the capital wouldn't take too long if you cut through the mountain path.

    Three days,{cps=4} {/cps}Maybe less if you're quick.

    It would be best to pack enough food and supplies for at least twice that.

    """

    ##TODO: show inventory packing here!!! ##

    """
    You decide to get what little rest you still can.
    """
################################################################################
## █▀▄ ▄▀▄ ▀▄▀   █▀█ █▄ █ █▀▀ 
## █▄▀ █▀█  █    █▄█ █ ▀█ ██▄ 
################################################################################


################################################################################
## █▀▄ ▄▀▄ ▀▄▀   ▀█▀ █ █ █ █▀█ 
## █▄▀ █▀█  █     █  ▀▄▀▄▀ █▄█ 
################################################################################


################################################################################
## █▀▄ ▄▀▄ ▀▄▀ ▀█▀ █▄█ █▀█ █▀▀ █▀▀ 
## █▄▀ █▀█  █   █  █ █ █▀▄ ██▄ ██▄ 
################################################################################
