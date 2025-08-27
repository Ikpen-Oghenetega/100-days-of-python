from turtle import Turtle

#Create ScoreBoard class from Turtle Class and assign attributes
class Pitch(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.teleport(0,-450)
        self.goto(0,450)

