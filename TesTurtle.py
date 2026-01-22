import turtle
import colorsys
import random

def setup():
    screen = turtle.Screen()
    screen.setup(1000, 800)
    screen.bgcolor('black')
    screen.title("Galaxy Spiral Nebula - Simple Version")
    turtle.colormode(255)
    return screen

def draw_star(x, y, size=2):
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.goto(x, y)
    s.pendown()
    s.dot(size * 2, 'white')

def galaxy_spiral():
    screen = setup()
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()

    for _ in range(5):
        draw_star(random.randint(-480, 480), random.randint(-360, 360), size=random.randint(1, 3))

    def spawn_star():
        draw_star(random.randint(-480, 480), random.randint(-360, 360), size=random.randint(1, 3))
        screen.ontimer(spawn_star, 5000)  

    screen.ontimer(spawn_star, 5000)

    screen.update()

    for i in range(450):
        hue = (i / 450) * 0.8 + 0.1
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 0.8, 1)]
        t.color(r, g, b)

        t.forward(i * 0.7)
        t.right(91)

    screen.exitonclick()

galaxy_spiral()
