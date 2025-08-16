from turtle import *
import colorsys as cs

bgcolor("black")  
pensize(2)
speed(-2)         
h = 0

up()
goto(0, -100)  
down()

# --- Main loop to draw the colorful spiral ---
for i in range(250):
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