import turtle

#Setup Screen

screen = turtle.Screen()


t = turtle.Pen()
t.forward(50)
t.left(90)


#Click to exit to prevent instant window closing
screen.exitonclick()

for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)