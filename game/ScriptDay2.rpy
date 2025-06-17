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

    "A sharp voice from outside your tent cuts through the early morning haze."
    menu:
        "Investigate the noise":
            "Throwing the blanket off yourself, you quickly make your way outside."
            jump investigate_outside
        "Sleep in a bit longer":
            "You pull the blanket over your head to drown out the noise, but, a moment later, a voice comes from outside."
            if second_watch == "[plo_name]":
                Quinn "[player_name], we need you outside the tent. We have a situation."
            else:
                Plo "[player_name]! Wake up! We've got a problem!"
            "You reluctancy throw the blanket off and follow it outside."
            $ quiet += 1
            jump investigate_outside


    label investigate_outside:
    #change bg
    "The first thing you see is the worried group gathered around a carriage missing one wheel."

    if second_watch == "[plo_name]":
        $ quinn_points -= 5
        $ darcey_points -= 8
        $ plo_points -= 3
        Darcey "The wheel's just... gone?! How do you not notice someone taking a whole wheel?!"
        Plo "Who would take a wheel? Not really something I was looking out for!"
        Quinn "They took the rations too; the carriage is cleared out."
        Plo "Alright! I get it! I messed up, okay? I was—"

        "[plo_name] hesitates, glancing at you."

        Plo "...I was tired. I thought I could close my eyes for just a minute."

        Darcey "A minute doesn't lose a wheel, [plo_name]!"

        Quinn "[darcey_name], we need to work together to fix this."

        Plo "Sorry, everyone. I should've stayed sharp. I'll make it right."

        if seen_plo_inventory == True:
            Plo "Blasted! They even took my childhood basking rock!"
            Plo "[player_name], you know I would't slack on purpose."

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

        Quinn "We can't, and I don't plan to. I failed my watch. I... lost focus."

        Darcey "What were you doing? Checking the area for enemies?"

        Quinn "No. Just... tired. And careless."

        Plo "{i}Sigh.{/i}"
        Plo "We're going to have to get creative fixing this."

        Quinn "[player_name]... I take responsibility. I won't let this happen again."

        menu:
            "Reassure [quinn_name]":
                Iris "You're allowed to make mistakes. We'll get through this."
                Iris "We have to, for the people who will be saved by the letter."
                Quinn "...You're kinder than I deserve right now."
                $ quinn_points += 5
            "Focus on the mission":
                Iris "We have a mission to focus on, one with many lives at stake."
                Iris "Let's get past this and continue on."
                Quinn "Of course. Thank you, [player_name]."

    elif second_watch == "darcey":
        $ quinn_points -= 10
        $ darcey_points -= 6
        $ plo_points -= 6
        Quinn "We will fix this. No one can blame you after what you went through yesterday."
        Darcey "I failed my duties as a solider; its my fault. This was so simple. All I had to do was stay awake."
        Quinn "No, there should be some order when choosing night watch."

        Plo "You think everyone would be this nice if it was me that lost the stuff?"

        Plo "What's the use of having big ears if you can't even hear someone unscrewing our carriage wheel!"

        Darcey "Okay! I-I just needed a moment."

        Plo "You should've asked someone to take over."

        Darcey "Yeah, and wake up who? [player_name] who had just served a night shift, or drag [quinn_name] into covering both our night shifts after helping to save me."
        Darcey "Or you? You wouldn't have even woken up! I heard you snoring from out here!"

        Quinn "Let's not waste time assigning blame. We are going to recover from this."

        menu:
            "Reassure [darcey_name]":
                Iris "Even the best soldiers make mistakes." 
                Iris "Recognizing and owning you're mistakes is enough. Let's get past this together."
                Darcey "Thank you, [player_name]."
                $ plo_points += 5
            "Focus on the mission":
                Iris "We have a mission to focus on, one with many lives at stake."
                Iris "Let's get past this and continue on."
                Darcey "Of course! I would never forget about the mission!"


    Iris "Let's log what's lost."
    "You check your bag and see the contents are still there." 
    "Could it have been too risky to enter your tent for it? Strange."

    "You step over the tracks, trying to preserve them, as you approach the carriage."

    "The wheel's been screwed clean off. The carriage heavily leans on the empty space left there."

    "You kneel to inspect the sand nearby."

    Plo "Why didn't they just take all the wheels? Why just one?"

    Quinn "Sabotage? Taking one wheel could be a message to us."

    menu:
        "Check for tracks":
            "Faint impressions lead away from the road."
            "Too big for a fox, too faint for bandits."
            "Whatever it was, it moved fast and light."
        "Look at what's missing inside":
            "You dig through the scattered supplies."
            "The thief took almost everything; it would be easier to say what they left."

    "Quinn joins you and brushes aside some sand near the axle."

    if second_watch == "quinn":
        Quinn "It was truly inexcusable of me, [player_name]. I will make it up to everyone."
        "He composes himself before inspecting where the axle directly."

    Quinn "Precision work. They didn't just stumble into our camp. They knew what they were doing."

    Plo "Took the good stuff too. Well, all our stuff really."

    if second_watch == "darcey":
        Darcey "Ugh, I'm sorry again guys. They didn't make a sound, I would have heard."
    else:
        Darcey "Bold enough to slip in without a sound, and smart enough to grab everything at once."

    Iris "They were watching us. That's what this means."

    "The others fall quiet for a moment, taking that in."

    Quinn "They could come back. We'll need to be smarter tomorrow."

    Plo "And more awake."

    menu:
        "No more solo watches.":
            Iris "We need a better system. "
            Iris "From now on, we'll rotate in pairs."
            $ solo_watch == False
        "Make our watches shorter.":
            Iris "We need a better system."
            Iris "All four of us will take watch every night from now on."
            Iris "A shorter watch each is a better watch."

    "You glance back at the trail with an uneasy heart."

    Plo "Damn carriage is more trouble than it's worth."

    menu:
        "We will have to proceed on foot.":
            Iris "Our best bet is to leave the carriage behind."
            Plo "In the desert sand?!"
            Plo "Why can't we just fix the carriage up again? I didn't mean what I said."
            if get_serious == False:
                Darcey "Great. Nothing like a scenic death march to build morale."
                Darcey "Maybe we can even chant a marching song."
        "We need to find something to fix the carriage.":
            Iris "We should try to fix the carriage."
            Plo "I could fix it up if we got a replacement part."
            Quinn "Another wheel {i}would{/i} be relatively cheap, but we have nowhere to buy one."
            Darcey "Or enough gold to afford it."


