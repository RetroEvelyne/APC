import turtle

def make_planet(turt, radius, colour):
    turt.color(colour)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

def move_down(turt, distance):
    turt.right(90)
    turt.penup()
    turt.forward(distance)
    turt.pendown()
    turt.left(90)

window = turtle.Screen()
turtle1 = turtle.Turtle()

window.bgcolor("black")
turtle1.speed(0)

make_planet(turtle1, 60, "orange")
move_down(turtle1, 70)
make_planet(turtle1, 20, "gray")
move_down(turtle1, 100)
make_planet(turtle1, 40, "red")
move_down(turtle1, 100)
make_planet(turtle1, 30, "green")

turtle.done()

