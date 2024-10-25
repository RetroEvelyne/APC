import turtle

class SolarSystem:
    def __init__(self) -> None:
        self.window = Window()
        self.planets = [Planet() for _ in range(3)]


class Planet(turtle.Turtle):
    def __init__(self, *args, **kwargs) -> None:
        super(Planet, self).__init__(*args, **kwargs)
        pass


class Window:
    def __init__(self) -> None:
        self.window = turtle.Screen()
        self.window.tracer(0)
        self.window.setup(0.5, 0.75)
        self.window.bgcolor(0.2, 0.2, 0.2)
        self.window.title("Solar System")


if __name__ == "__main__":
    SolarSystem()
    turtle.done()
