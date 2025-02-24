
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
        def __init__(self, character, name = "Player", gender = "male", imagename = "eileen happy"):
            self.c = character
            self.name = name
            self.gender = gender
            self.i = imagename

        #this might not be necessary, if we just set male/female as part of the image name below  
        def SetGender(self, g):
            gender = g

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