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
    """
    scene cave with Dissolve(1.5)
    """
    Humidity and dirt clings to your skin as stalactites loom overhead{cps=4} {/cps}with mineral-rich condensation.

    You are called urgently to the Captain's Chamber.{cps=2} {/cps}At this hour in the night? Strange.{cps=2} {/cps}Nervousness creeps into your steps.

    Through winding tunnels, you follow the jagged walls with your torchlight{cps=4} {/cps}. 
    
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

    show iris happy at left
    show captain at right 
    with Dissolve(1.5)

    """
    On closer inspection, you notice the Captain's dark circles under his bloodshot eyes.{cps=4} {/cps}Who knows when he last moved.
    
    He barely reacted to your approach.

    You give him a quick salute and announce your presence.
    """

    Iris "Captain."

    Captain "[player_name],{cps=4} {/cps}wait there,{cps=4} {/cps}I have more people on their way."

    

    show plo happy with Dissolve(1.5)
    #TODO: pan around character image

    """

    You barely notice a torchlight reach the tent flap when a massive figure ducks beneath it.{cps=4} {/cps}His broad shell scraps the fabric on entrance. 
    
    The figure's weathered brown skin was hardened by time.{cps=4} {/cps}The oil lamps revealed its deep grooves and ridges.
    """
    Plo "{i}Can't let this old man get his sleep after a hard days work?{/i}"

    """
    His heavy-lidded eyes scan the room as if routine then approaches. 
    
    He straightens his thick frame and gives the captain a curt salute.
    """

    Plo "Captain."

    Captain "At ease Plo,{cps=4} {/cps}I wouldn't drag you out this late without a good reason."

    $ plo_name = "Plo"

    "Plo gives a sarcastic snort."

    Plo "{i}Right{/i}."

    "Only a second passes before the tent door flutters open once more."

    show plo happy at MoveToLeft
    
    show darcey happy with Dissolve(1.5) 
    #TODO: pan around character image

    """
    A short,{cps=4} {/cps}red-skinned tiefling strides in next.{cps=4} {/cps}You swore you feel the air stop at her presence, afraid to move disrespectfully.{cps=4} {/cps}She approached the desk poised and unwavering.

    She stands at attention.
    
    Her dark eyes flick over the assembled group,{cps=4} {/cps}assessing,{cps=4} {/cps}before settling on the captain with a crisp salute.

    """

    Darcey "Captain."

    #TODO: pan around character image
    #TODO: more screen positions to make everyone fit
    show darcey happy at MoveToLeft 
    show quinn happy with Dissolve(1.5) 
 
    """
    The final arrival slips inside quickly after.{cps=4} {/cps}The extra shadow against the torchlight is what made you notice.

    He's a lean dark skinned elf whose dark cloak is still dusted from the cave's passage.

    Glancing between the others,{cps=4} {/cps}he only pauses on the tiefling with a nod of acknowledgment{cps=4} {/cps}before facing the captain.

    He offers a salute before speaking.
    """

    Quinn "Captain. Something urgent,{cps=4} {/cps}I assume?"

    Captain "Darcey, Quinn."

    $ darcey_name = "Darcey"
    $ quinn_name = "Quinn"

    Captain "Plo, [player_name]"

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
            Captain "I'm glad you asked{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1

        "Why choose us?":
            #TODO: character image changes
            Captain "Plo,{cps=4} {/cps}the best carriage driver we've got.{cps=2} {/cps}He knows how to handle rough terrain—and rougher company."
            Captain "Quinn,{cps=4} {/cps}a skilled navigator.{cps=2} {/cps}If there's a way through,{cps=4} {/cps}he'll find it."
            Captain "Darcey,{cps=4} {/cps}a fighter through and through.{cps=2} {/cps}Deadly for fights you want to pick and intelligent for fights you don't." 
            Captain "And of course,{cps=4} {/cps}[player_name],{cps=4} {/cps}the rising star messenger.{cps=2} {/cps}Fast,{cps=4} {/cps}reliable,{cps=4} {/cps}and able to think on their feet."
            Captain "All excellent in your own rights."
            Captain "You four are the perfect team for this mission because{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            jump continue1
        
        "Stay Quiet":
            Captain "I summoned you all here today because{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"
            $ quiet += 1
            jump continue1
    
    label continue1:
    
    "He displays the letter to the group." 
    
    Captain "The enemy sent us this letter of surrender at sundown."

    show darcey happy at happyAnim
    show plo happy at spookedAnim
    
    #TODO: character image changes
    Darcey "{i}Gasp{/i}"

    Quinn "At long last{cps=4}.{/cps}{cps=4}.{/cps}{cps=4}.{/cps}"

    Captain "There's still work to be done here,{cps=4} {/cps}but what matters now is to send word to the capital. Immediately"

    Captain "That is why im entrusting this mission to you,{cps=4} {/cps}Sergeant [player_name]."

    menu:
        "Yes,{cps=4} {/cps}Captain!":
            Captain "Good.{cps=2} {/cps}You all are dismissed.{cps=2} {/cps}The others will wake up to good news."
            jump continue2
        
        "Stay Quiet":
            Captain "......{cps=4} {/cps}Well, get going then!{cps=4} {/cps}I want you all out of here before morning."
            jump continue2
    
    label continue2:

    Iris "Understood,{cps=4} {/cps}captain."

    """
    You turn to your new team, who stare at you with anticipation.

    """
    Iris "Let's meet at the camp entrance in 5 hours."

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

    Bunkmate "What was that about? You get in trouble?"

    "Your bunkmate above you shifts to eye you inquisitively."

    menu:
        "Be honest":
            Iris "Actually,{cps=4} {/cps}I have great news!"
            "You lean in,{cps=4} {/cps}lowering your voice so as not to wake anyone."
            Iris "The Captain will announce the end of the war in the morning."
            "They nearly shout before clapping both hands over their mouth."
            Iris "Shh,{cps=4} {/cps}I have to pack{cps=4}—{/cps}I'm leaving before sunrise"
            Bunkmate "I can't believe it will be over; THIS will be over.{cps=4} {/cps}I'm not going to be able to sleep tonight."
            jump continue3

        "Joke around":
            Iris "3 days night shift duty for me."
            Bunkmate "Man, that sucks."
            "You chuckle."
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
    ##TODO: show map!!! ##

    """

    The ideal trip to the capital would be to cut through the mountain path.

    Three days,{cps=4} {/cps}maybe less if you're quick.

    We'd need to pack enough food and supplies for at least twice that. For four people.

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
    label day1:
    
    scene black with Dissolve(1.5)
    
    centered "Day 1"
    
    """
    Sunrise hasn't hit yet as you make your way to the designated meeting spot.

    Soldiers move about groggily. The night shift returns for some needed sleep as{cps=4} {/cps}the day shift gets ready to work.

    """
    scene cave with Dissolve(1.5)

    """
    You meet your party near the supply tent{cps=4} {/cps}where a wooden carriage{cps=4} {/cps}tied to a sturdy draft horse{cps=4} {/cps}stands ready.

    A cold chill blows into the cave,{cps=4} {/cps}bringing the smell of rain and mud. You wish nature was more merciful.

    Plo secures the last of the crates onto the back of the carriage.
    """

    show plo happy
    
    Plo "Cart's packed and ready.{cps=2} {/cps}Not much,{cps=4} {/cps}but it'll get us there."

    show quinn neutral

    Quinn "The rain looks intense."

    show quinn sad

    Quinn "At this rate, our journey might be hindered by the mud."

    show plo happy at jumpAnim

    Plo "A little rain won't bother me."

    Plo "I'll be driving that carriage even if it's blizzardin'."

    "Darcey approaches,{cps=4} {/cps} a bag in hand and a dignified smirk on her face."

    Darcey "Try not to get us stuck in a ditch,{cps=4} {/cps}alright?"

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
            Iris "The lives of many people rely on this letter being delivered."
            show darcey sad
            Darcey "Apologies,{cps=4} {/cps}[player_name]."
            "Darcey looks embarrassed of her unknightly behavior."
            $ quinn_points += 3
            "Plo awkwardly shuffles towards the carriage to get some air."
            ##TODO: ANImaTion here!!! ##
            $ plo_points -= 3
            $ get_serious = True
            jump continue4

        "Say nothing":
            $ quiet += 1
            jump continue4
    
    label continue4:


    """
    The conversation dies off as the sound of rain tapping against the heavy stone of the cave grows louder.

    Quinn's eyes narrow slightly at the sight of the road ahead.
    """

    Quinn "We shouldn't waste any more time."

    Quinn "The weather will only get worse."

    Plo "Alright,{cps=4} {/cps}everybody.{cps=2} {/cps}Let's get this letter on the road."

    "Plo packs the final crate and secures the latch on the carriage."

    Iris "Mount up."

    """
    Darcey and Quinn enter the carriage.

    Quinn props the door open and faces you with respect.
    
    """
    
    Quinn "After you,{cps=4} {/cps}[player_name]."

    menu:
        "Sit inside":
            Iris "Thank you, Quinn."
            $ quinn_points += 5
            $ darcey_points += 5
            jump InsideCarriage

        "Guard outside":
            "[player_name] waves their hand at Quinn."
            Iris "No need,{cps=4} {/cps}I'll help guard outside alongside Plo."
            Plo "Hmph, at least someone else isn't afraid of water."
            Quinn "As you wish."
            "Quinn shuts the door behind them."
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

    show quinn neutral at left
    show darcey happy at right

    Darcey "So,{cps=4} {/cps}Seargent [player_name]... Got any words of wisdom before we roll out?"
    menu:
        "Keep it lighthearted":
            Iris "Try not to kill each other before we get there."  
            "Darcey laughs,{cps=4} {/cps}while Quinn gives a small,{cps=4} {/cps}knowing smile."  
            Darcey "I'll be on my best behavior." 
            Quinn "I bet so." 
            $ darcey_points += 5
            $ quinn_points += 3

        "Be serious":
            Iris "Stay focused. Stay alert. Distractions can't delay us."  
            """
            Darcey agrees, but her smile slightly fades. 
            
            Quinn gives a small nod of approval.
            """
            Quinn "Understood."  
            $ darcey_points += 2
            $ quinn_points += 5

    """
    Time passes in silence. {cps=4} {/cps}The rain doesn't let up.
    """

    menu:
        "Ask Quinn about the path ahead":  
            label path:
            $ quinn_points += 5
            Iris "What's the terrain like ahead?"
            Quinn "Rough. Once we're out of the mud, we'll hit gravel. It'll even out once we hit the main road."  
            "Darcey sighs."
            Darcey "Let's hope Plo is as skilled as he brags he is." 
            jump continue5

        "Ask about Darcey and Plo":
            Iris "What's the deal between you and Plo?"
            "Darcey sighs,{cps=4} {/cps}lowering her voice to a whisper."
            Darcey "Let's just say you'd be wrong to expect him to be a model soldier.{cps=4} {/cps}Plo's not the kind of person who thinks of the consequences before he acts."
            "Quinn hits her softly with his elbow."
            Quinn "He has a good heart when it matters." 
            jump continue5

        "Sit Quietly":
            """
            You settle back,{cps=4} {/cps}listening to the sound of the rain.

            Quinn's eyes remain half-lidded as Darcey hums softly under her breath.

            The rhythmic sway of the carriage mixes with the patter of rain to create a drowsy sort of calm.
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
                                Darcey "Listeners are valuable too." 
                                "Darcey's gaze moves toward the window." 
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

    "A comfortable silence dawns on you and your party as the carriage rocks gently beneath you."

    Darcey "So,{cps=4} {/cps}what do you think about-" 
    #TODO: shake screen

    """
    The carriage lurches forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.

    You hear a horse's annoyed neigh from outside.
    """

    Darcey "Damnit,{cps=4} {/cps}I knew he would." 
    
    Iris "That does not sound good..."

    "You,{cps=4} {/cps}Quinn,{cps=4} {/cps}and Darcey make your way out of the carriage."

    scene forest with Dissolve(1.5)

    Quinn "Plo,{cps=4} {/cps}are you alright?"

    Plo "I am,{cps=4} {/cps}but I can't say the same for the carriage."

    "One of the carriage's wheels was stuck in the mud."

    jump continue6
