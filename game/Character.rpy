
init python:
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

        def GetName(self):
            return self.name