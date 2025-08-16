from turtle import *   
import colorsys as cs  

bgcolor('black')
pensize(2)
speed(-2)
h = 0 

up()
goto(0, -100)
down()

for i in range(250): 
    c = cs.hsv_to_rgb(h, 1, 1)
    pencolor(c)
    fillcolor(c)

    begin_fill()
    circle(50)
    end_fill()

    h += 0.01 

    up()
    circle(i, 25)
    down()

done()


