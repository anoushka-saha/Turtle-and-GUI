#Anoushka Saha
#Random Walk
#May 18th, 2024
#Day 18 Practice

from turtle import Turtle, Screen
import random

walk = Turtle()
colours = ["HotPink", "LightPink", "PaleVioletRed", "Plum", "MediumOrchid", "Purple", "MediumSlateBlue", "MediumPurple"]

#Making pen invisible
walk.hideturtle()

#Line thickness
walk.pensize(8)

#Random walk
angles = [90, 180, 270, 360, -90, -180, -270]

while True:
    walk.color(colours[random.randint(0,7)])
    walk.forward(20)
    walk.right(angles[random.randint(0,6)])

screen = Screen()
screen.exitonclick()

