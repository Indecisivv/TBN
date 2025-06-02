################################################################################
## █▀▄ ▄▀▄ ▀▄▀   ▀█▀ █ █ █ █▀█ 
## █▄▀ █▀█  █     █  ▀▄▀▄▀ █▄█ 
################################################################################
label day2:
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
            "[darcey_name] hands over the food and reaches for the wheel."
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
label watch_tired:
    $ first_watch_failed == True

    scene black with Dissolve(1.5)
    pause 1.0

    "You drift off to sleep. The sounds of the night slip away..."

    centered "Day 2"

    "There's a sharp voice outside your tent, cutting through the early morning haze."
    menu:
    "Investigate the noise":
        "Throwing the blanket off yourself, you quickly make your way outside the tent."
        jump investigate_outside
    "Sleep in a bit longer":
        "You pull the blanket over your head, but a moment later—"
        if second_watch == "plo":
            Quinn "[player_name], we need you outside the tent. We have a situation."
        else:
            Plo "[player_name]! Wake up! We've got a problem!"
        "A voice from outside the tent urges you out."
        "You reluctancy throw the blanket off and follow them outside the tent."
        $ quiet += 1
        jump investigate_outside


    label investigate_outside:
    #change bg
    "As you exit you see the faces of worry, the group gathering around a carriage missing one wheel."

    if second_watch == "plo":
        $ quinn_points -= 5
        $ darcey_points -= 8
        $ plo_points -= 3
        Darcey "The wheel's just gone?! How do you not notice someone taking a whole wheel?!"
        Plo "Who would take a wheel? Not really something I was looking out for!"
        Quinn "The rations too, the carriage is cleared out."
        Plo "Alright, I get it! I messed up, okay? I was—"

        "Plo hesitates, glancing at you as you arrive."

        Plo "...I was tired. I thought I could close my eyes for just a minute."

        Darcey "A minute doesn't lose a wheel, Plo!"

        Quinn "[darcey_name], we need to focus to fix this."

        Plo "Sorry, Iris. I should've stayed sharp. I'll make it right."

        if seen_plo_inventory == True:
            Plo "They even took my childhood basking rock, [player_name]!"
            Plo "You know I would't slack on purpose."

        menu:
            "Reassure [plo_name]":
                Iris "We all make mistakes. Let's just fix this one and move on."
                Plo "...Thanks. I owe you."
                $ plo_points += 5
            "Focus on the mission":
                Iris "We have a mission to focus on, one with many lives at stake."
                Iris "Let's get past this and continue on."
                Plo "Yeah... you're right. No more excuses."
                Plo "We have so much more on the line."

    elif second_watch == "quinn":
        $ quinn_points -= 5
        $ darcey_points -= 4
        $ plo_points -= 3
        Plo "You didn't notice anything? Nothing at all?"

        Darcey "Our wheel's gone, and so are supplies. We can't just shrug that off."

        Quinn "No, we can't. And I don't plan to. I failed my watch. I... lost focus."

        Darcey "What were you doing? Checking the area for the plant?"

        Quinn "No. Just... tired. And careless."

        Plo "{i}Sigh.{/i}"
        Plo "We're going to have to get creative fixing this."

        Quinn "[player_name]... I'll take responsibility. I won't let it happen again."

        menu:
            "Reassure [quinn_name]":
                Iris "You're allowed to make mistakes. We'll get through this."
                Iris "We have to, for the people who will be saved by the message."
                Quinn "...You're kinder than I deserve right now."
                $ quinn_points += 5
            "Focus on the mission":
                Iris "We have a mission to focus on, one with many lives at stake."
                Iris "Let's get past this and continue on."
                Quinn "Of course, thank you [player_name]."

    elif second_watch == "darcey":
        $ quinn_points -= 10
        $ darcey_points -= 6
        $ plo_points -= 6
        Quinn "We will fix this. No one can blame you after what you went through yesterday."
        Darcey "I failed my duties as a solider, its my fault. That plant barely even scraped me."
        Quinn "No, there should be some order when choosing night watch."

        Plo "You think everyone would be this nice if it was me that lost the stuff?"

        Plo "What's the use of having big ears if you can't even hear someone unscrewing our carriage wheel!"

        Darcey "Okay! I screwed up, alright? I just needed a moment."

        Plo "You should've asked someone to take over."

        Darcey "Yeah, and wake up Quinn? He looked worse than me, all anxious about the plant coming back."
        Darcey "And you- You would not have even woken up, I heard you snoring from out here!"

        Quinn "Let's not waste time assigning blame. We are going to recover from this."

        menu:
            "Reassure [darcey_name]":
                Iris "Even the best soldiers make mistakes." 
                Iris "You're already a good soldier because you care, let's get past this together."
                Darcey "Thank you, [player_name]."
                $ plo_points += 5
            "Focus on the mission":
                Iris "We have a mission to focus on, one with many lives at stake."
                Iris "Let's get past this and continue on."
                Darcey "Of course, I would never forget about the mission!"


    Iris "Let's focus on logging what's lost now."
    "You check your bag and see the contents still there." 
    "Must have been too risky to enter the tent for the bag you kept with you."

    "You step over the tracks, trying to preserve them, as you approach the carriage."

    "The wheel's been screwed off clean, just empty space where it once sat."

    "You kneel to inspect the sand nearby."

    Plo "Why didn't they just take all the wheels? Why just one?"

    Quinn "They most likely would have given the time to..."

    menu:
        "Check for tracks":
            "Faint impressions lead away from the road."
            "Too big for a fox, too quiet for bandits."
            "Whatever it was, it moved fast and light."
        "Look at what's missing inside":
            "You dig through the scattered supplies."
            "The thief took almost everything, it would be easier to say what they left."

    "Quinn joins you, brushing aside some sand near the axle."

    if second_watch == "quinn":
        Quinn "It was truly inexcusable of me, [player_name]. I will make it up to everyone..."
        "He composes himself before inspecting the wheel."

    Quinn "Precision work. They didn't just stumble into our camp. They knew what they were doing."

    Plo "Took the good stuff too. Well, all our stuff really."

    if second_watch == "darcey":
        Darcey "Ugh, I'm sorry again guys. They didn't make a sound, I would have heard."
    else:
        Darcey "Bold enough to slip in without a sound, and smart to grab everything at once."

    Iris "They're watching us. That's what this means."

    "The others fall quiet for a moment, taking that in."

    Quinn "Then we'll need to be smarter tomorrow."

    Plo "And more awake."

    menu:
        "No more solo watches.":
            Iris "We need a better system."
            Iris "From now on will rotate in pairs."
            $ solo_watch == False
        "Make our watches shorter.":
            Iris "We need a better system."
            Iris "All four of us will take watch every night from now on."
            Iris "A shorter watch is a better watch."

    "You glance back at the trail, heart uneasy."

    Plo "Damn carriage more trouble than it's worth at this point."

    menu:
        "We will have to proceed on foot.":
            Iris "Our best bet is to leave the carriage behind."
            Plo "In the dessert sand?!"
            Plo "I didn't mean it, why can't we just fix the carriage up again?"
            if get_serious == False:
                Darcey "Great. Nothing like a scenic death march to build morale."
        "We need to find something to fix the carriage.":
            Iris "We should try to fix the carriage."
            Plo "I could definitely fix it up if we got a replacement part."
            Quinn "Another wheel {i}would{/i} be relatively cheap, but we have no gold left to buy one."


######################
## proceed on foot
######################  
        



    












