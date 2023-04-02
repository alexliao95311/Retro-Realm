# Import required library
import turtle
import pygame
from pygame import mixer


# Create screen
sc = turtle.Screen()
sc.title("Pong - Retro Realm")
sc.bgcolor("black")
sc.setup(width=1400, height=600)

pygame.mixer.init()
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)
 
# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
 
 
# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
 
 
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("yellow")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 8
hit_ball.dy = -8
 
 
# Initialize the score
left_player = 0
right_player = 0
 
# Title
title = turtle.Turtle()
title.speed(0)
title.color('white')
title.penup()
title.hideturtle()
title.goto(0, 240)
title.write('PONG REMASTERED - RETRO REALM', align = 'center', font=('Courier', 30, 'normal'))

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 200)
sketch.write("Player 1: 0                                                                                        Player 2:  0",
             align="center", font=("Calibri", 24, "normal"))
 
 
# Functions to move paddle vertically
def paddleaup():
    y = left_pad.ycor()
    if y+20 > 229:
        left_pad.sety(229)
    else:
        y += 20
        left_pad.sety(y)
    
 
def paddleadown():
    y = left_pad.ycor()
    if y-20 < -229:
        left_pad.sety(-229)
    else:
        y -= 20
        left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    if y+20 > 229:
        right_pad.sety(229)
    else:
        y += 20
        right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    if y-20 < -229:
        right_pad.sety(-229)
    else:
        y -= 20
        right_pad.sety(y)
 
 
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
 
 
while True:
    sc.update()
 
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
 
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
 
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
 
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Player 1: {}                                                                                        Player 2: {}".format(
                      left_player, right_player), align="center",
                      font=("Calibri", 24, "normal"))
 
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Player 1: {}                                                                                        Player 2: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Calibri", 24, "normal"))
 
    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+70 and hit_ball.ycor() > right_pad.ycor()-70):
        soundeffect = pygame.mixer.Sound("collision.mp3")
        soundeffect.play()
        hit_ball.setx(360)
        hit_ball.dx*=-1
    
    if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+70 and hit_ball.ycor()>left_pad.ycor()-70):
        soundeffect = pygame.mixer.Sound("collision.mp3")
        soundeffect.play()
        hit_ball.setx(-360)
        hit_ball.dx*=-1