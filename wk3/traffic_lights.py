import turtle

window = turtle.Screen()

window.title("Traffic Light Simulation")
window.bgcolor("darkgrey")

light = turtle.Turtle()
light.shape("circle")
light.turtlesize(20)

def update_light_color(color):
    light.color(color)

def go_green():
    update_light_color("green")
def go_yellow():
    update_light_color("yellow")
def go_red():
    update_light_color("red")

turtle.onkeypress(go_green, "g")
turtle.onkeypress(go_yellow, "y")
turtle.onkeypress(go_red, "r")

window.listen()
window.mainloop()

