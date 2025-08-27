#Import Turtle class
from turtle import Turtle
import random

#Create Ball class from Turtle Class and assign attributes
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.setheading(135)

    #define move function
    def move(self):
        self.forward(1)
        #Make it bounce of the walls
        if self.ycor()>280 or self.ycor()<-280:
            new_heading= self.heading()+90
            self.setheading(new_heading)

    def go_center(self):
        self.goto(0,0)
        self.setheading(random.choice([45,135]))