######################
## proceed on foot
######################  
label proceedSand:

    "Darcey kicks some sand up."
    Darcey "Now what? This is going to delay the mission."

    Quinn "Let's not panic. We need to assess what supplies we have and figure out our options."

    "Iris pulls out the map from her pack and spreads it across the damaged bench seat."
    #TODO:Show map

    Quinn "There's a town marked here. Just south of the mountain range."

    Plo "Judging from the map it's about a half day's ride."

    Plo "In dangerously hot sand that is."

    Plo "Who's even knows how long it would take to walk that."

    #TODO:hide map

    Plo "This is exactly why we had the carriage in the first place, it's not safe walking in this mess."

    Quinn "We can't leave the carriage for long."

    Iris "Let's just gather everything to leave for now."

    "Quinn gives a nod before going over to collect supplies."

    if first_watch_failed == True:
        Darcey "Nothing much left anyway..."
    else:
        if plo_points >= 70:
            Plo "I'll help carry. I got no problem hauling some more weight on my shell."
            "Plo makes his way to rummage what is left of the carriage."
        elif plo_points >= 50:
            Plo "I've never had more bad luck than on a mission than with you, [player_name]."
            "Plo grumbles and makes his way to rummage what is left of the carriage."
        else:
            Plo "Not much more can go wrong than this." 
            Plo "Imagine if they stole the letter, then we'd be in deep trouble."
            "Plo grumbles and makes his way to rummage what is left of the carriage."
  
    Iris "Then it's settled."
    Iris "We'll head to the town and see what our options are."


    """
    With the decision made, the group quickly prepares for the short journey to the nearby town.

    The desert sun rises higher, beating down on you and your team. 
    
    With the carriage damaged there's no choice but to continue on foot. 

    """
    

    jump trekInSand

