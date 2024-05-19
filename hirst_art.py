#Anoushka Saha
#Hirst Dot Art
#Day 18 Final Project
#May 18th, 2024

from turtle import Turtle, Screen
import random
import colorgram

dot = Turtle()

#rgb_col = []
#colours = colorgram.extract("pink.jpg", 10)
#for i in colours:
##    r = i.rgb.r
#    g = i.rgb.g
#    b = i.rgb.b
#    new_col = (r, g, b)
#    rgb_col.append(new_col)

#print(rgb_col)

import turtle as turtle_module
import random

turtle_module.colormode(255)
dot = turtle_module.Turtle()
dot.speed("fastest")
dot.penup()
dot.hideturtle()

cols = [(244, 163, 191), (247, 201, 222), (235, 124, 160), (214, 89, 130), (162, 168, 124), (248, 242, 241),
         (251, 254, 254), (114, 153, 85), (134, 174, 102), (126, 144, 94)]
dot.setheading(225)
dot.forward(300)
dot.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    dot.dot(20, random.choice(cols))
    dot.forward(50)

    if dot_count % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()