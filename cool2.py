import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Floral Starburst")

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.width(2)

# Set initial hue for color cycling
h = 0.0

# Main loop to draw the starburst
for i in range(120):
    # Convert HSV color to RGB
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    t.pencolor(c)

    # Move to starting position for each petal
    t.penup()
    t.goto(0, 0)
    t.forward(i * 0.5)
    t.pendown()

    # Draw a petal/spike of the star
    t.right(45)
    t.forward(i)
    t.left(90)
    t.forward(i)

    # Increment the hue for the next color
    h += 0.008

    # Rotate the turtle for the next petal
    t.left(28)

# Keep the window open after drawing is complete
screen.mainloop()