######################
## trekInSand
######################  

    
    if inside_carriage:
        Darcey "Back on the road together again~"

    """
    As the path rises and curves, the heat haze lifts to reveal a wonderful sight: streaks of rose, gold, indigo, and silver paint the ridges of towering sand dunes. 

    """
    Darcey "Whoa... that's... actually beautiful."

    Plo "Bah, nothing but fancy colored sand. Hurts my feet all the same."

    "Quinn narrows his eyes, studying the lines." 
    Quinn "These are mineral strata built over millennia. Iron, copper, and manganese compressed and crystallized." 
    Quinn "If you look closely, the red bands indicate high concentrations of oxidized layers that absorb heat differently."

    Darcey "I'll take it as you think it's beautiful too."
    

    show quinn blush

    menu:
        "Tease Quinn a little.":
            Iris "You know quite a lot about the mountains."
            Iris "Or did you memorize that to impress us?"
            Quinn "It's common sense, really."
        "Thank Quinn for the info.":
            $ quinn_points += 8
            Iris "That's actually fascinating. Thank you."
            "Quinn approaches bashfully, saying in a softer voice."
            Quinn "There is also the dry basin downwind." 
            Quinn "Those Rainbow Mountains block all moisture from forming clouds, even though the southern sea is just beyond the ridge." 
            Quinn "The rain never gets past here."

    """
    Step by step you make your way through this endless desert.

    The air is dry and the desert sand sticks to the sweat on your skin.

    You can't see anything but sand and vegetation as far as you look.
    """

    menu:
        "Talk to Plo":
            "You fall into step beside Plo."
            Iris "Ever miss your old transport routes?"
            Plo "Miss? Sure. They had roads. Less sand."
            Plo "I would never miss work."
            if not inside_carriage:
                Plo "But you chose the ride outside yesterday. Bet you won't miss that route."
            Iris "But you stuck around."
            Plo "Bah. Someone's gotta haul the future around, huh?"
            if plo_points >= 60:
                "He pats your head."
                Plo "Just focus walking before you trip."
            $ plo_points += 3

        "Talk to Darcey":
            "You slow your steps to find your way at the back with Darcey."
            Iris "You ever think about life after the war?"
            if darcey_points >= 50:
                Darcey "Knighthood isn't a job. It's a calling. But maybe... maybe I'll plant something." 
                Darcey "A tree, a garden—something with roots."
                if darcey_tired == True: #if she got attacked by the plant
                    Darcey "Maybe raise something that doesn't fight back. ideally."
            else:
                Darcey "After the war? Hah, one battle at a time." 
                Darcey "Thinking too far ahead just gets you hurt out here."
            $ darcey_points += 3

        "Talk to Quinn":
            "You speed up your steps to find your way at the front with Quinn."
            Iris "You ever think about life after the war?"
            Quinn "Sometimes. I think everyone does, even if they don't admit it."
            if quinn_points >= 70:
                Quinn "I want a quiet life, regardless of where that takes me."
                "His eyes glance around at everyone."
                Quinn "Surrounded by my companions if possible."
                Quinn "You could visit, if you'd like."
            else:
                Quinn "Hard to picture it, honestly. Feels like the war's been my whole life."
                Quinn "I would like to think I'd be a great researcher after this."
                Quinn "Maybe an author."
                Quinn "What about you?"
            $ quinn_points += 3

        "Stay quiet.":
            """
            You breathe in the vastness of the landscape, saying nothing.

            The wind brushes across the dunes, stirring the sand in gentle spirals—restless.

            You watch the way the horizon blurs into the sky, both tinted with the same golden red dust. 
            
            There's something humbling about how small you are out here.

            You think about the mountainscape in the distance, how many lifetimes it must've taken for them to form.
            
            How your life is a measly fraction of that time.

            You close your eyes for a second and take it all in.
            """
            #TODO: background black
            """

            No battle plans. No questions. 
            
            Just you, the sand, and the sound of your own heartbeat.
            """
            $ quiet += 1

    
    """
    The wind shifts again, carrying with it the distant murmur of voices—your companions ahead, pressing on through the sand.

    """

    "You hear Plo grunt in pain."

    Plo "My feet really do hurt, I'm telling you it's this sand."

    "He limps slightly, trying to adjust his gait."

    Darcey "Stop for a second."

    "Plo blinks, surprised, as Darcey kneels down and pulls a length of cloth from her pack."

    Darcey "Here. It's a wrap I used back in training, an old habit from long marches."
    
    Darcey "Tie it around your feet. Won't fix everything, but it'll help with the friction."

    Plo "Wait, seriously?"

    Darcey "Don't make it weird. I don't want to listen to you whine the rest of the way."

    "She smirks, but her hands are gentle as she wraps the fabric around one of his feet."
    
    "Plo watches her for a beat, clearly touched."

    Plo "...Thanks, Darce."

    Darcey "Keep moving slow and steady. Or I'm stealing it back."
    Darcey "And don't call me that!"

    menu:
        "Let's keep moving.":
            Iris "All patched up? Let's keep going."
            Plo "Ready as i'll ever be."
            $ plo_points += 2
        "Plo, are you okay?":
            Iris "Is everything okay now?"
            Plo "It's not a fix, more like a s
            tall."
            Plo "Good enough to keep going."
            $ plo_points += 3
            $ quinn_points += 2
            $ darcey_points += 2
        "Say nothing":
            $ quiet += 1
            # no dialogue
            
    #TODO: could use a better transition connector

