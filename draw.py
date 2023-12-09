import turtle

#Setup Screen

screen = turtle.Screen()


t = turtle.Pen()
t.forward(50)
t.left(90)


#Click to exit to prevent instant window closing
screen.exitonclick()

def mysquare(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)