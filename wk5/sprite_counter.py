import turtle
import random


screen = turtle.Screen()
screen.title("Random Sprites")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

counter = turtle.Turtle()
counter.penup()
counter.hideturtle()
counter.color("white")
counter.goto(-280, 250)

shapes = ["arrow", "circle", "classic", "square", "triangle", "turtle"]

color_counts = {
        "red": 0,
        "orange": 0,
        "yellow": 0,
        "green": 0,
        "purple": 0
        }
sprites = []

def update_counter():
    counter.clear()
    counter.write(f"Total: {sum(color_counts.values())}", font=("Arial", 20, "normal"))
    y = 250
    for color, counts in color_counts.items():
        counter.goto(-280, y)
        counter.write(f"{color}: {counts}", font=("Arial", 20, "normal"))
        y -= 20
    counter.goto(-280, 280)

def create_sprite():
    t = turtle.Turtle()
    t.penup()
    t.goto(random.randint(-250, 250), -280)
    t.left(90)
    t.turtlesize(random.randint(2,5))
    t.shape(random.choice(shapes))
    random_color = random.choice(list(color_counts.keys()))
    t.pencolor(random_color)
    color_counts[random_color] += 1
    update_counter()
    sprites.append(t)

def move_sprites():
    for sprite in sprites[:]:
        sprite.forward(5)

        if sprite.ycor() > 300:
            color_counts[sprite.pencolor()] -= 1
            update_counter()
            sprite.hideturtle()
            sprites.remove(sprite)

    if random.random() < 0.1:
        create_sprite()

    screen.update()

    screen.ontimer(move_sprites, 50)

move_sprites()

screen.exitonclick()
