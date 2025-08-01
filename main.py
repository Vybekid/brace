import turtle 
import colorsys 

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Floral Starburst")

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.width(2)

h = 0.0 

for i in range(125): 
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    t.pencolor(c)

    t.penup()
    t.goto(0, 0)
    t.forward(i * 0.5)
    t.pendown()

    t.right(45)
    t.forward(i)
    t.left(90)
    t.forward(i)

    h += 0.008 

    t.left(28)

screen.mainloop()

