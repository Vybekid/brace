from turtle import *
import colorsys as cs

# --- Setup the Screen and Turtle ---
bgcolor("black")   # Change 1: A dark background makes the colors pop
pensize(2)
speed(0)           # Change 2: Sets the drawing speed to the fastest possible
h = 0

# --- Position the turtle ---
up()
goto(0, -100)      # Change 3: Start lower to center the final spiral
down()

# --- Main loop to draw the colorful spiral ---
for i in range(300):
    c = cs.hsv_to_rgb(h, 1, 1)
    pencolor(c)
    fillcolor(c)

    begin_fill()
    # Change 4: Draw a different, simple shape (a circle)
    circle(50)
    end_fill()

    h += 0.01          # Change 5: Adjusts the speed of the color change

    # Change 6: Move for the next shape in a tighter spiral
    up()
    circle(i, 25)
    down()

# --- Keep the window open ---
done()