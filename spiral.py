import turtle

screen =turtle.Screen()
screen.screensize(400,400)
screen.title("spiral")
t = turtle.Turtle()
screen.bgcolor("grey")
t.width(1)
t.color("darkred")
a = 10
while True:
    t.forward(a)
    t.right(90)
    a = a + 2



