#Import Turtle class
from turtle import Turtle

class UserPaddle:
    def __init__(self):
        self.segments=[]
        for i in range(4):
            paddle_segment= Turtle()
            paddle_segment.color("white")
            paddle_segment.shape("square")
            # paddle_segment.speed("fastest")
            paddle_segment.penup()
            paddle_segment.goto(-340,i*20)
            self.segments.append(paddle_segment)

    # define the move down function
    def move_down(self):
        # for each segment starting from the highest one vertically
        for seg in self.segments[::-1]:
            # make it move to the space of the next segment below (for proper animation)
            new_position= (seg.xcor(),seg.ycor()-20)
            seg.goto(new_position)

    # define the move up function
    def move_up(self):
        # for each segment starting from the lowest one vertically
        for seg in self.segments:
            # make it move to the space of the next segment above(for proper animation)
            new_position = (seg.xcor(), seg.ycor() + 20)
            seg.goto(new_position)








