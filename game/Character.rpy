################################################################################
##  ████  █   █  ███  ████   ███   ████ █████ █████ ████  █████ 
##  █     █   █ █   █ █   █ █   █ █       █   █     █   █ █     
##  █     █████ █████ ████  █████ █       █   ████  ████  █████ 
##  █     █   █ █   █ █   █ █   █ █       █   █     █   █     █ 
##   ████ █   █ █   █ █   █ █   █  ████   █   █████ █   █ █████ 
################################################################################
#narrator
define n = Character(callback=text_sounds)
#main characters
define Iris = Character("[player_name]", image="iris", who_color="#ffc23e")
image iris angry= "images/sprites/[sprite_image] angry.png"
image iris blush = "images/sprites/[sprite_image] blush.png"
image iris happy = "images/sprites/[sprite_image] happy.png"
image iris neutral = "images/sprites/[sprite_image] neutral.png"
image iris sad = "images/sprites/[sprite_image] sad.png"
image iris shocked = "images/sprites/[sprite_image] shocked.png"
image iris worried = "images/sprites/[sprite_image] worried.png"

define Plo = Character("[plo_name]", who_color="#6cff3b")
#for when voices are done here is the template
#define Plo = Character("[plo_name]", callback=text_sounds, who_color="#6cff3b")
define Darcey = Character("[darcey_name]", who_color="#f95959")
define Quinn = Character("[quinn_name]", who_color="#bca6eb")
#side characters
define Officer = Character("Officer", color="#ffffff")
define Captain = Character("Captain", color="#ffffff")
define Bunkmate = Character("Bunkmate", color="#ffffff")

################################################################################
##  Player Definition
################################################################################
init python:

    class Pronoun():
        def __init__(self, neutral, masculine, feminine):
            self.neutral = neutral
            self.masculine = masculine
            self.feminine = feminine
        def __str__(self):
            global pronouns
            if pronouns == "She/Her":
                return self.feminine
            elif pronouns == "He/Him":
                return self.masculine
            elif pronouns == "They/Them":
                return self.neutral
            else:
                return self.neutral

    class Player:
        def __init__(self, character, name = "Iris", gender = "female", imagename = "eileen happy"):
            self.c = character
            self.name = name
            self.gender = gender
            self.i = imagename

        #this might not be necessary, if we just set male/female as part of the image name below  
        def SetGender(self, g):
            self.gender = g

        def SetCharacter(self, character):
            self.c = character

        def SetImage(self, imagename):
            self.imagename = imagename

        def SetName(self, name):
            self.name = name

        #Set Position and Portrait
        def ShowPlayer(self, portrait, position):
            renpy.show(str(p.imagename) + portrait, at_list=[position])

        #Same as ShowPlayer but if you don't want to change the position
        def EmotePlayer(self, portrait):
            renpy.show(str(p.imagename) + portrait)

        #Same as ShowPlayer but if you don't want to change the portrait
        def MovePlayer(self, position):
            renpy.show(str(p.imagename), at_list=[position])

        def GetName(self):
            return self.name

    
default p = Player(Character("Sylvia"))