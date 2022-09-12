import turtle
import random


class DrawFractal:
    def __init__(self, turtle_drawer, scale=2,
                 start_position=(20, 40), view=(0, 0)):
        self.const_value = complex(-0.1244, 0.756)
        self.pos_x = start_position[0]
        self.pos_y = start_position[1]
        self.scale = scale
        self.view = view
        self.drawer = turtle_drawer

    def paint_pixels(self, red, green, blue):
        self.drawer.penup()
        x_pixel_number = self.pos_x - self.view[0]
        y_pixel_number = self.pos_y - self.view[1]
        self.drawer.goto(x_pixel_number, y_pixel_number)
        self.drawer.pendown()
        self.drawer.color(red, green, blue)
        self.drawer.dot()

    def render(self, n_iter, fract_size=(600, 600)):
        number = random.randint(1, 7)
        const_value = fractals_const[number]
        border = min(fract_size[0], fract_size[1]) // 2
        for y in range(-border + self.view[1], border + self.view[1], 2):
            for x in range(-border + self.view[0], border + self.view[0], 2):
                a = x / self.scale
                b = y / self.scale
                z = complex(a, b)
                n = 0
                for n in range(n_iter):
                    z = z ** 2 + const_value
                    if abs(z) > 2:
                        break
                if n == n_iter - 1:
                    r = g = b = 0
                else:
                    r = (n % 3) * 32 + 90
                    g = (n % 3) * 34
                    b = (n % 4) * 36 + 90
                self.paint_pixels(r, g, b)


fractals_const = {
    1: complex(-1),
    2: complex(-0.2, 0.75),
    3: complex(-0.1244, 0.756),
    4: complex(-0.1194, 0.6289),
    5: complex(-0.7382, 0.0827),
    6: complex(0.377, -0.248)
}


class Application:
    def __init__(self, window_size=(600, 600)):
        self.screen = turtle.Screen()
        self.window_size = window_size
        self.pos = (0, 0)
        self.screen.colormode(255)
        self.screen.delay(0)
        self.screen.tracer(10000)
        self.drawer = turtle.Turtle()

    def run(self):
        self.setup_screen()
        fractal = DrawFractal(self.drawer)
        fractal.render(100, self.window_size)

    def setup_screen(self):
        self.screen.title("Julia set")
        self.screen.bgcolor(120, 10, 125)
        self.drawer.hideturtle()
        turtle.color("white")
        turtle.write("It's loading...", align='center',
                     font=("Verdana", 25, "normal"))
        self.drawer.speed(0)
        turtle.done()


if __name__ == "__main__":
    app = Application()
    app.run()