######################
## snek 🐍
######################  
label snake:
    """
    You continue walking but you hear something in the distance.

    A rustling. 

    A thin green viper slithers past Quinn's foot. 

    Everyone freezes. 

    The desert air suddenly feels sharper, as if holding its breath alongside your team.
    """
    Quinn "A desert viper. Venomous. Unlikely to bite unless startled."

    "Darcey's hand pauses at her spear hilt."

    Darcey "Don't move."

    "Plo struggles to stay still, whisper-shouting his complaints."

    Plo "Sand AND snakes?! This day just keeps getting better and better, huh?."

    menu:
        "Stay still.":
            """
            You hold still, trusting Quinn's read of the creature. 

            ...
            
            Seconds drag out like hours. 

            ....

            Plo lets out a soft grunt, barely audible.
            """


            Plo "Whats with this thing?? Does it not have a life to get on about?"

            Quinn "It will lose interest eventually, just hold still."

            Plo "Not sure how much longer I can hold still like this."

            "You can see a drop of sweat hit the sand from his forehead."

            "You glance just enough to see Quinn's eyes tracking the creature's slow movement—every muscle in his frame braced"

            menu:
                "Keep waiting.":
                    jump keep_waiting
                
                "Throw a rock at the snake.":
                    jump throw

                "Stomp to scare it off.":
                    jump stomp

            label keep_waiting:

            """
            ...

            The snake's head shifts slightly. A flick of its tongue. 
            
            You swear it looks right at you.
            
            Your knees are starting to ache from standing still this long.

            There's a tremble in your fingers. You will them still.

            You take a deep breath. 

            """

            Plo "This is getting ridiculous."

            "Quinn doesn't respond. He's focused."

            Darcey "Just stand still! Big baby."

            "One beat. Then another."

            "Quinn murmurs softly."

            Quinn "We're doing fine. It knows we're not a threat. That's good."

            """

            The snake slithers a little to the left, dragging its heavy body through the dirt, unbothered by your presence but still lingering.

            Plo shifts again. A pebble rolls from beneath his boot.

            The creature halts.

            Every hair on your body stands on end.

            Quinn shoots a sharp look at Plo, who immediately freezes again.
            """
            menu:
                "Keep waiting.":
                    jump keep_waiting2
                
                "Throw a rock at the snake.":
                    jump throw

                "Stomp to scare it off.":
                    jump stomp
            #can switch to the other options

            label keep_waiting2:

            """
            For a minute it feels like no one breathes.
            
            Then the snake flicks its tongue once more... and glides away into the brush.

            ...

            Quinn doesn't relax until the rustle of the creature fades into the distance.
            """

            $ quinn_points += 5
            jump snake_gone

        "Throw a rock at the snake.":
            label throw:
            "You reach crouch down to sift your hands through the sand, looking for something big enough to throw."

            Plo "What are you doing?!"

            Darcey "[player_name]??"

            "The snake flinches at the shout, taking a coiled up defensive posture towards Plo."

            Plo "It's looking at me..."
            
            "You weigh a stone in your palm before lobbing it towards the snake." 
            
            "It grazes the snake as it recoils before slithers away, disappearing into the brush."

            Quinn "Not quite what I had in mind but no one got hurt."

            jump snake_gone


        "Stomp to scare it off.":
            label stomp:
            """
            Your foot slams the ground.
            
            The viper recoils, then strikes.
            
            Pain flares. 
            
            Someone yells. 
            
            Blood and panic.

            In the panic the snake flees to nearby brush.
            """

            Darcey "Why would you do that?!"

            Plo "Of all the dumb moves—"

            if get_serious:
                Quinn "...I expected better from someone who preaches caution."
            
            $ plo_points -= 5
            $ quinn_points -= 15
            $ darcey_points -= 10
            jump snake_bit

    label snake_bit:
        $ bit == True
        #if has_antidote:
            #TODO: this has to be coded to work!!!!!!!
            # use antidote to recover
            "The pain from the bite travels along your veins, making your body feel like its on fire."
            menu:
                "Endure the pain.":
                    "You grit your teeth and bear it. Speaking won't help now."
                    $ quiet += 1
                "Apologize for the mistake.":
                    Iris "I misjudged. I'm sorry."
                    Darcey "Just don't get yourself killed."
                    Plo "It was dumb but let's focus treating it now."

            "You fumble for the antidote in your bag. With Quinn's help, you drink the entire vial."
            Quinn "That was reckless."
            "The pain dulls slowly."
            Quinn "Timely. You'll live."

            jump snake_gone
        #else: #no serum in inventory
            # Game over

            """
            The venom spreads quickly. 

            Your vision blurs. 

            """
            scene black with Dissolve(1.5)
            """
            The others shout.
            
            Darcey grabs your hand, Plo is shaking you, Quinn is already reaching for a vial of who knows what—but it's too late.
            """
            jump bad_ending

    label snake_gone:

        "The tension in the air finally breaks, like a string pulled too tight and suddenly released."

        "You feel the sweat cooling on your skin, your legs still stiff from standing so long."

        "Plo wipes the back of his hand across his forehead, scowling at the ground where the snake vanished."

        Plo "That thing stared right into my soul."

        Darcey "You have a soul?"

        Plo "Then what was it looking at?"

        "Darcey snorts, low and relieved, though her hand is still hovering near her weapon."

        Plo "Let's just keep moving."

        "Darcey watches you for a beat longer, her grip still tight on her weapon."



