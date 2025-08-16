from turtle import *
import colorsys as cs

# --- Setup the Screen and Turtle ---
bgcolor("black")  # Set the background color to black
pensize(4)        # Set the thickness of the drawing outline
tracer(100)       # Speed up the drawing animation

# --- Initial variables ---
h = 0             # Initialize hue value for colors

# --- Position the turtle to start ---
up()              # Lift the pen to move without drawing
goto(40, -10)     # Move to the starting position
down()            # Put the pen down to start drawing

# --- Main loop to draw the pattern ---
for i in range(600):
    # Convert HSV color to RGB color
    # The hue (h) changes in each loop, while saturation and value are max (1)
    c = cs.hsv_to_rgb(h, 1, 1)

    # Set the colors
    color('black')    # Set the outline color of the shape
    fillcolor(c)      # Set the fill color of the shape

    # Position the turtle for the next shape in a spiral path
    up()
    circle(i, 60)
    down()

    # Draw and fill one of the leaf-like shapes
    begin_fill()
    circle(40, 145)
    left(10)
    circle(40, 145)
    end_fill()        # This command completes the shape filling

    # Increment the hue to change the color for the next shape
    h += 0.005

# --- Keep the window open ---
done()           