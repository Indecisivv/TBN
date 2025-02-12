label GenderQuestion:
    show sylvie green normal at AnchorHalfBottom
    show lucy happy at AnchorHalfBottom
    show lucy happy at HalfLeft
    show sylvie green normal at HalfRight
    e "Are you a boy? Or are you a girl?"
    
    menu:
        "Boy":
            jump Boy
        "Girl":
            jump Girl
        "Toek Me To The Debug":
            hide sylvie green
            jump DebugTest
    label Boy:
        hide sylvie green
        show lucy at MoveToMiddle
        "Are you sure?"
        menu:
            "Yes.":
                $ p.SetGender("male")
                $ p.SetName("Lucy")
                $ p.SetCharacter(Character("Lucy"))
                $ p.SetImage("lucy ")
                $ pronouns = "he/him"
                jump GenderTest
            "No.":
                jump GenderQuestion
    label Girl:
        hide lucy
        show sylvie green at MoveToMiddle
        "Are you sure?"
        menu:
            "Yes.":
                $ p.SetGender("female")
                $ p.SetName("Sylvie")
                $ p.SetCharacter(Character("Sylvie"))
                $ p.SetImage("sylvie green ")
                $ pronouns = "she/her"
                jump GenderTest
            "No.":
                jump GenderQuestion


define they = Pronoun("they", "he", "she")

define They = Pronoun("They", "He", "She")

define sex = Pronoun("neutral", "boy", "girl")

define attractive = Pronoun("attractive", "handsome", "beautiful")

label GenderTest:
    $ p.ShowPlayer("happy", zoomInLeft)

    p.c "Here I am!!!!! I'm The Player Character!"
    $ p.c("My name is " + (p.name))


    e "[They] is a [attractive] [sex]."

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