######################
## mirage
######################  
label mirage:
    """
    You walk in silence for a while.

    The sand crunches underfoot. 
    
    Every step sinks a little, dragging your pace slower.

    Time becomes strange in the desert. Distance stretches. The horizon wavers.

    You notice a glimmering in the distant horizon.

    It almost looks like a body of water.
    """
    menu:
        "Ask about the glimmer."
            Iris "Is that... water?"
        "Point out water."
            Iris "I see water up ahead."
        "Check your map."
            #TODO: show map
            "Pulling out your map shows there is no bodies of water in the entire path before the town."
            Iris "Strange, it almost looks like there is water up ahead."
            #TODO: hide map

    Darcey "I see it too! That must be where the town is."

    Plo "Finally, feels like the heat's cooking me into a tortle soup."

    Quinn "Sorry to be the bearer of bad news..."

    Quinn "It's just the refraction of distant light through hot air layers. A mirage."

    Darcey "Ugh... just what I needed as this armor's starting to feel like it's cooking me from the inside out."

    menu:
        "Encourage moving on":
            Iris "Let's keep moving. Maybe the real thing's waiting somewhere out there."
            $ quinn_points += 2
        "Silent disappointment.":
            "You say nothing, but the letdown hits all the same."
            $ quiet += 1

    "Slowly, as you ascend a sandy hill, the illusion fades."

    Darcey "Sigh. Hope the next one doesn't vanish on us."
