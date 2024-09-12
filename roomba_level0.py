# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Mayaexit() <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import turtle
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
for i in range(3):
    turtle.forward(40*4)
    turtle.right(270)
for i in range(2):
   turtle.forward(40*3)
   turtle.left(90)
for i in range(2):
    turtle.forward(40*2)
    turtle.left(90)
for i in range(2):
    turtle.forward(40)
    turtle.left(90)
 
 
# End your code here
###
 
window.exitonclick()
