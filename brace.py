import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Spirograph (Slow and Centered)")

t = turtle.Turtle()
t.speed(0)
t.width(2)

h = 0.0

for i in range(125):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    t.pencolor(c)

    t.forward(i) 
    t.right(91)
    t.circle(i / 2, 90) 
    t.left(120)
    t.forward(i / 2)
    t.right(150)

    h += 0.005

t.hideturtle()
screen.mainloop()