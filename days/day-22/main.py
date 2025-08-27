#import necessary classes
import random
from random import randint
from turtle import Screen
from scoreboard import ScoreBoard
from userpaddle import UserPaddle
from comppaddle import CompPaddle
from ball import Ball
import time
from pitch import Pitch

#Create Screen
screen=Screen()
screen.bgcolor("black")
#Create a variable for the while loop
game_is_on=True



#Freeze animation and create the class instances
screen.tracer(0)
user=UserPaddle()
comp= CompPaddle()
ball=Ball()
scoreboard=ScoreBoard()
pitch= Pitch()


#Update Screen
screen.update()

#Map user paddle movement keys
screen.listen()
screen.onkeypress(user.move_down,"Down")
screen.onkeypress(user.move_up, "Up")

#define a function for the computer to catch the ball
#Arguments are the co-ordinates of the ball
def comp_catch_315(x_cord,y_cord):
    #For a 315 degree line slope is -1. Obtain the x,y coordinates of the ball landing
    y=y_cord-340+x_cord
    x=340
    #if it lands above the paddle, make it move up
    if comp.centre_turtle.towards(x,y)<180:
        #get the distance between the ball and the landing point
        distance=comp.centre_turtle.distance(x,y)
        #make it move once per loop for proper animation
        #Use distance less than five to see whether it has approximately gotten to the landing point.
        #Distance==0 would give poor animation
        if distance >5:
            # Don't allow the paddle leave the screen
            if comp.centre_turtle.ycor()< 320:
                comp.move_up()
    #if it lands below the paddle, make it move down
    elif comp.centre_turtle.towards(x,y)>180:
        distance=comp.centre_turtle.distance(x,y)
        # make it move once per loop for proper animation
        if distance>5:
            # Don't allow the paddle leave the screen
            if comp.centre_turtle.ycor() >- 320:
                comp.move_down()

#define a function for computer to fail
def comp_fail():
    x=340
    y=50
    if comp.centre_turtle.towards(x,y)<180:
        distance=comp.centre_turtle.distance(x,y)
        #make it move once per loop for proper animation
        #Use distance less than five to see whether it has approximately gotten to the landing point.
        #Distance==0 would give poor animation
        if distance >5:
            # Don't allow the paddle leave the screen
            if comp.centre_turtle.ycor()< 320:
                comp.move_up()
    elif comp.centre_turtle.towards(x,y)>180:
        distance=comp.centre_turtle.distance(x,y)
        # make it move once per loop for proper animation
        if distance>5:
            # Don't allow the paddle leave the screen
            if comp.centre_turtle.ycor() >- 320:
                comp.move_down()


#define a function for the computer to catch the ball
def comp_catch_45(x_cord,y_cord):
    # For a 45 degree line slope is 1.Obtain the x,y coordinates of the ball landing
    y=y_cord+340-x_cord
    x=340
    # if it lands above the paddle make it move up
    if comp.centre_turtle.towards(x,y)<180:
        distance=comp.centre_turtle.distance(x,y)
        if distance >5:
            #Don't allow the paddle leave the screen
            if comp.centre_turtle.ycor() <320:
                comp.move_up()


    #if it lands below the paddle make it move down
    elif comp.centre_turtle.towards(x,y)>180:
        distance=comp.centre_turtle.distance(x,y)
        if distance>5:
            # Don't allow the paddle leave the screen
            if comp.centre_turtle.ycor() > -320:
                comp.move_down()


loop_count=0
comp_win=True

#CODE THE GAME
while game_is_on:
    loop_count+=1
    #set time and screen to update
    time.sleep(0.00009)
    screen.update()

    #set ball to be in motion
    ball.move()

    #set ball to bounce off user paddle at either angle 45 or 315
    for seg in user.segments:
        if ball.distance(seg)<20:
            angles=[45,315]
            new_heading = random.choice(angles)
            ball.setheading(new_heading)

    #set ball to bounce off computer paddle at either angle 135 or 225
    for seg in comp.segments:
        if ball.distance(seg)<20:
            angles = [135, 225]
            new_heading = random.choice(angles)
            ball.setheading(new_heading)

    if comp_win:
        #if the ball is coming in a downward direction towards the computer side
        if ball.heading()==315 and ball.xcor()>0:
            #move the comp paddle to the expected place of landing for the ball
            comp_catch_315(ball.xcor(),ball.ycor())

        #if the ball is coming in an upward direction towards the computer side
        if ball.heading() == 45 and ball.xcor() > 0:
            # move the comp paddle to the expected place of landing for the ball
            comp_catch_45(ball.xcor(),ball.ycor())
    elif comp_win== False and ball.xcor()>0:
        comp_fail()

    #set what happens if user loses, that is, if ball is not caught by player
    if ball.xcor()<-400:
        # scoreboard.comp_point()
        # ball.go_center()
        game_is_on=False

    #set what happens if comp loses.
    if ball.xcor()>400:
        scoreboard.user_point()
        comp_win=True
        ball.go_center()

    #set how computer will lose
    if loop_count%2000==0:
        chance=randint(1,6)
        if chance==4:
            comp_win=False















screen.exitonclick()

