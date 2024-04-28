import random
import turtle as t

my_turtle = t.Turtle()
my_turtle.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


my_turtle.speed("fastest")
for _ in range(36):
    my_turtle.color(random_color())
    my_turtle.circle(100)
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading + 10)


screen = t.Screen()
screen.exitonclick()
