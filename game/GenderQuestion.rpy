# label GenderQuestion:
#     show sylvie green normal at AnchorHalfBottom
#     show lucy happy at AnchorHalfBottom
#     show lucy happy at HalfLeft
#     show sylvie green normal at HalfRight
#     e "Select your portrait"
    
#     menu:
#         "Masculine":
#             jump Boy
#         "Feminine":
#             jump Girl
#     label Boy:
#         hide sylvie green
#         show lucy at MoveToMiddle
#         "Are you sure?"
#         menu:
#             "Yes.":
#                 $ p.SetGender("male") #We might not actually need this, if we just set male/female as part of the image name below  
#                 $ p.SetImage("lucy ") #Change this when final portraits are in
#                 jump PronounQuestion
#             "No.":
#                 jump GenderQuestion
#     label Girl:
#         hide lucy
#         show sylvie green at MoveToMiddle
#         "Are you sure?"
#         menu:
#             "Yes.":
#                 $ p.SetGender("female") #We might not actually need this, if we just set male/female as part of the image name below  
#                 $ p.SetImage("sylvie green ") #Change this when final portraits are in
#                 jump PronounQuestion
#             "No.":
#                 jump GenderQuestion

# label PronounQuestion:
#     "Select Pronouns"

#     menu: 
#         "She/Her":
#             $ pronouns = "She/Her"
#             jump NameQuestion

#         "He/Him":
#             $ pronouns = "He/Him"
#             jump NameQuestion

#         "They/Them":
#             $ pronouns = "They/Them"
#             jump NameQuestion

#     label PronounCheck:
#         "Are you Sure?"
#         menu:
#             "Yes":
#                 jump NameQuestion
#             "No":
#                 jump PronounQuestion

    

# label NameQuestion:


#     $ p.SetName(renpy.input("What's Their Name?", default = "Iris"))

#     $ p.SetCharacter(Character(p.name))


# label FinalCheck:
#     $ p.c("My name is " + (p.name) + " and my pronouns are " + (pronouns))

#     "Are you sure about all that?"
#     menu: 
#         "Yes":
#             jump GenderTest
#         "No":
#             jump GenderQuestion



define they = Pronoun("they", "he", "she")

define theyre = Pronoun("they're", "he's", "she's")

define Theyre = Pronoun("They're", "He's", "She's")

define They = Pronoun("They", "He", "She")

define sex = Pronoun("neutral", "boy", "girl")

define attractive = Pronoun("attractive", "handsome", "beautiful")

label GenderTest:
    $ p.ShowPlayer("happy", zoomInLeft)

    p.c "Here I am!!!!! I'm The Player Character!"
    $ p.c("My name is " + (p.name))


    e "[Theyre] a [attractive] [sex]."

    $ p.MovePlayer(confuseFacingRight)

    p.c "I can be confused."

    $ p.MovePlayer(Straighten)

    p.c "And Straighten."

    $ p.MovePlayer(spookedAnim)

    p.c "Get Spooked"

    $ p.MovePlayer(scaredAnim)

    p.c "Or Scared"

    $ p.MovePlayer(jumpAnim)

    p.c "Or Jump for joy"

    $ p.MovePlayer(happyAnim)

    p.c "Be happy"

    $ p.MovePlayer(sadAnim)

    p.c "Or sad"

    $ p.MovePlayer(flipLeft)
    pause 0.4

    $ p.MovePlayer(MoveToHalfRight)

    p.c "move around"


    $ p.MovePlayer(proudAnim)
    p.c "Just like everybody else!"