######################
## merchant
######################  
label merchant:

    Plo "[quinn_name], can a mirage look like a person too?"

    Quinn "Um... I have never heard of something like that, why?"

    Plo "I'm seeing one right now, on the horizon."

    """
    The wind shifts as the party pass a dune, and the distant jingle of chimes can be heard.

    The path becomes more defined, a clear trail of pressed down sand of frequent traffic lead right to it.

    A colorful carriage appears against the dunes, its canopy striped in faded reds and golds.

    Crates stacked in stacks next to it. 

    A merchant sits on a pile of rugs, lazily fanning himself.

    When he sees your party he stands to welcome them.
    
    """  

    Merchant "Travelers! Come, feel free to fan yourselves and browse."

    Plo "You would't happen to trade carriage wheels, do you?"

    Merchant "Heh, I have never gotten that request before."
    Merchant "Unfortunately not."

    Plo "Bah, let's just move on [player_name], nothing here but scams."

    Darcey "No one normal is waiting in the middle of a desert for customers."

    Merchant "Well hold on there, I assure you I only carry quality products."

    if first_watch_failed == True: #all the supplies stolen
        "You bring out your bag to look through to see what you have left."
        Darcey "But... We do need supplies. Anything that can help us reach the capital faster."
        Quinn "We lost more than we could afford. We need to focus on the important things."
        Quinn "Especially water. Won't last the rest of the journey without any."
        if second_watch == "darcey":
            Darcey "I'm sorry to ask when it's my fault [player_name], but we should probably stock while we have the chance..."
        elif second_watch = "quinn":
            Quinn "[player_name], this is all I have left but take it to spend on necessities."
            "Quinn hands you 5 gold."
        elif second_watch = "plo":
            Plo "I messed up today, that's true. But there are better places to get supplies than a scam artist."

    else:#succsesful first watch
        "You bring out your bag to look through to see what you have left."
        Darcey "We're stocked, but it wouldn't hurt to have backups. Especially water."
        

    Merchant "I have plenty supplies, take a look."


