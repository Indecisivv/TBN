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
    label intro:
    
    """
    Deep within a vast cave system,{cps=4} {/cps}warmed by the geothermal currents of an underground aquifer,{cps=4} {/cps}lies your camp.

    The ever-present humidity and dirt clings to your skin. 
    
    Stalactites loom overhead,{cps=4} {/cps}glistening with mineral-rich condensation.

    You are called urgently to the captain's chamber.{cps=2} {/cps}An unusual call this late.{cps=2} {/cps}It sets a nervous edge to your steps.

    You make your way through the winding tunnels,{cps=4} {/cps}the torchlight casting restless shadows against the jagged walls. 
    
    Heated water hisses through the fissures above.
    
    When you finally reach the chamber,{cps=4} {/cps}the air is thick with the scent of damp rock.

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

    The torchlight barely reaches the tent flap as a massive figure ducks beneath it,{cps=4} {/cps}his broad shell scraping the fabric's edge. 
    
    A figure steps inside,{cps=4} {/cps}his weathered green skin illuminated by the dim glow,{cps=4} {/cps}deep grooves and ridges marking the passage of time across his form.
    """
    Plo "{i}Can't let this old man get his sleep after a hard days work?{/i}"

    """
    His heavy-lidded eyes scan the room with the slow deliberation of a veteran who's seen more than his fair share of orders. 
    
    With a sigh he straightens his thick frame gives the captain a curt salute.
    """

    Plo "Captain."

    Captain "At ease Plo,{cps=4} {/cps}I wouldn't drag a grumpy old tortle like you this late without good reason."

    $ plo_name = "Plo"

    Plo "{i}Suuure{/i} you wouldn't."

    "Plo gives a sarcastic snort."

    "Only a second passes before the tent door flutters open once more."

    show plo happy at MoveToLeft
    
    show darcey happy with Dissolve(1.5) 
    #TODO: pan around character image

    """
    A short,{cps=4} {/cps}red-skinned tiefling strides in next,{cps=4} {/cps}her presence like a blade—sharp,{cps=4} {/cps}poised,{cps=4} {/cps}and unwavering.

    She stands with military discipline.
    
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

    His eyes glancing between the others,{cps=4} {/cps}pausing briefly on the tiefling with a nod of acknowledgment,{cps=4} {/cps}before locking onto the captain.

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

    Captain "I have a very important message that needs to be delivered.{cps=2} {/cps}You four will be the ones delivering it."

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
            $ quiet += 1
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

    Captain "That is why im entrusting this mission to you,{cps=4} {/cps}Sergeant [player_name]."

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
    
    The air here is warmer,{cps=4} {/cps}the proximity to the aquifer making it thick with humidity and body heat.

    Despite the subterranean shelter,{cps=4} {/cps}exhaustion clings to your bones like the damp air itself.
    """ 

    scene bg bg3 with Dissolve(1.5)

    #TODO: pan around the tent bg
    """
    
    The stifling air inside the soldier's tent is thick with sweat and dirt,{cps=4} {/cps}clinging to your skin like a second layer of grime. 
    
    The canvas walls do little to shield you from the humid night,{cps=4} {/cps}the smell of damp straw body odor pressing in from all sides of the tent. 
    
    Half a dozen exhausted soldiers lay cramped like sardines in haphazardly built bunk beds.
    
    A single lantern,{cps=4} {/cps}its flame weak and flickering,{cps=4} {/cps}casts shifting shadows along the tent's sagging ceiling.

    This was the life of a conscripted solider.
    
    The few still awake glance up as you return.
    """

    Bunkmate "What was that about? You get in trouble?"

    "Your bunkmate above you shifts,{cps=4} {/cps}eyes filled with concern."

    menu:
        "Be honest":
            Iris "Actually,{cps=4} {/cps}I have great news!"
            "You lean in,{cps=4} {/cps}lowering your voice so as not to wake anyone."
            Iris "The Captain will announce the end of the war in the morning."
            Bunkmate "NO WAY!!"
            "They nearly shout before clapping both hands over their mouth."
            Iris "Shh,{cps=4} {/cps}I have to pack{cps=4}—{/cps}I'm leaving on a mission this morning"
            Bunkmate "This is so huge{cps=4} {/cps}I'm not going to be able to sleep tonight!{cps=2} {/cps}Good luck [player_name]!"
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
    
    You take a moment to look at the map the Captain entrusted to you.

    """
    ##TODO: show map!!! ##

    """

    A trip to the capital wouldn't take too long if you cut through the mountain path.

    Three days,{cps=4} {/cps}maybe less if you're quick.

    It would be best to pack enough food and supplies for at least twice that.

    Quietly you reach under the bunk to pull out your stuff.

    """

    ##TODO: show inventory packing here!!! ##

    """
    You decide to get what little rest you still can.
    """


    
################################################################################
## █▀▄ ▄▀▄ ▀▄▀   █▀█ █▄ █ █▀▀ 
## █▄▀ █▀█  █    █▄█ █ ▀█ ██▄ 
################################################################################
    label day1:
    
    scene bg black with Dissolve(1.5)
    
    centered "Day 1"
    
    """
    It's still early in the morning as you make your way to the designated meeting spot.

    Soldiers move about groggily,{cps=4} {/cps}some returning from night patrols,{cps=4} {/cps}others preparing for the day ahead.

    """
    scene bg cave with Dissolve(1.5)

    """
    Your small party gathers near the supply tent,{cps=4} {/cps}where a wooden carriage,{cps=4} {/cps}tied to a sturdy draft horse,{cps=4} {/cps}stands ready.

    The cold chill blows into the cave{cps=4} {/cps}the smell of rain and mud wafts in.

    Plo is already there and securing the last of the crates onto the back of the carriage.
    """

    show plo happy
    
    Plo "Cart's packed and ready.{cps=2} {/cps}Not much,{cps=4} {/cps}but it'll get us there."

    show quinn neutral

    Quinn "The rain looks intense."

    show quinn sad

    Quinn "At this rate our journey might be hindered by the mud."

    show plo happy at jumpAnim

    Plo "A little rain won't bother me."

    Plo "Rain or shine you can trust that I {i}will{/i} be driving that carriage."

    "Darcey approaches,{cps=4} {/cps} a bag in hand and a dignified smirk on her face."

    Darcey "Yeah,{cps=4} {/cps} just try not to get us stuck in a ditch,{cps=4} {/cps}alright?"

    show plo angry

    Plo "As if {i}you{/i} would handle it any better."

    show plo happy

    Plo "Maybe a little rain would put out your fire-like temper."

    show darcey angry

    Darcey "Hey,{cps=4} {/cps}I'd have us halfway there already if I was in charge."

    show darcey neutral

    show quinn happy

    Quinn "Halfway down a ravine maybe,{cps=4} {/cps}I don't seem to recall you ever driving a carriage before..."

    Darcey "You're supposed to have {i}my{/i} back here."

    menu:
        "Joke around":
            ##TODO: eed to finish ##
            Iris ""
            $ quinn_points += 5
            $ darcey_points += 5
            $ plo_points += 5
            jump continue4

        "It's time to get serious":
            show iris neutral
            Iris "We don't have time for this,{cps=4} {/cps}guys."
            show darcey angry
            show plo neutral
            show quinn neutral
            Iris "This mission holds the lives of many people in our hands."
            show darcey sad
            Darcey "Apologies,{cps=4} {/cps}[player_name]."
            "Darcey looks apologetic,{cps=4} {/cps}embarrassed of her unknightly behavior."
            $ quinn_points += 3
            "Plo awkwardly shuffles towards the carriage to get away."
            ##TODO: ANImaTion here!!! ##
            $ plo_points -= 3
            $ get_serious = True
            jump continue4

        "Say nothing":
            $ quiet += 1
            jump continue4
    
    label continue4:


    """
    The conversation trails off as the sound of rain tapping against the cave mouth grows louder.

    Quinn's eyes narrow slightly as he glances toward the road ahead.
    """

    Quinn "We shouldn't waste any more time."

    Quinn "The longer we wait the worst it will be."

    Plo "Alright,{cps=4} {/cps}alright.{cps=2} {/cps}Let's get this thing on the road."

    "Plo packs the final crate and secures the latch on the carriage."

    Iris "Let's not waste any more time.{cps=2} {/cps}Mount up."

    """
    Darcey and Quinn enter the carriage.

    As Quinn steps in,{cps=4} {/cps}he turns around and glances at you with the door propped open.
    
    """
    
    Quinn "Getting in,{cps=4} {/cps}[player_name]?"

    menu:
        "Sit inside":
            Iris "Yes,{cps=4} {/cps}Let's head in then."
            $ quinn_points += 5
            $ darcey_points += 5
            jump InsideCarriage

        "Guard outside":
            Iris "You two head in,{cps=4} {/cps}I'll help guard outside alongside Plo."
            Plo "Not afraid of the rain?"
            Plo "Well,{cps=4} {/cps}let's get a move on then."
            Quinn "As you wish."
            "Quinn shuts the door behind them."
            $ plo_points += 5
            jump OutsideCarriage
      
######################
## inside carriage
###################### 
    label InsideCarriage:

    scene bg InsideCarriage with Dissolve(1.5)

    """
    You climb into the carriage,{cps=4} {/cps}settling into the slightly worn wooden seat.

    The inside of the carriage is dim,{cps=4} {/cps}the patter of rain muffled by the canvas roof.
    """

    show quinn neutral at left
    show darcey happy at right

    Darcey "So,{cps=4} {/cps}Major [player_name]... you're the one in charge now. Got any words of wisdom before we roll out?"
    menu:
        "Keep it lighthearted":
            Iris "Just try not to kill each other before we get there,{cps=4} {/cps}alright?"  
            "Darcey laughs,{cps=4} {/cps}while Quinn gives a small,{cps=4} {/cps}knowing smile."  
            Darcey "I'll be on my best behavior." 
            Quinn "How encouraging of you." 
            $ darcey_points += 5
            $ quinn_points += 3

        "Be serious":
            Iris "This mission is too important for any distractions. Stay focused."  
            """
            Darcey's smile fades slightly. 
            
            Quinn gives a small nod of approval.
            """
            Quinn "Understood."  
            $ darcey_points += 2
            $ quinn_points += 5

    """
    Time passes in silence,{cps=4} {/cps}the rain not letting up.
    """

    menu:
        "Ask Quinn about the path ahead":  
            label path:
            $ quinn_points += 5
            Iris "What's the terrain like ahead?"
            Quinn "Rough. Mud at first,{cps=4} {/cps}then gravel. It'll get better once we hit the main road."  
            "Darcey sighs."
            Darcey "Let's hope Plo's steering is as good as his bragging." 
            jump continue5

        "Ask about Darcey and Plo":
            Iris "What's the deal between you and Plo?"
            "Darcey sighs,{cps=4} {/cps}lowering her voice to a whisper."
            Darcey "Let's just say he does not exactly act like a model soldier,{cps=4} {/cps}he's not the kind of person who cares about being on someone's bad side."
            "Quinn hits her softly with his elbow scoldingly."
            Quinn "He has a good heart when it matters." 
            jump continue5

        "Sit Quietly":
            """
            You settle back,{cps=4} {/cps}listening to the sound of the rain.

            Quinn's eyes remain half-lidded as Darcey hums softly under her breath.

            The rhythmic sway of the carriage mixed with the patter of rain creates a drowsy sort of calm.
            """
            Quinn "Something on your mind,{cps=4} {/cps}[player_name]?"
            menu:
                "Ask about path ahead.":
                    jump path

                "Nothing.":
                    Iris "Nothing much..."

                    if quiet >= 2:
                        "Darcey studies you for a moment,{cps=4} {/cps}her gaze steady but not probing."  
                        Darcey "You don't talk much,{cps=4} {/cps}do you?"
                        menu:
                            "I'm not much of a talker.":
                                Iris "I'm more of a listener."  
                                Darcey "That's not a bad thing." 
                                "Darcey's gaze lingers on you for a moment longer before she looks toward the window." 
                                Darcey "Sometimes quiet company is better."   
                                $ darcey_points += 5 
                                jump continue5 

                            "Say nothing.":
                                Darcey "Pfft."
                                $ quinn_points += 5  
                                $ darcey_points += 5
                                jump continue5  
                    else:
                        Quinn "Alright." 
                        "Quinn studies you for a moment,{cps=4} {/cps}his gaze steady but not probing." 
                        jump continue5
                    jump continue5
    label continue5:

    "The conversation fades into a comfortable silence as the carriage rocks gently beneath you."

    Darcey "So,{cps=4} {/cps}what do you think about-" 
    #TODO: shake screen

    """
    You feel the carriage lurch forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.

    You hear a horse's annoyed neigh from outside.
    """

    Darcey "Damnit,{cps=4} {/cps}I knew he would." 
    
    Iris "That does not sound good..."

    "You,{cps=4} {/cps}Quinn,{cps=4} {/cps}and Darcey quickly make your way out of the carriage."

    Quinn "Plo,{cps=4} {/cps}are you alright?"

    Plo "I am,{cps=4} {/cps}but I can't say the same for the carriage."

    Plo "One of the wheels got stuck in the mud..."

    jump continue6
######################
## outside carriage
###################### 
    label OutsideCarriage:

    scene bg OutsideCarriage with Dissolve(1.5)
    ##TODO: rain effect here
    """
    The steady patter of rain against the canopy above mingles with the sound of the horse's hooves stomping through the wet mud path.

    The air is thick with moisture,{cps=4} {/cps}and the occasional gust of wind sends moisture sliding down your collar.

    "Plo sits at the front,{cps=4} {/cps}reins loose in his hands,{cps=4} {/cps}eyes half-lidded as he watches the road ahead."

    You sit side by side in peaceful silence as you make your way through the thick forest.
    """

    Plo "Rain's picking up…" 

    menu:
        "Make small talk.":
            $ plo_points += 5
            Iris "Lovely weather today,{cps=4} {/cps}huh?"
            Plo "Haha!" 
            Plo "It is actually quite nice for tortle folk like myself." 
            Plo "Keeps the shell from drying out."
            Iris "Is that so?"  
            Plo "Yes,{cps=4} {/cps}nothing worse than an itchy shell."  
            "Plo flashes you a smile before focusing back on the road."  
            Iris "And here I thought you were just happy to see the sun gone."  
            Plo "Eh. The sun's not so bad. It's the heat that's the problem."  
            Plo "That... and sand."  
            Iris "You don't like sand?"  
            Plo "It gets {i}everywhere{/i}."  
            jump continue8

        "Talk about the mission.":
            Iris "Did you pack everything you needed for the mission last night?"
            Plo "Barely had any time to get this prepared,{cps=4} {/cps}so I just packed the essentials."
            ##the joke is that his inventory is filled with junk, ill make a graphic for this
            show ploinventory
            Iris "Essentials?" 
            menu:
                "Praise his packing skills":
                    Iris "You... really thought of everything I guess."
                    Iris "How did you even get all that to fit in there?"  
                    Plo "The amount of supply runs i've gone on you pick up some things."
                    Plo "You get to know whats {i}really{/i} essential."
                    $ plo_points += 3
                    jump continue8

                "Question his choices":
                    Plo "Hmph."
                    Plo "What would a human know about packing,{cps=4} {/cps}anyway."
                    $ plo_points -= 3
                    jump continue8

    label continue8:

    "Plo's eyes remain sharp,{cps=4} {/cps}scanning the muddy road ahead."

    "The road begins to narrow as the mud deepens beneath the horse's hooves."   

    Plo "The road is getting bad... I'm afraid one of the carriage wheels is going to-"
    #TODO: shake screen

    """
    You feel the carriage lurch forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.

    The horse strapped to the vehicle lets out an annoyed whine and stomps its feet.
    """

    Plo "Get stuck in the mud..."

    show plo angry

    Plo "Great. Just great."  
    
    "You hear a muffled voice from inside the carriage"

    Darcey "Damnit,{cps=4} {/cps}I knew he would." 

    """
    Plo groans,{cps=4} {/cps}jumping down and already stepping toward the wheel.
    
    Quinn and Darcey quickly emerge from the carriage,{cps=4} {/cps}worry written on both their faces.
    """ 

    Quinn "[player_name],{cps=4} {/cps}Plo,{cps=4} {/cps}are you alright?"

    Iris "We are fine,{cps=4} {/cps}a wheel got stuck in the mud."

    jump continue6
######################
## wheel stuck in mud
######################     
    label continue6:

    
    Darcey "Hah,{cps=4} {/cps}figures."
    #wip
        
    Iris "Plo,{cps=4} {/cps}how long will this take to fix?"

    Plo "Nothing I can't fix,{cps=4} {/cps}just give me a minute I got just the thing."
    #wip


    







################################################################################
## █▀▄ ▄▀▄ ▀▄▀   ▀█▀ █ █ █ █▀█ 
## █▄▀ █▀█  █     █  ▀▄▀▄▀ █▄█ 
################################################################################


################################################################################
## █▀▄ ▄▀▄ ▀▄▀ ▀█▀ █▄█ █▀█ █▀▀ █▀▀ 
## █▄▀ █▀█  █   █  █ █ █▀▄ ██▄ ██▄ 
################################################################################
