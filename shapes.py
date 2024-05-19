#Anoushka Saha
#Shapes
#May 18th, 2024
#Day 18 Practice

from turtle import Turtle, Screen
import random
shape = Turtle()

colours = ["HotPink", "LightPink", "PaleVioletRed", "Plum", "MediumOrchid", "Purple", "MediumSlateBlue", "MediumPurple"]

def draw_shape(sides):
    angle = 360 / sides
    for s in range(sides):
        shape.forward(100)
        shape.right(angle)

for shape_side_n in range(3, 10):
    shape.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()