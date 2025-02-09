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
                jump GenderTest
            "No.":
                jump GenderQuestion


label GenderTest:
    $ p.ShowPlayer("happy", zoomInLeft)

    p.c "Here I am!!!!! I'm The Player Character!"
    $ p.c("My name is " + (p.name))