import turtle
import random

screen = turtle.Screen()
screen.title("Colorful Spiral Activity")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

colours = [ "red", "orange", "yellow", "green", "blue", "purple" ]
size = 5

while size < 500:
    t.color(random.choice(colours))
    for i in range(10):
        if size % 2 == 0:
            t.circle(size/4)
        else:
            t.circle(size/2)
        t.right(10)
        size += 2
    t.right(10)
    size += 5

turtle.done()
