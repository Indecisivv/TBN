
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

        def SetGender(self, g):
            gender = g

        def SetCharacter(self, character):
            self.c = character

        def SetImage(self, imagename):
            self.imagename = imagename

        def SetName(self, name):
            self.name = name

        def ShowPlayer(self, emotion, position):
            renpy.show(str(p.imagename) + emotion, at_list=[position])

        #Same as Show but if you don't want to change the emotion
        def MovePlayer(self, position):
            renpy.show(str(p.imagename), at_list=[position])

        def GetName(self):
            return self.name

    
