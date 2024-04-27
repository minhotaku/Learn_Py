import random
from turtle import Turtle

color = ["IndianRed", "DeepSkyBlue", "green", "violet", "black", "seaGreen"]
direction = [0, 90, 180, 270]
my_turtle = Turtle()
my_turtle.pensize(7)
while True:
    my_turtle.forward(35)
    my_turtle.color(random.choice(color))
    my_turtle.setheading(random.choice(direction))
