import colorgram
from turtle import Turtle
import turtle as t
import random

# Using colorgram.py to collect a color palatte from a picture, and using that palatte to create a hirst drawing replica using turtle.

poka = Turtle() 
t.Screen
t.bgcolor('#f0f0eb')
t.colormode(255)
poka.ht()
poka.speed(.1)  # Lines 8 - 13 initate the turtle and add it to a variable poka as well as changing the characteristics both the screen and turtle will have.

colors = colorgram.extract('photo.jpg', 15) # photo where the palatte was extracted from
color_list = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110)] # The several colors extracted are stored in a list of tuples to randomly choose from
y_axis = 0 # used to go up after 10 dots are drawn
poka.penup() 
for dots in range(100): # amount of dots to be drawn
    poka.pencolor(random.choice(color_list))
    
    if dots % 10 == 0: # Once dots drawn == 10 the dots will return to the inital dot and go up by the number stored in y_axis
        poka.home()
        poka.sety(y_axis)
        poka.dot(20)
        y_axis += 33 #increment the y_axis
    else:
        poka.forward(33)
        poka.dot(20)



t.exitonclick()
