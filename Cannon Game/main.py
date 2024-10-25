import turtle
from time import time
from random import choice

from cannon import Cannon
from alien import Alien

class Game:
    def __init__(self):
        self.window = Window()
        self.player = Cannon(self.window)
        self.window.keybinds(self.player)
        self.player.draw_cannon()
        self.lost = False
        self.score = 0
        self.alien_timer = 0
        self.aliens = []

    def game_loop(self):
        while not self.lost:
            for laser in self.player.lasers:
                laser.move()
                if laser.ycor() > self.window.TOP:
                    self.remove_item(laser, self.player.lasers)
                    pass
                for alien in self.aliens:
                    if laser.distance(alien) < 20:
                        self.score += 1
                        self.remove_item(laser, self.player.lasers)
                        self.remove_item(alien, self.aliens)

            if time() - self.alien_timer > choice([2, 2.5, 3, 3.5, 4]):
                self.aliens.append(Alien(self.window))
                self.alien_timer = time()
            for alien in self.aliens:
                alien.walk()
                if alien.pos()[1] <= self.window.BOTTOM:
                    self.lost = True
            self.window.window.update()
        if self.lost:
            self.lost_screen()
    
    def remove_item(self, item, item_list):
            item.clear()
            item.hideturtle()
            self.window.window.update()
            item_list.remove(item)
            turtle.turtles().remove(item)

    def lost_screen(self):
        self.window.window.clear()
        self.window.window.title("lost...")
        self.window.window.bgcolor(0.2, 0.2, 0.2)
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("lightgray")
        self.writer.write(f"you lost, your score is {self.score}", align="center", font=("System", 20, "bold"))

class Window:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.tracer(0)
        self.window.setup(0.5, 0.75)
        self.window.bgcolor(0.2, 0.2, 0.2)
        self.window.title("Space Invaders")

        self.LEFT = -self.window.window_width() / 2
        self.RIGHT = self.window.window_width() / 2
        self.TOP = self.window.window_height() / 2
        self.BOTTOM = -self.window.window_height() / 2
        self.FLOOR_LEVEL = 0.9 * self.BOTTOM
        self.SIDEBUFFER = 0.06 * self.window.window_width()

    def keybinds(self, player):
        self.window.onkeypress(player.move_left, "Left")
        self.window.onkeypress(player.move_right, "Right")
        self.window.onkeypress(player.fire_cannon, "space")
        self.window.onkeypress(turtle.bye, "q")

        self.window.listen()


if __name__ == "__main__":
    turtle.register_shape("teddy-bear.gif")
    turtle.register_shape("heart.gif")
    game = Game()
    game.game_loop()
    turtle.done()
