from turtle import Turtle

#Create ScoreBoard class from Turtle Class and assign attributes
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.comp_score=0
        self.user_score=0
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.user_score, align="center", font=("Courier",80,"normal"))
        self.goto(100, 200)
        self.write(self.comp_score, align="center", font=("Courier", 80, "normal"))

    def user_point(self):
        self.clear()
        self.user_score+=1
        self.update_scoreboard()

    def comp_point(self):
        self.clear()
        self.comp_score+=1
        self.update_scoreboard()


