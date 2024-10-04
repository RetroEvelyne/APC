import turtle as t

def turtle_setup(screen, turtle1):
    screen.setup(0.5, 0.75)
    screen.bgcolor(1, 1, 0)
    screen.title("Activity Program")

    turtle1.shape("turtle")

def turtle_draw_smiley(turt):
    turt.speed(0)
    turt.color("blue")
    turt.circle(100)
    turt.penup()
    turt.goto(-60, 60)
    turt.right(45)
    turt.pendown()
    for i in range(45):
        turt.forward(3)
        turt.left(2)

    turt.penup()
    turt.goto(-25, 125)
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

    turt.goto(50, 125)
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()
    
    turt.goto(1000, 1000)

    


if __name__ == "__main__":
    turtle1 = t.Turtle()
    screen = turtle1.getscreen()

    turtle_setup(screen, turtle1)
    turtle_draw_smiley(turtle1)
    t.done()
