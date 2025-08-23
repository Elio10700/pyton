import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.title("star")
t = turtle.Turtle()
screen.bgcolor("white")
t.width(4)
t.color("black" )
n = 3
a = 360/n
for i in range(n):
    t.forward(100)
    t.left(a)
t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()
for i in range(n):
    t.forward(100)
    t.right(a)
turtle.done()