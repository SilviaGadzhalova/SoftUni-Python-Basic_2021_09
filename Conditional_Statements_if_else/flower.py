import turtle

turtle.speed(0)
turtle.bgcolor("black")
colors=['red','purple','orange','yellow','blue','green']
t=turtle.Turtle()

t.shape("turtle")
t.speed(15)
t.left(0)

t.penup
size=18

def petal ():
    t.pendown()
    for x in range (40):
        t.pencolor(colors[x%6])
        t.pensize(5)
        t.forward(size)
        t.left(x)
    t.penup()
left_d = -15
for pet in range (8):
    petal()
    t.goto(0,0)
    t.left(-15)