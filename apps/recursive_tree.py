import turtle
import colorsys

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Recursive Fractal Forest")
screen.tracer(0, 0)
artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)

def draw_branch(length, depth, hue):
    if depth == 0:
        return
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    artist.pencolor(color)
    artist.pensize(max(depth / 2, 1))
    artist.forward(length)
    artist.right(22)
    draw_branch(length * 0.76, depth - 1, hue + 0.015)
    artist.left(44)
    draw_branch(length * 0.76, depth - 1, hue + 0.015)
    artist.right(22)
    artist.backward(length)

def plant_tree(x_position, starting_hue):
    artist.penup()
    artist.goto(x_position, -320)
    artist.setheading(90)
    artist.pendown()
    draw_branch(110, 10, starting_hue)

tree_positions = [-320, -160, 0, 160, 320]
hues = [0.30, 0.55, 0.05, 0.75, 0.15]
for position, hue in zip(tree_positions, hues):
    plant_tree(position, hue)
screen.update()
turtle.done()