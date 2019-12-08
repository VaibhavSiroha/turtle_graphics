import turtle
import math
import random
sam=turtle.Turtle()
sam.speed(0)
sam.color("Red","Blue")
sam.begin_fill()
def square(turtle,size,angle):
    for i in range(4):
        turtle.forward(size)
        turtle.left(angle)
        turtle.forward(size)
for a in range(4):
    square(sam,100,90)
    sam.penup()
    sam.forward(100)
    sam.pendown()
sam.end_fill()
turtle.done


