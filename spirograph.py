#Anoushka Saha
#Spirograph
#May 18th, 2024
#Day 18 Practice

from turtle import Turtle, Screen
import random

spi = Turtle()
Turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spi.color(random_color())
        spi.circle(100)
        spi.setheading(spi.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
