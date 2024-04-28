import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()
my_turtle.shape("turtle")
my_turtle.penup()


def change_direction(direct):
    if direct == "right":
        my_turtle.setheading(0)
    elif direct == "left":
        my_turtle.setheading(180)
    elif direct == "up":
        my_turtle.setheading(90)
    else:
        my_turtle.setheading(270)


def move_forward():
    if my_turtle.heading() != 90:
        change_direction("up")
    my_turtle.forward(10)


def move_backward():
    if my_turtle.heading() != 270:
        change_direction("down")
    my_turtle.forward(10)


def move_left():
    if my_turtle.heading() != 180:
        change_direction("left")
    my_turtle.forward(10)


def move_right():
    if my_turtle.heading() != 0:
        change_direction("right")
    my_turtle.forward(10)


while True:
    screen.listen()
    screen.onkey(move_forward, "Up")
    screen.onkey(move_backward, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.exitonclick()

