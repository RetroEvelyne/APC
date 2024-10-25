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
    y = 250
    counter.write(f"Red: {color_counts['red']}", font=("Arial", 20, "normal"))
    counter.goto(-280, y-20)
    counter.write(f"Orange: {color_counts['orange']}", font=("Arial", 20, "normal"))
    counter.goto(-280, y-40)
    counter.write(f"Yellow: {color_counts['yellow']}", font=("Arial", 20, "normal"))
    counter.goto(-280, y-60)
    counter.write(f"Green: {color_counts['green']}", font=("Arial", 20, "normal"))
    counter.goto(-280, y-80)
    counter.write(f"Purple: {color_counts['purple']}", font=("Arial", 20, "normal"))
    counter.goto(-280, y)

def create_sprite():
    t = turtle.Turtle()
    t.penup()
    t.goto(random.randint(-250, 250), -280)
    t.left(90)
    t.shape("turtle")
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
