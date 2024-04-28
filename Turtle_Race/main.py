import turtle
import random

screen = turtle.Screen()
red_turtle = turtle.Turtle()
green_turtle = turtle.Turtle()
blue_turtle = turtle.Turtle()
goldenrod_turtle = turtle.Turtle()
olive_turtle = turtle.Turtle()
line = turtle.Turtle()

line.hideturtle()
line.color("black")
line.speed("fastest")
line.teleport(320, -300)
line.setheading(90)
line.forward(600)

choose_color = screen.textinput("Make your bet", "Who wil win in race? Enter a colour:\n red, green, blue ,goldenrod, olive ")

turtle_list = [red_turtle, green_turtle, blue_turtle, goldenrod_turtle, olive_turtle]
turtle_colors = ["red", "green", "blue", "goldenrod", "olive"]
set_pos = 200

for x in range(len(turtle_list)):
    turtle_list[x].shape("turtle")
    turtle_list[x].penup()
    turtle_list[x].color(turtle_colors[x])

for _ in turtle_list:
    _.goto(-300, set_pos)
    set_pos = set_pos - 100


def random_speed():
    return random.randint(10, 30)


winner = -1
while winner == -1:
    for x in range(len(turtle_list)):
        turtle_list[x].forward(random_speed())
        if turtle_list[x].xcor() > 300:
            winner = x
            break

if choose_color == turtle_list[winner].color()[0]:
    print("You Win")
else:
    print("Your choose {0}\nYou lose {1} first".format(choose_color, turtle_list[winner].color()[0]))

screen.exitonclick()
