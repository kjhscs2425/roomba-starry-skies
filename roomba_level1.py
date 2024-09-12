# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import left, forward, backward
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here
import turtle
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




# notes from lecture 09/09 below:
# square = 40
# for i in range(4):
#     arm_length = (4 - i) + square
#     print(arm_length)
#     for _ in range (2):
#          #because after going 4*40 
#         left(90)
#         forward (arm_length)
 
# End your code here
###
 
window.exitonclick()


# height = 15
# width = 20

# forward ((height - 1)*square)
# for i in range (1, min(height, width) + 1):
#     vertical_arm_length = (height - i) * square
#     horizontal_arm_length = (width - i) * square
#     left(90)
#     forward(horizontal_arm_length)
#     left(90)
#     forward(vertical_arm_length)

# bug: when something is going wrong in the code
# debugging: figure out why code is wrong
# how to debug: text editor will usually tell you + pay attention to code