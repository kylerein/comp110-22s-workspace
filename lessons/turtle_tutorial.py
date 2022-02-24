from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.color("blue")
leo.speed(500)
leo.penup()
leo.goto(-40, 0)
leo.pendown()


i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()

bob: Turtle = Turtle()