######################
## outside carriage
###################### 
    label OutsideCarriage:

    scene forest with Dissolve(1.5)
    ##TODO: rain effect here
    """
    The steady patter of rain against the carriage's canopy mingles with the sound of the horse's hooves stomping through the wet mud.

    Moisture from the air sticks to you; the rain helping it drip down your collar.

    "Plo sits at the front,{cps=4} {/cps}reins loose in his hands and{cps=4} {/cps}eyes half-lidded as he watches the road ahead."

    You sit next to him in peaceful silence as the party makes its way through the thick forest.
    """

    Plo "Rain's picking up." 

    menu:
        "Make small talk.":
            $ plo_points += 5
            Iris "The weather only gets better for us."
            Plo "Haha!" 
            Plo "It is actually quite nice for turtle folk like myself." 
            Plo "Keeps the shell from drying out."
            Iris "Is that so?"  
            "Plo grunts in approval."
            Plo "Nothing worse than an itchy shell."  
            "Plo flashes you a smile before focusing back on the road."  
            Iris "And here I thought you were going to be miserable out here."  
            Plo "Eh, only if it were sunny. It's the heat that's the problem."  
            "A second of silence passes before Plo's face scrunches."
            Plo "That... and sand."  
            Iris "Sand?"  
            Plo "It gets {i}everywhere{/i}."  
            jump continue8

        "Talk about the mission.":
            Iris "Did you pack everything you needed for the mission last night?"
            "Plo makes an annoyed grunt. He can't hide his grumble."
            Plo "Barely had any time,{cps=4} {/cps}so I just packed the essentials."
            ##the joke is that his inventory is filled with junk, ill make a graphic for this
            show jokeinventory 
            menu:
                "Praise his packing skills":
                    Iris "You... really thought of everything I guess."
                    Iris "How did you even get all that to fit in there?"  
                    Plo "The amount of supply runs i've gone on you pick up some things."
                    Plo "You get to know whats {i}really{/i} essential."
                    $ plo_points += 3
                    jump continue8

                "Question his choices":
                    Iris "I'm not sure a lot of that is necessary..."
                    Plo "Hmph."
                    Plo "What would a human know about packing{cps=4} {/cps}anyway."
                    $ plo_points -= 3
                    jump continue8

    label continue8:

    "Plo's eyes remain scanning the muddy road ahead."

    "The road begins to narrow as the mud deepens beneath the horse's hooves."   

    Plo "The road is getting bad... I'm afraid one of the carriage wheels is going to-"
    #TODO: shake screen

    """
    The carriage lurches forward,{cps=4} {/cps}almost knocking you out of the seat before stopping just as quickly.

    The horse strapped to the vehicle lets out an annoyed whine while stomping its feet.
    """

    Plo "Get stuck in the mud."

    show plo angry

    Plo "Great. Just great."  
    
    "You hear a muffled voice from inside the carriage"

    Darcey "Damnit,{cps=4} {/cps}I knew he would." 

    """
    Plo groans,{cps=4} {/cps}jumping down and already stepping toward the wheel.
    
    Quinn and Darcey quickly emerge from the carriage,{cps=4} {/cps}the former worried and the latter annoyed.
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