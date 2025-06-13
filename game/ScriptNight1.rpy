################################################################################
##█▄ █ ▀█▀ █▀▀ █▄█ ▀█▀   █▀█ █▄ █ █▀▀ 
##█ ▀█ ▄█▄ █▄█ █ █  █    █▄█ █ ▀█ ██▄ 
##https://lingojam.com/GiantTextGenerator
################################################################################
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


# # Flags to prevent replays
default event_night1_played = False
default event_night2_played = False

label night_event_check:
    $ night_event_queue = []
    python:
        # build the queue of eligible events
        night_events = [
            {
                "name": "event_night1",
                "played_flag": "event_night1_played",
                "condition": (
                    plo_points < 50 and 
                    darcey_points < 50 and 
                    quinn_points < 50 and 
                    not event_night1_played
                )
            },
            {
                "name": "event_night2",
                "played_flag": "event_night2_played",
                "condition": (
                    plo_tired and darcey_tired and quinn_tired and 
                    not event_night2_played
                )
            },
            # TODO: more events here
        ]
        # add valid events to the queue
        for event in night_events:
            if event["condition"]:
                night_event_queue.append(event["name"])
    # call each event from the queue in order
    while night_event_queue:
        $ current_event = night_event_queue.pop(0)
        call expression current_event
    return


label event_night1:
    "this is event 1"
    $ event_night1_played = True
    return
label event_night2:
    "this is event 2"
    $ event_night2_played = True
    return
    

label test1:
    "this is a test"
    $ quinn_points -= 50
    $ darcey_points -= 50
    $ plo_points -= 50
    $ plo_tired = True
    $ darcey_tired = True
    $ quinn_tired = True
    call night_event_check
    "end of test"