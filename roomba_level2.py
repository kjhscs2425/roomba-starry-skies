# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster


# Draw the Level 2 version of the room
window = room.draw_room(level = 2, radius = 5)

###
# Start your code here
 

import turtle
speed (50)
for i in range(3):
    turtle.forward(40*4)
    turtle.right(270)
    speed (50)
for i in range(2):
   turtle.forward(40*3)
   turtle.left(90)
   speed (50)
for i in range(2):
    turtle.forward(40*2)
    turtle.left(90)
    speed (50)
for i in range(2):
    turtle.forward(40)
    turtle.left(90)
    speed (50)




# End your code here
###
 
window.exitonclick()
