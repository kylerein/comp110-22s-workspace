"""A pleasant rural home with two lovely trees on a sunny day."""

__author__ = "730403346"

from turtle import Turtle, done


def main() -> None:
    """The entrypoint of my scene."""
    andy: Turtle = Turtle()
    andy.speed(5)
    draw_sun(andy, 250, 160, 50)
    draw_tree(andy, -200, 10, 20)
    draw_tree(andy, 200, 10, 20)
    draw_house(andy, 30, 15, 30)
    draw_grass(andy, -350, -20, 40)
    done()


def draw_sun(andy: Turtle, x: float, y: float, radius: float) -> None:
    """Draw the sun in the top right corner."""
    andy.color("yellow")
    andy.begin_fill()
    andy.penup()
    andy.goto(x, y) 
    andy.setheading(0.0)
    andy.pendown()
    andy.circle(radius)
    andy.end_fill()
    andy.penup()
    andy.color("orange")
    andy.goto(x, y)
    andy.setheading(0.0)
    andy.pendown
    andy.circle(radius)
    andy.end_fill()
    andy.penup()


def draw_tree(andy: Turtle, x: float, y: float, width: float) -> None:
    """Draw a tree."""
    andy.color("green")
    andy.begin_fill()
    andy.penup()
    andy.goto(x, y) 
    andy.setheading(0.0)
    andy.pendown()
    i: int = 0
    while i < 3:
        andy.forward(100)
        andy.left(120)
        i = i + 1
    andy.end_fill()
    andy.penup()
    andy.begin_fill()
    andy.goto(x, y + 40)
    andy.setheading(0.0)
    andy.pendown()
    j: int = 0
    while j < 3:
        andy.forward(100)
        andy.left(120)
        j = j + 1
    andy.end_fill()
    andy.penup()
    andy.color("brown")
    andy.begin_fill()
    andy.goto(x + 40, y)
    andy.pendown()
    andy.setheading(0.0)
    k: int = 0
    while k < 2:
        andy.forward(20)
        andy.right(90)
        andy.forward(30)
        andy.right(90)
        k = k + 1
    andy.end_fill()
    andy.penup()
    

def draw_house(andy: Turtle, x: float, y: float, width: float) -> None:
    """Draw a house."""
    andy.color("red")
    andy.begin_fill()
    andy.penup()
    andy.goto(x, y + 50) 
    andy.setheading(0.0)
    andy.pendown()
    i: int = 0
    while i < 3:
        andy.forward(100)
        andy.left(120)
        i = i + 1
    andy.end_fill()
    andy.penup()
    andy.color("blue")
    andy.begin_fill()
    andy.goto(x, y - 50)
    andy.setheading(0.0)
    andy.pendown()
    k: int = 0
    while (k < 4):
        andy.forward(100)
        andy.left(90)
        k = k + 1
    andy.end_fill()
    andy.pendown()


def draw_grass(andy: Turtle, x: float, y: float, width: float) -> None:
    """Draw the grass covering the bottom half of the image."""
    andy.color("green")
    andy.begin_fill()
    andy.penup()
    andy.goto(x, y) 
    andy.setheading(0.0)
    andy.pendown()
    i: int = 0
    while i < 2:
        andy.forward(1000)
        andy.right(90)
        andy.forward(300)
        andy.right(90)
        i = i + 1
    andy.end_fill()
    andy.penup()


if __name__ == "__main__":
    main()