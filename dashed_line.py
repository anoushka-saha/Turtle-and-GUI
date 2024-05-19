#Anoushka Saha
#Drawing dashed line
#May 18th, 2024
#Day 18 Practice

from turtle import Turtle, Screen
name = Turtle()
for i in range(15):
    name.forward(10)
    name.up()
    name.forward(10)
    name.down()

screen = Screen()
screen.exitonclick()