import turtle

class Cannon(turtle.Turtle):
    def __init__(self, window, *args, **kwargs):
        super(Cannon, self).__init__(*args, **kwargs)
        self.window = window
        self.penup()
        self.color(1, 1, 1)
        self.shape("square")
        self.setposition(0, self.window.FLOOR_LEVEL)
        self.step = 20
        self.lasers = []
    
    def fire_cannon(self):
        self.lasers.append(Laser(self))
    
    def move_left(self):
        new_x = self.xcor() - self.step
        if new_x >= self.window.LEFT + self.window.SIDEBUFFER:
            self.setx(new_x)
        self.draw_cannon()
    
    def move_right(self):
        new_x = self.xcor() + self.step
        if new_x <= self.window.RIGHT - 1.15*self.window.SIDEBUFFER:
            self.setx(new_x)
        self.draw_cannon()
    
    def draw_cannon(self):
        self.clear()
        self.turtlesize(1, 4) # Base
        self.stamp()
        self.sety(self.window.FLOOR_LEVEL + 10)
        self.turtlesize(1, 1.5) # Next tier
        self.stamp()
        self.sety(self.window.FLOOR_LEVEL + 20)
        self.turtlesize(0.8, 0.3) # Tip of cannon
        self.stamp()
        self.sety(self.window.FLOOR_LEVEL)
        self.window.window.update()

class Laser(turtle.Turtle):
    def __init__(self, player, *args, **kwargs):
        super(Laser, self).__init__(*args, **kwargs)
        self.penup()
        self.color(1, 0, 0)
        self.hideturtle()
        # self.shape("heart.gif")
        self.setposition(player.xcor(), player.ycor())
        self.setheading(90)
        self.forward(20)
        self.pendown()
        self.pensize(5)

        self.laser_length = 20
        self.laser_speed = 10

    def move(self):
        self.clear()
        self.forward(self.laser_speed)
        self.forward(self.laser_length)
        self.forward(-self.laser_length)
