#Silas Stary
#P4LAB2b: Initials

#First I import the turtle and give its attributes

import turtle
win = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)
t.pencolor("green")
t.shape("turtle")

#now I make the turtle draw an S. Since my initials are 'SS' I will do a loop that repeats twice

for i in range(2):
    t.forward(50)
    t.left(36)
    t.forward(25)
    t.left(36)
    t.forward(20)
    t.left(36)
    t.forward(25)
    t.left(36)
    t.forward(25)
    t.left(36)
    t.forward(20)
    t.right(36)
    t.forward(25)
    t.right(36)
    t.forward(20)
    t.right(36)
    t.forward(25)
    t.right(36)
    t.forward(25)
    t.right(36)
    t.forward(25)
    t.penup()
    t.forward(150)
    t.right(90)
    t.forward(150)
    t.left(90)
    t.pendown()
