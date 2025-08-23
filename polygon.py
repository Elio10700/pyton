import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.title("Polygon")
t = turtle.Turtle()
screen.bgcolor("goldenrod")
t.color("black" )
n = 6
a = 360/n
for i in range(6):
    t.forward(100)
    t.right(a)
turtle.done()