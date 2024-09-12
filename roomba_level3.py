# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here

import turtle
forward (40)
right (90)
forward (120)
backward (240)
left(90)
forward (40)
right (90)
forward (7*40)
backward (8*40)
left (90)
forward (40)
right (90)
forward (8*40)
left (90)
forward (40)
left(90)
forward (8*40)
right (90)
forward (40)
left(90)
forward(40)
backward(10*40)
forward (40)
right (90)
forward (40)
left (90)
forward (8*40)
right (90)
forward (40)
right(90)
forward (8*40)
left (90)
forward (40)
left (90)
forward (40*8)
right (180)
forward(40)
left(90)
forward (40)
right(90)
forward(40*6)
backward (40*3)
left(90)
forward(40)
# End your code here
###
 
window.exitonclick()
