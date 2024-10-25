import turtle
from random import randint, random


class Alien(turtle.Turtle):
    def __init__(self, window, *args, **kwargs):
        super(Alien, self).__init__(*args, **kwargs)
        self.alien_speed = randint(1, 3)
        
        self.penup()
        self.turtlesize(1.5)
        self.setposition(
            randint(
                int(window.LEFT + 1.15*window.SIDEBUFFER),
                int(window.RIGHT - 1.15*window.SIDEBUFFER),
            ),
            window.TOP,
        )
        self.shape("teddy-bear.gif")
        self.setheading(-90)
        self.color(random(), random(),
        random())
    
    def walk(self):
        self.forward(self.alien_speed)
