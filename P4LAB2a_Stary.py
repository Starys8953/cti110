#Silas Stary
#P4LAB2a: Shapes

#First I import the turtle and give its attributes

import turtle
win = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)
t.pencolor("green")
t.shape("turtle")
#to make the turtle draw a square I insert a loop with a range of 4(as a square
#has 4 sides) and have it draw the 4 sides.
for i in range(4):
    t.forward(100)
    t.left(90)
#now I use penup and pendown to move the turtle away from the square
t.penup()
t.forward(250)
t.pendown()
#now I insert a loop with a range of three in order to draw the triangle
for i in range(3):
    t.forward(100)
    t.left(120)