#TODO: loop this so you can do every option. make option out of stock when bought
default shop_ask_path = False
default shop_buy_food = False
default shop_buy_water = False
default shop_deal = False


    label shop_loop:
        menu:
            "Ask about path ahead" if not shop_ask_path:
                $ shop_ask_path = True
                $ plo_points += 3
                $ darcey_points += 3
                $ quinn_points += 3
                Merchant "What else can I say except there is a bunch of sand."
                Darcey "What use this guy is..."
                Plo "Don't skimp out on potential customers, give us a landmark or something."
                Merchant "Ah, now that you mention it, you will know you are close to town when you pass beggar's hole."
                Iris "Beggar's hole?"
                Merchant "It's just where a bunch of beggars wait outside town for rich travelers to steal from."
                Merchant "Anymore info and i'm going to start asking for payment."
                Quinn "That is good to know."
                Darcey "I'd like to see them try to steal from me. {i}Tsk.{/i}"
                jump shop_loop

            "5G Buy Food" if not shop_buy_food:
                $ shop_buy_food = True
                #TODO: remove gold!
                #if you have enough
                Merchant "I pity the man who doesn't even have water in this sweltering desert."
                jump shop_loop
                #if you dont have enough
                Merchant "Good choice, the finest water straight from the finest desert oasis."
                jump shop_loop

            "5G Buy Water" if not shop_buy_water:
                $ shop_buy_water = True
                #TODO: remove gold!
                #if you have enough
                Merchant "I pity the man who doesn't even have water in this sweltering desert."
                jump shop_loop
                #if you dont have enough
                Merchant "Good choice, the finest water straight from the finest desert oasis."
                jump shop_loop

            "5G Buy Special Charm" if shop_buy_food and shop_buy_water and not shop_deal:
                $ shop_deal = True
                "A special deal for a loyal customer."
                #TODO: remove gold!
                #if you have enough
                Merchant "Great! You will not regret this purchase!"
                Quinn "What does the charm do?"
                Quinn "[player_name], why would you buy that without asking first?"
                Merchant "Great question, "
                if pronouns == "She/Her":
                    Plo "Bah, let [player_name] have her weird little purchase."
                elif pronouns == "He/Him":
                    Plo "Bah, let [player_name] have his weird little purchase."
                elif pronouns == "They/Them":
                    Plo "Bah, let [player_name] have their weird little purchase."
                Plo "More importantly, I need some of that water you just bought."
                jump shop_loop
                #if you don't have enough
                Merchant "How unfortunate you don't have enough left for it. Could have come in handy."
                jump shop_loop

            "15G Buy Mystery Potion" if not shop_trade_food:
                $ shop_trade_food = true
                #TODO: remove gold!
                #if you have enough
                Merchant "My finest item, I hope it is of use for you."
                "All three look at you in confusion."
                if first_watch_failed == True: #all the supplies stolen
                    Quinn "I don't recall anyone in need of this expensive potion..."
                    Plo "What the heck, [player_name]? I thought we were going to get food and water."
                    Darcey "Yeah, whats the deal?"
                    if darcey_points >= 50:
                        Darcey "Don't blame me if i'm too hungry to do my job later then."
                    else:
                        if bit == True:
                            Darcey "First you get bit and now this? What is up with you today."
                            $ darcey_points -= 2
                        Darcey "Why would you buy that over food and water??"
                        Darcey "Don't forget about our mission."
                    $ plo_points -= 5
                    $ darcey_points -= 5
                    $ quinn_points -= 5
                    jump shop_loop
                else:
                    Quinn "A strange purchase, but I don't control what you spend your gold on..."
                    jump shop_loop
                #if you dont have enough
                Merchant "Quality means cost, and it doesn't look like you can afford this quality."
                jump shop_loop

            "Leave":
                jump shop_done

label shop_done:
    """
    After leaving the merchant behind, the dunes roll on endlessly. 
    
    You follow the darker sand, a desire path formed by many feet over a long time.
    """
    
######################
## sand man
######################  
label sand_man:
    """
    As you crest a low hill, the sight of a figure sprawled across the sand halts your step.

    The heat rising from the ground shimmers around his crumpled form like a ghostly veil.
    """
    Sandman "Help me... Please..."
    """

    His robes are in disarray, sand sticks to his face, and his breathing shallow.

    Quinn kneels beside the man.

    """
    $ sandman_name == "test"

    Quinn "Signs of heatstroke. Dehydration. His lips are cracked. Pulse is weak... but there."

    "Plo squints under the harsh sun, whispering so only the group heard."
    Plo "This guy looks like a walking corpse."

    $ if first_watch_failed == True: #all the supplies stolen
        Plo "And not to be insensitive but we need our supplies..."
    $ if shop_buy_food == True or shop_buy_water == True:
        Plo "And didn't we {i}just{/i} use the rest of our gold to buy more."

    $ if shop_ask_path == True:
        Darcey "It's probably a beggar like the merchant told us about."

    Quinn "Regardless, we can't just leave someone here to die."

    if quiet >= 5: #quinn will start leading if you are always quiet
        "Quinn takes the little water he has left from his personal bag and gives it to the man."
        Quinn "It's not much but it will help."
        "The man drinks shakily, life returning to his eyes one slow blink at a time."

        jump sandman_after
     
    
    default ignore1 = False
    label sandmanmenu:
    menu:
        "Give him water":
            $ darcey_points += 5
            $ quinn_points += 5
            $ plo_points += 2
            Iris "Here... drink slowly."
            "His hand trembles as he accepts the canteen."
            "He gulps, coughs, then drinks slower. The color slowly comes back to her face."
            Sandman "Mercy... gods above... T-thank you, thank you!"
            Sandman "I waved down so many... no one even slowed."
            Sandman "No one else stopped for me, you are the only ones."
            $ sandman_name == "Henry"
            Sandman "My name is Henry, I thought the sun had claimed me."
            "He lets out a shaky laugh that quickly collapses one more in relief."
            Quinn "He must still be tired, it will take him a while to recover from the extreme heat."
            "As you stand to leave, a sudden grip catches your wrist."
            Sandman "Please take this as a token of my gratitude."
            "He places a pendant into your hand."
            "You open your hand: a small pendant, shaped like a crescent moon, its surface etched with faded symbols worn smooth by sand."
            Iris "I hope you feel better soon."
            #TODO: get the pendant
            #TODO: lose a water
            jump sandman_after

        "Spare a sip":
            $ darcey_points += 2
            $ plo_points -= 1 
            $ quinn_points += 1
            Iris "Just a sip. We don't have much more to spare."
            "You tilt the canteen gently. He swallows once, barely moving and semi conscious."
            Quinn "It may be enough to stabilize him."
            Plo "If you are going to give him some don't half-ass it."
            Sandman "Thank you... thank you for stopping when no one else would."
            Sandman "May the weather be in your favor."
            #TODO: lose a water
            jump sandman_after

        "Ignore him.":
            $ plo_points -= 5 
            $ darcey_points -= 5
            $ quinn_points -= 5
            Iris "We don't have time. The trek through the sand has slowed us enough."
            "All three look at you in surprise."
            Quinn "[player_name], are you sure?"
            $ ignore1 == True
            jump sandmanmenu
            
        
        "Ignore him. For real." if ignore1:
            $ plo_points -= 5 
            $ darcey_points -= 5
            $ quinn_points -= 5
            "You walk on. The others hesitate, then follow." 
            "The man doesn't move. Not even to beg."
            Darcey "I hated that."
            Plo "Feels wrong. Like we left something behind."
            Quinn "Morality traded for expedience."
            jump sandman_after

    label sandman_after:

    """
    The man fades into the distance behind you as the top of buildings peak over the sand dunes.

    The sun is now directly overhead, the hottest time of the day.

    It's merciless and Plo is visibly wilting in the rays.

    Plo stumbles. He catches himself on a knee.
    """

