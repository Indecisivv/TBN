
################################################################################
## Endings
################################################################################
label endings:
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
            text "Additional Sound Design":
                font "Bellefair-Regular.ttf"
                color "#ffffff"
                size 55
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