######################
## sand tired 
######################  
label sand_tired:

    Darcey "You okay, shellback?"

    Plo "I was born in a marsh. You know what a marsh has? Not sand."

    Plo "I need a minute before I end up like that guy back there."

    "Plo sits down onto a dune, eyes squinting beneath the harsh glare."

    "Quinn is by his side examining him."

    Quinn "His pulse is elevated, I'm worried about possible heat stroke soon."

    "Plo wipes sweat from his brow, muttering."

    Plo "Don't suppose a miracle's just over that hill..."

 
    $ if ignore1 == True:
        Plo "Hopefully if I end up dying here no one ignores my plight."

    menu:
        "Crack a joke":
            $ plo_points += 3
            Iris "You look like a sand sculpture with all that sand over you now."
            Plo "Would love to be one with a moat around it... Too much sand."
            "Plo pushes himself up, unsteady but motivated to continue on."
        "Offer Plo a break":
            $ plo_points += 5
            Iris "Take a minute. I'll keep watch."
            "Plo relaxes onto a shaded rock with a grateful grunt."
            "The sun crawls overhead. Somewhere, a dry wind howls."
            "Darcey fiddles with her spear, quietly sharpening it."
            "Quinn scans the horizon, eyes narrow beneath his bangs."
            "You stand guard, one hand on your weapon, eyes trained on the dunes."
            "Darcey snorts."
            Darcey "Don't forget to blink sometime [quinn_name]."
            "Quinn doesn't respond, but his shoulders loosen just slightly."
            "After a while, Plo pushes himself up, a little steadier now."
            Plo "Okay. Legs like boiled noodles, but I can move. Thanks, Iris."
        "Push forward":
            $ plo_points -= 3
            Iris "We've got to stay on schedule."
            "He looks reluctant to continue forward."
            Darcey "Don't make me have to take my wrap back."
            Plo "Alright, alright."
            Plo "Bah, I'm getting up."
            "Plo pushes himself up, unsteady but ready to continue on."

######################
## arrived inn
######################  
label arrived_inn:
    """
    The Sun moves across the sky in the time it takes you to approach he distant town.
    """

